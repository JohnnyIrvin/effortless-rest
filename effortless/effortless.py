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
from typing import Any


class Effortless:
    def __init__(self, orm: Any, web: Any) -> None:
        """
        Effortless is a class that integrates Effortless with a framework.

        Args:
            orm (Any): Object-relational mapper (ORM).
            web (Any): Web framework to use.
        """
        self._orm = orm
        self._web = web
    
    def build(self, models: ModuleType) -> "Effortless":
        """
        Serve is a method that starts the server.

        Args:
            models (ModuleType): Module containing dataclasses.
        """
        stores = self._orm.create_stores(models=models)
        routes = self._web.create_routes(models=models, stores=stores)

        return self
 