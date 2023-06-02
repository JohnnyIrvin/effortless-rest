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


class EffortlessFlask:
    def integrate(self, models: list[dataclass], integrations: dict[type, Integration]) -> "EffortlessFlask":
        """
        Run integrations on models and return an instance of EffortlessFlask. Use this method to
        use Flask with the Effortless framework. Flask will handle the HTTP requests and responses
        while Effortless will pass it models and additional information from other integrations.

        Args:
            models (list[dataclass]): The models to integrate into the microservice.
            integrations (dict[type, Integration]):  The integrations to run on the models.
                Examples of integrations are:
                    - Database integration
                    - API integration
                    - Logging integration
                    - etc.

        Returns:
            EffortlessFlask: An instance of EffortlessFlask with the integrations ran on the models.
        """        
        raise NotImplementedError('EffortlessFlask is not implemented yet.')
