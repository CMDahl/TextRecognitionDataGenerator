# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)

# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromDict(
    count=4,
    language="da",
)



for img, lbl in generator:
    img.show()
    print(lbl)