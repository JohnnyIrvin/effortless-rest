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
import os
import pathlib

import uvicorn

from effortless import Effortless, EffortlessFastAPI, EffortlessSQLAlchemy

from . import models

DATABASE_DIRECTORY = f'{pathlib.Path(__file__).parent.absolute()}/databases'

if not os.path.exists(DATABASE_DIRECTORY):
    os.makedirs(DATABASE_DIRECTORY)

uvicorn.run(
    Effortless(
        orm=EffortlessSQLAlchemy(
            connection=f'sqlite+pysqlite:///{DATABASE_DIRECTORY}/tasks.db',
        ),
        web=EffortlessFastAPI(),
    ).build(
        models=models,
    ),
    host='127.0.0.1',
    port=13373,
)
