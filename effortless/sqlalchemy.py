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
from dataclasses import fields, is_dataclass
from types import ModuleType
from typing import Dict, Optional, TypeVar
from uuid import uuid4

from sqlalchemy import UUID, Column, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import registry as SQLAlchemyRegistry

from .store import Store

T = TypeVar("T")

class _AlchemyStore:
    def __init__(self, dataclass: T, registry: SQLAlchemyRegistry) -> None:
        dataclass.__tablename__ = dataclass.__name__.lower()
        dataclass.uuid = Column(
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid4,
            unique=True,
            nullable=False
        )

        self._table = registry.mapped(dataclass)

class EffortlessSQLAlchemy:
    def __init__(self) -> None:
        self._registry = SQLAlchemyRegistry()
        
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
        return _AlchemyStore(dataclass=model, registry=self._registry)

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

        return stores
