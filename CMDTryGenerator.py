# -*- coding: utf-8 -*-

import trdg

from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromStrings
)

# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromStrings(
    ['Test1', 'Test2', 'Test3'],
    blur=2,
    random_blur=True
)


for img in generator:
    print(img)