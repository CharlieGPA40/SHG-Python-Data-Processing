import os
from tkinter import *
from matplotlib import pyplot
import matplotlib.patches as patches
import numpy as np
import pandas as pd
from tkinter import filedialog


class SHG_Processing():
    def shg_sin(x):
        return np.sin(2 * x) ** 2


    SHGpath = 'SHG'  # Processed data directory
    isExist = os.path.exists(SHGpath)
    if not isExist:  # Create a new directory because it does not exist
        os.makedirs(SHGpath)
        print("The new directory is created!")
        print('--------------------------------------------\n')

    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(initialdir="SHG RA/SHG Data")
    dir_list = os.listdir(folder_selected)
    file_name = dir_list[0]
    file_name_1 = dir_list[1]
    for i in range(len(file_name)-1, 0, -1):
        if file_name[i] == '_':
            file_name = file_name[:i]
            break

    folder_selected = folder_selected + "/"
    data_sel = 'n'
    Parameter = pd.read_csv(folder_selected + "Experimental_Parameters.txt",header=None)
    step_size = Parameter.iat[7,0]
    for i in range(len(step_size)-2, 0, -1):
        if step_size[i] == ' ':
            step_size = step_size[i+1:-1]
            break

    step_size = int(step_size)
    avg_x = 0
    avg_y = 0
    iteration = 0

    deg_file_org = []
    sig_file_org = []

    for degree in range(0, 360+step_size, step_size):
        SHG_Raw = np.loadtxt(folder_selected + file_name + "_{}deg".format(degree) + ".txt", dtype=int, delimiter=',')
        # SHG_Raw = SHG_Raw[128:384, 128:384]
        fig, ax = pyplot.subplots()
        im = ax.imshow(SHG_Raw, vmin=500, vmax=2300)
        fig.colorbar(im, ax=ax, label='SP Polarization')
        pyplot.title('SHO-TSO Fundamental Data at {} Degree'.format(degree))
        pyplot.show()