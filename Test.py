
import os
from tkinter import *
from matplotlib import pyplot
import matplotlib.patches as patches
import numpy as np
import pandas as pd
from tkinter import filedialog

root = Tk()
root.withdraw()

folder_selected = filedialog.askdirectory(initialdir="SHG RA/SHG Data")
dir_list = os.listdir(folder_selected)
SHG_Raw = np.loadtxt(folder_selected + '/GSO_SHG_test_60deg' + ".txt", dtype=int, delimiter=',')

fig, ax = pyplot.subplots()
im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
im.set_clim(vmin=800, vmax=2200)
fig.colorbar(im, ax=ax, label='Interactive colorbar 80K')
pyplot.show()



# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_80K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 80K')
# pyplot.show()
#
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_75K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 75K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_70K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 70K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_65K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 65K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_60K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 60K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_55K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 55K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_50K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 50K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_45K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 45K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_40K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 40K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_30K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 35K')
# pyplot.show()
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_30K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 30K')
# pyplot.show()
#
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_25K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 25K')
# pyplot.show()
#
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_20K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 20K')
# pyplot.show()
#
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_15K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 15K')
# pyplot.show()
#
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_10K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 10K')
# pyplot.show()
#
# SHG_Raw = np.loadtxt(folder_selected + '/STO_Nb_0_002_5K_0deg' + ".txt", dtype=int, delimiter=',')
#
# fig, ax = pyplot.subplots()
# im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)
# im.set_clim(vmin=800, vmax=2200)
# fig.colorbar(im, ax=ax, label='Interactive colorbar 5K')
# pyplot.show()