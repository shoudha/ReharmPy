import os
import sys
from functools import reduce
from itertools import accumulate

import pandas as pd
import numpy as np

import helpers.constants

def notes_of_scale(root_name='C', scale_type='M', **kwargs):
    
    root = list(helpers.constants.notes_dict.values()).index(root_name)
    
    scale_formula = helpers.constants.scale_formula[scale_type]
    scale_notes = list(accumulate(scale_formula, initial=root))
    
    scale_notes = [s % 12 for s in scale_notes]
    assert scale_notes[0] == scale_notes[-1], "Scale starting and ending notes must be the same"
    del scale_notes[-1]
    
    scale_note_names = [helpers.constants.notes_dict[s] for s in scale_notes]
    
    return scale_notes, scale_note_names


def notes_of_chord(root_name='C', chord_type='M', **kwargs):
    
    root = list(helpers.constants.notes_dict.values()).index(root_name)
    
    chord_formula = helpers.constants.chord_formula[chord_type]
    
    chord_notes = list(accumulate(chord_formula, initial=root))
    chord_notes = [s % 12 for s in chord_notes]
    chord_notes_names = [helpers.constants.notes_dict[s] for s in chord_notes]

    return chord_notes, chord_notes_names


def chord_name_from_notes(notes_names=['C', 'E', 'G'], root_name='C', **kwargs):
    
    root = list(helpers.constants.notes_dict.values()).index(root_name)
    
    notes = [list(helpers.constants.notes_dict.values()).index(s) for s in notes_names]
    notes = np.sort([s+12 if s < root else s for s in notes])
    
    note_diffs = list(np.diff(notes))
    
    if note_diffs in helpers.constants.chord_formula.values():
        chord_ind = list(helpers.constants.chord_formula.values()).index(note_diffs)
        chord_type = list(helpers.constants.chord_formula)[chord_ind]
        chord_name = root_name + chord_type
    else:
        chord_name = 'Chord not in dictionary'
    
    return chord_name


def chords_of_scale(root_name='C', scale_type='M', **kwargs):
    
    scale_notes, scale_notes_names = helpers.util.notes_of_scale(root_name=root_name, 
                                                                 scale_type=scale_type)
    
    chords_notes = list()
    root_notes = list()
    
    for chord_type, chord_formula in helpers.constants.chord_formula.items():
        for root in scale_notes:
            chord_notes = list(accumulate(chord_formula, initial=root))
            chord_notes = [s % 12 for s in chord_notes]
            if set(chord_notes).issubset(set(scale_notes)):
                chords_notes.append(tuple(chord_notes))
                root_notes.append(root)
    
    assert len(root_notes) == len(chords_notes), "number of chords and roots do not match"
    
    chords_names = []
    
    for i in range(len(root_notes)):
        root_name = helpers.constants.notes_dict[root_notes[i]]
        notes_names = [helpers.constants.notes_dict[s] for s in chords_notes[i]]
        chord_name = helpers.util.chord_name_from_notes(notes_names=notes_names, root_name=root_name)
        chords_names.append(chord_name)
        
    return chords_notes, root_notes, chords_names


def melody_harmony_check(melody_notes_names=['C', 'D', 'E'], chords_notes=['C', 'E', 'G'], **kwargs):
        
    melody_notes = [list(helpers.constants.notes_dict.values()).index(s) for s in melody_notes_names]
    
    pass_all = []
    
    # atleast one common note between melody-harmony
    if any(x in melody_notes for x in chords_notes):
        pass_all.append(True)
    else:
        pass_all.append(False)
        
    # no b9 notes in melody relative to harmony
    chords_notes_sharp = [s+1 for s in list(chords_notes)]
    if not any(x in melody_notes for x in chords_notes_sharp):
        pass_all.append(True)
    else:
        pass_all.append(False)
    
    pass_all = all(pass_all) and bool(len(pass_all))
    return pass_all


def chords_for_note(config=None, melody_notes_names='C', root_name='C', scale_type='M', **kwargs):
    
    chords_notes, root_notes, chords_names = helpers.util.chords_of_scale(root_name=root_name, scale_type=scale_type)
    
    chords_in_scale = []
    for (s, t) in zip(chords_notes, chords_names):
                
        if melody_harmony_check(melody_notes_names=melody_notes_names, chords_notes=s):
            chords_in_scale.append(t)
    
    chords_dict = {
        'chords_in_scale': chords_in_scale,
        'chords_out_scale': None,
    }
    return chords_dict

























    
    