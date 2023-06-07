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
from types import ModuleType
from typing import Dict, TypeVar

from fastapi import FastAPI

from .store import Store

T = TypeVar("T")


class EffortlessFastAPI:
    def __init__(self) -> None:
        self._app = FastAPI()        

    def create_routes(self, models: ModuleType, stores: Dict[T, Store[T]]):
        for model, store in stores.items():
            name = model.__name__.lower()
            
            @self._app.get(f"/{name}")
            def get_all():
                return store.all()
            
            @self._app.get(f"/{name}/{{uuid}}")
            def get(uuid: str):
                return store.get(uuid)
            
            @self._app.post(f"/{name}")
            def create(m: model):
                created_uuid = store.create(m)

                print(created_uuid)

                return {
                    "uuid": created_uuid
                }
            
            @self._app.delete(f"/{name}/{{uuid}}")
            def delete(uuid: str):
                store.delete(uuid)
            
            @self._app.put(f"/{name}/{{uuid}}")
            def update(uuid: str, m: model):
                store.update(uuid, m)
