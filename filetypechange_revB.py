import numpy as np
import subprocess
import os
from ase.io import read,write



input_directory = './Files_to_change'
output_directory = './Changed_files'

file_list = os.listdir(input_directory)

for filename in file_list:
    input_file_path = os.path.join(input_directory, filename)
    print(input_file_path)
    atoms = read(input_file_path, format='lammps-dump-text')
    output_filename = filename + '.xyz'
    print(output_filename)
    output_filepath = os.path.join(output_directory, output_filename)
    write(output_filepath, atoms, format='extxyz')
