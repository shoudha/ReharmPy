import os
import sys
import pandas as pd
import numpy as np

notes_dict = {
    0: 'A',
    1: 'A#',
    2: 'B',
    3: 'C',
    4: 'C#',
    5: 'D',
    6: 'D#',
    7: 'E',
    8: 'F',
    9: 'F#',
    10: 'G',
    11: 'G#',
}

# scale formula: how many semitones to skip from the current note to get 
# to the next note of scale
scale_formula = {
    'M': [2, 2, 1, 2, 2, 2, 1],
    'm': [2, 1, 2, 2, 1, 2, 2], 
}

chord_formula = {
    'M': [4, 3, ],
    'm': [3, 4, ],
    'M7': [4, 3, 4, ],
    'm7': [3, 4, 3, ],
    '7': [4, 3, 3, ],
    'm7b5': [3, 3, 4, ],
    'dim': [3, 3, 3, ],
    'sus4': [5, 2, ],
}

chords_in_scale_formula = {
    'M': [4, 3, ],
    'm': [3, 4, ],
    'M7': [4, 3, 4, ],
    'm7': [3, 4, 3, ],
    '7': [4, 3, 3, ],
    'm7b5': [3, 3, 4, ],
    'dim': [3, 3, 3, ],
    
    
}
