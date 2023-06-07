# Copyright (c) 2021-2023 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import enum
from dataclasses import asdict, dataclass, fields, is_dataclass
from types import ModuleType
from typing import Dict, Optional, TypeVar
from uuid import UUID, uuid4

from sqlalchemy import (Column, Engine, Enum, Float, Integer, String,
                        create_engine)
from sqlalchemy.orm import Session, mapped_column
from sqlalchemy.orm import registry as SQLAlchemyRegistry

from .store import Store

T = TypeVar("T", bound=dataclass)

class _AlchemyStore:

    def _get_compatible_column(self, value: type) -> Column:
        supported = {
            str: String,
            int: Integer,
            float: Float,
            enum.Enum: Enum
        }

        for key, val in supported.items():
            if not issubclass(value, key):
                continue

            if issubclass(value, enum.Enum):
                return Column(Enum(value), nullable=False)
            
            return Column(val())
        
        raise ValueError(f"Unsupported type {value}")
    
    def __init__(self, dataclass: T, registry: SQLAlchemyRegistry, engine: Engine) -> None:
        dataclass.__tablename__ = dataclass.__name__.lower()

        dataclass.id = Column(
            String(),
            primary_key=True,
            default=uuid4,
            unique=True,
            nullable=False
        )

        for field in fields(dataclass):
            if field.name == "id":
                continue
            
            setattr(dataclass, field.name, self._get_compatible_column(field.type))

        self._dataclass = dataclass
        self._table = registry.mapped(dataclass)
        self._engine = engine

    def get(self, uuid: UUID) -> Optional[T]:
        with Session(self._engine) as session:
            return session.get(self._dataclass, uuid)

    def update(self, uuid: UUID, value: T) -> "Store[T]":
        with Session(self._engine) as session:
            existing = session.get(self._dataclass, uuid)

            if existing is None:
                raise ValueError(f"Could not find {self._dataclass.__name__} with uuid {uuid}")

            for key, val in asdict(value).items():
                if key == "uuid":
                    continue

                setattr(existing, key, val)

            session.commit()

        return self

    def delete(self, uuid: UUID) -> "Store[T]":
        with Session(self._engine) as session:
            existing = session.get(self._dataclass, uuid)

            if existing is None:
                raise ValueError(f"Could not find {self._dataclass.__name__} with uuid {uuid}")

            session.delete(existing)
            session.commit()

        return self

    def create(self, value: T) -> UUID:
        if hasattr(value, "id"):
            value.id = str(uuid4())

        with Session(self._engine) as session:
            session.add(value)
            session.commit()
            session.refresh(value)

        return value.id
    
    def all(self) -> list[T]:
        with Session(self._engine) as session:
            return session.query(self._dataclass).all()


class EffortlessSQLAlchemy:
    def __init__(self, connection: str) -> None:
        """
        __init__ is the constructor for EffortlessSQLAlchemy.

        Args:
            connection (str): SQLAlchemy connection string
        """        
        self._registry = SQLAlchemyRegistry()
        self._engine = create_engine(connection, echo=True)
        
    def _create_store(self, model: T) -> Store[T]:
        """
        _create_store is a method that creates a SQLAlchemy store. This
        method is called by create_stores. This method is not meant to be
        called directly.

        Args:
            model (T): Generic Dataclass, represented by [T]

        Returns:
            Store[T]: SQLAlchemy store which contains [T]
        """
        return _AlchemyStore(dataclass=model, registry=self._registry, engine=self._engine)
    
    def _save_tables(self) -> None:
        """
        _save_tables is a method that saves the SQLAlchemy tables.
        """
        self._registry.metadata.create_all(self._engine)

    def create_stores(self, models: ModuleType) -> Dict[T, Store[T]]:
        """
        create_stores is a method that creates SQLAlchemy stores.

        Args:
            models (ModuleType): Module containing dataclasses

        Returns:
            Dict[T, Store[T]]: Dictionary of SQLAlchemy stores
        """
        stores = {}

        for _, model in models.__dict__.items():
            if not isinstance(model, type):
                continue

            if not is_dataclass(model):
                continue

            stores[model] = self._create_store(model=model)
            self._save_tables()

        from sqlalchemy import inspect
        inspector = inspect(self._engine)
        for table_name in inspector.get_table_names():
            for column_name in inspector.get_columns(table_name):
                print(f'Table: {table_name} {"*" * 10} Column: {column_name}')
    
        return stores
