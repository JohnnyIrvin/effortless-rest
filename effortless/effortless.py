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
from dataclasses import dataclass

from .integrations import Integration


class Effortless:
    def __init__(self, models: list[dataclass]) -> 'Effortless':
        """
        Constructor for the Effortless class.

        Args:
            models (list[dataclass]): A list of dataclasses that represent
                the models of the application.
        """        
        self._models = models
        self._integrations = {}
    
    def uses(self, integration_type: type, implementation: Integration) -> 'Effortless':
        """
        Uses is a method that adds an integration to the Effortless

        Args:
            integration_type (type): The type of integration to add. (e.g. OrmIntegration)
            implementation (Integration): The implementation of the integration to add. (e.g. EffortlessSQLAlchemy)

        Returns:
            Effortless: The Effortless instance.
        """
        self._integrations[integration_type] = implementation
        return self
    
    def run(self) -> 'Effortless':
        """
        Run is a method that runs the Effortless instance.

        Returns:
            Effortless: The Effortless instance.
        """        
        for integration in self._integrations.values():
            integration(self._integrations, self._models)

        return self
