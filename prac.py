import os
import sys
import pandas as pd
import numpy as np

import helpers.util
import helpers.constants


root_name='A'
scale_type='m'
scale_notes, scale_notes_names = helpers.util.notes_of_scale(root_name=root_name, scale_type=scale_type)
print(f'{root_name}{scale_type} notes: {scale_notes_names}')


root_name='B'
chord_type='dim'
chord_notes, chord_notes_names = helpers.util.notes_of_chord(root_name=root_name, chord_type=chord_type)
print(f'{root_name}{chord_type} notes: {chord_notes_names}')


notes_names = ['C', 'F', 'G']
root_name='C'
chord_name = helpers.util.chord_name_from_notes(notes_names=notes_names, root_name=root_name)
print(f'{notes_names} with root {root_name}: {chord_name}')


root_name='C'
scale_type='M'
chords_notes, root_notes, chords_names = helpers.util.chords_of_scale(root_name=root_name, scale_type=scale_type)
print(f'{root_name}{scale_type} chords: {chords_names}')


root_name = 'C'
melody_notes_names = ['C', 'D', 'E']
scale_type = 'M'
note_chords = helpers.util.chords_for_note(melody_notes_names=melody_notes_names, root_name=root_name, scale_type=scale_type)
print(f'chords for melody note(s) {melody_notes_names} in {root_name}{scale_type}: {note_chords}')
