#!/usr/bin/env python
# Path_generation
# use UTF-8
# Python 3.6.3

import os

label_map = {
    'left': 0,
    'right': 1
}

with open('data.txt', 'w') as f:
    for root, dirs, files in os.walk('data'):
        for filename in files:
            filepath = os.sep.join([root, filename])
            dirname = root.split(os.sep)[-1]
            label = label_map[dirname]
            line = '{},{}\n'.format(filepath, label)
            f.write(line)
