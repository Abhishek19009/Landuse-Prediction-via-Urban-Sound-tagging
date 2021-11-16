import glob
import os
from gammatone.plot import take_input
import numpy as np

ind_files = np.array(glob.glob("./audio_datasets/Industrial/*"))
comm_files = np.array(glob.glob("./audio_datasets/Commercial/*"))
res_files = np.array(glob.glob("./audio_datasets/Residential/*"))


for i, audio in enumerate(ind_files):
    take_input(audio, "Industrial")
