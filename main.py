# -----------------------------------------------------------#
# Name: Chunli Tang                                          #
# School: Auburn University                                  #
# -----------------------------------------------------------#

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
    Parameter = pd.read_csv(folder_selected + "Experimental_Parameters.txt", header=None, sep=':')
    step_size = Parameter.iat[7, 1]
    step_size = int(step_size)
    avg_x = 0
    avg_y = 0
    iteration = 0

    deg_file_org = []
    sig_file_org = []

    # for degree in range(0, 10, step_size):
    degree = 10
    SHG_Raw = np.loadtxt(folder_selected + file_name + "_{}deg".format(degree) + ".txt", dtype=int, delimiter=',')
    # SHG_Raw = SHG_Raw[128:384, 128:384]
    fig, ax = pyplot.subplots()
    im = ax.imshow(SHG_Raw, vmin=0, vmax=2000)
    polarization = Parameter.iat[8, 1]
    fig.colorbar(im, ax=ax, label='{} Polarization'.format(polarization))
    exposure_time = str(float(Parameter.iat[9, 1]))
    title = str(Parameter.iat[1, 1]) + '' + str(Parameter.iat[2, 1]) + '' + str(Parameter.iat[3, 1]) \
            + '\n' + str(Parameter.iat[4, 1]) + 'mW Exposure Time ' + exposure_time + 's Averaging ' \
            + str(int(Parameter.iat[11, 1]))
    pyplot.title(title + ' at {} Degree'.format(degree), pad=10, wrap=True)
    # pyplot.show()

    def onclick(event):
        if event.dblclick:
            global cur_x, cur_y, click
            cur_x = event.xdata
            cur_y = event.ydata
            click = event.button
            if click == 1:
                print('Closing')
                pyplot.close()
    connection_id = fig.canvas.mpl_connect('button_press_event', onclick)
    pyplot.savefig(folder_selected+"Figure_1.png")
    pyplot.show()

    # pyplot.show()
    # SHG_Plot = cv2.cvtColor(SHG_Raw, cv2.COLOR_BGR2GRAY)
    # pyplot.imshow(SHG_Plot)
    # pyplot.show()
    # edges = cv2.Canny(SHG_Plot, threshold1=30, threshold2=100)
    # pyplot.imshow(edges)
    #     test_max = np.max(region_test)
    #     test_postion_max = np.where(region_test == test_max)
    #     test_max_x = test_postion_max[0].astype(int)
    #     test_max_y = test_postion_max[1].astype(int)
    #     # pyplot.scatter(test_max_x, test_max_y, s=60, color='tomato', marker='x')

    #     avg_x = avg_x + test_max_x
    #     avg_y = avg_y + test_max_y
    #     iteration += 1
    #     large_sum_test = sum(map(sum, SHG_Raw))
    #     deg_file_org = np.append(deg_file_org, degree)
    #     sig_file_org = np.append(sig_file_org, large_sum_test)
    #
    #
    # # Testing
    # postion_max_x = (avg_x / iteration).astype(int)
    # postion_max_y = (avg_y / iteration).astype(int)
    # SHG_Raw = np.loadtxt(folder + file_name + "_{}deg".format(degree) + ".txt", dtype=int, delimiter=',')
    #
    #
    # region = SHG_Raw[240:260, 235:255]
    # pyplot.imshow(region)
    # test_max = np.max(region)
    # test_postion_max = np.where(region == test_max)
    # test_max_x = int(test_postion_max[0])
    # test_max_y = int(test_postion_max[1])
    # pyplot.scatter(postion_max_x, postion_max_y, s=60, color='tomato', marker='x')
    # pyplot.show()

    # degree = 0
    # while data_sel == 'n':
    #     SHG_Raw = np.loadtxt(folder + file_name + "_{}deg".format(degree) + ".txt", dtype=int, delimiter=',')
    #     fig, ax = pyplot.subplots()
    #     ax.imshow(SHG_Raw)
    #     vmax = np.max(SHG_Raw)
    #     postion_max = np.where(SHG_Raw == vmax)
    #     max_x = int(postion_max[0])
    #     max_y = int(postion_max[1])
    #     region = SHG_Raw[max_x - 20: max_x + 20, max_y - 20: max_y + 20]
    #     ax.imshow(region)
    #     pyplot.show()
    #     data_sel = input('Are you satisfied with the data selection? (Y/N) ').lower()
    #     while data_sel not in ['y', 'n']:
    #         print("Invalid Entry. Please enter again!")
    #         data_sel = input('Are you satisfied with the data selection? (Y/N) ').lower()
    #     degree = degree + 5



    deg_file = []
    sig_file = []
    center_x = int(cur_x)
    center_y = int(cur_y)
    # center_x = 238
    # center_y = 258
    # center_x = int(input('Enter the center for x axis: '))
    # center_y = int(input('Enter the center for y axis: '))
    region_size = int(input('Enter the box size: '))
    # region_size = 80
    half_region_size = (np.ceil(region_size / 2)).astype(int)
    # min_pos = (postion_max_x + 235 - half_region_size)[0]
    # max_pos = (postion_max_x + 235 + half_region_size)[0]

    SHG_Raw = np.loadtxt(folder_selected + file_name + "_{}deg".format(0) + ".txt", dtype=int, delimiter=',')
    fig, ax = pyplot.subplots()
        # ax.imshow(SHG_Raw)
    region = SHG_Raw[center_x - half_region_size: center_x + half_region_size,
                         center_y - half_region_size: center_y + half_region_size]
    im = ax.imshow(SHG_Raw, vmin=1000, vmax=5000)

    fig.colorbar(im, ax=ax, label='Interactive colorbar')
    ax.scatter(center_x, center_y, s=30, color='tomato', marker='x')
    rect = patches.Rectangle((center_x - half_region_size, center_y - half_region_size),
                                 region_size, region_size, linewidth=1, edgecolor='r', facecolor='none')
        # Add the patch to the Axes
    ax.add_patch(rect)
    pyplot.show()
    for degree in range(0, 365, step_size):
        deg_file = np.append(deg_file, degree)
        SHG_Raw = np.loadtxt(folder_selected + file_name + "_{}deg".format(degree) + ".txt", dtype=int, delimiter=',')
        # fig, ax = pyplot.subplots()
        # ax.imshow(SHG_Raw)
        region = SHG_Raw[center_x - half_region_size: center_x + half_region_size,
                         center_y - half_region_size: center_y + half_region_size]
        # ax.imshow(SHG_Raw)
        # ax.scatter(center_x, center_y, s=60, color='tomato', marker='x')
        # rect = patches.Rectangle((center_x - half_region_size, center_y - half_region_size),
        #                          region_size, region_size, linewidth=1, edgecolor='r', facecolor='none')
        # # Add the patch to the Axes
        # ax.add_patch(rect)
        # pyplot.show()
        small_sum = sum(map(sum, region))
        large_sum = sum(map(sum, SHG_Raw))
        bkg_pixel = (large_sum - small_sum) / (512 ** 2 - region_size ** 2)
        sig = small_sum - bkg_pixel * region_size ** 2
        sig_file = np.append(sig_file, sig)

    sig_file = sig_file.astype(np.float64)
    # sig_file = sig_file.tolist()
    max_lim = max(sig_file)
    min_lim = min(sig_file)
    deg_file = deg_file * np.pi / 180
    deg_file = deg_file.astype(np.float64)
    # deg_file = deg_file.tolist()
    fig, ax = pyplot.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(deg_file, sig_file, color='red')
    ax.set_ylim(bottom=min_lim, top=max_lim)
    # pyplot.autoscale()
    pyplot.show()
    pyplot.plot(deg_file, sig_file, linewidth=5, color='blue')
    pyplot.show()
    print(deg_file)
    print(sig_file)

    slope = (sig_file[-1] - sig_file[0]) / (deg_file[-1] - deg_file[0])
    const = sig_file[-1] - slope * deg_file[-1]
    # const = sig_file[-1] + slope * deg_file[-1]
    for i in range(len(sig_file)):
        sig_file[i] = sig_file[i] - (slope * deg_file[i] + const)
        sig_file[i] = (sig_file[i]/30)/380000

    pyplot.plot(deg_file, sig_file, linewidth=5, color='blue')
    pyplot.show()

    max_lim = max(sig_file)
    min_lim = min(sig_file)

    print(deg_file)
    print(sig_file)

    fig, ax = pyplot.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(deg_file, sig_file, color='red')
    ax.set_ylim(bottom=min_lim, top=max_lim)
    pyplot.title(title + '{} Polarization'.format(polarization), pad=10, wrap=True)
    pyplot.tight_layout()
    pyplot.savefig(folder_selected+"Figure_2.png")
    pyplot.show()
    # para, cm = optimize.curve_fit(shg_sin, deg_file[0:], sig_file[0:], method='lm', maxfev=50000)
    # y_fit = np.array(
    #     [shg_sin(x) for x in deg_file])
    # returndata = {'Flod': 0}
    #
    # for i, name in enumerate(['Fold: ']):
    #     returndata[name] = para[i]
    #     print(name, returndata[name])
    #
    # error = np.sqrt(np.diag(cm))
    # residuals = sig_file - shg_sin(deg_file)
    # ss_res = np.sum(residuals ** 2)
    # ss_tot = np.sum((sig_file - np.mean(sig_file)) ** 2)
    # r_square = 1 - (ss_res / ss_tot)
    # print(f'\nThe fitting accuracy is {np.ceil(r_square * 10000) / 100} %')
    # pyplot.rc('font', size=42)
    # pyplot.rc('axes', labelsize=42)  # fontsize of the x and y labels
    # pyplot.rc('xtick', labelsize=42)  # fontsize of the tick labels
    # pyplot.rc('ytick', labelsize=42)  # fontsize of the tick labels
    # pyplot.rc('legend', fontsize=42)  # legend fontsize
    # pyplot.figure(figsize=(32, 18), dpi=100)
    # pyplot.plot(deg_file, y_fit, color='red', label='Fitting Data', linewidth=6.0)
    #
    # pyplot.xlabel("\u03C4 (ps)", fontname="Arial", labelpad=15)
    # pyplot.ylabel('\u0394R/R', fontname="Arial", labelpad=15)
    # pyplot.legend(loc='upper right', frameon=False, labelspacing=0.3)
    # pyplot.tight_layout()
    # pyplot.show()
    # pyplot.polar(deg_file, y_fit)
    # pyplot.show()


if __name__ == '__main__':
    # construct the main wi
    window1 = SHG_Processing()
    # endless loop unless quit