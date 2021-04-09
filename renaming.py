""" A stimple tool for renaming files in a folder sequentially

    TODO a small/useful extension would be to have sequential_rename take paths instead
    of a folder
"""

from glob import glob
from itertools import groupby
import re
import os


def sequential_rename(path, start=1, pad=None):
    """Renames all files in the folder to a sequential list.
    The expected file format is <name>.<number>.<extension> 
    eg.
    prodeng.27.jpg

    The <number> will be renamed sequentially with buffered zeros
    eg.
    prodeng.27.jpg prodeng.32.jpg
    becomes
    prodeng.01.jpg prodeng.02.jpg

    Args:
        path (str): path to the directory with the files
        start (int): file number to start with
        pad (int): Digits in the file number, zeros will be padded for small numbers to fill the field.
            If not given padding is assigned automatically to fit the largest number (min 2)
            If 0 is given, no padding will be assigned.

    Returns:
        list(tuple): a list of tuples of old and new filenames
    """
    
    files = [f.strip(path) for f in glob(os.path.join(path, "*.*.*"))]

    paths_split = [f.rsplit('.', 2) for f in files]

    paths_split.sort(key=lambda ps: (ps[0],ps[-1]))
    filegroups = groupby(paths_split, key=lambda f:(f[0],f[-1])) # group by name and ext

    changed_files = []

    for name_ext, group in filegroups:
        old_numbers = (p[-2] for p in group)
        old_numbers = sorted((p for p in old_numbers if re.match(r"[0-9]+",p)), key=int) # Just ignore non-numbers

        if pad is None:
            highest = len(old_numbers) + start -1
            group_pad = max(len(str(highest)), 2) # no. digits in the highest number
        else:
            group_pad = pad
        
        for new_number, old_number in enumerate(old_numbers, start=start):
            name, ext = name_ext

            oldfile = '.'.join((name, old_number, ext))
            newfile = '.'.join((name, str(new_number).zfill(group_pad), ext))

            if oldfile == newfile:
                continue

            os.rename(os.path.join(path, oldfile), os.path.join(path, newfile))

            # about possible name clashes - for this application avoiding clashes is not necessary,
            # since lower numbers are renamed first, they can't clash with higher numbers.

            changed_files.append((oldfile, newfile))

    return changed_files