import pyautogui, sys, time

def select_program():
    pyautogui.moveTo(286, 182)
    time.sleep(1)
    pyautogui.click(x=286, y=182)
    time.sleep(1)

def region_cal():

    pyautogui.click(x=286, y=182)
    time.sleep(1)

    pyautogui.moveTo(360, 321)
    time.sleep(1)
    pyautogui.click(x=360, y=321)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def copy_text():
    log_win_x = 1098
    log_win_y =898
    pyautogui.moveTo(log_win_x, log_win_y)
    pyautogui.click(x = log_win_x, y = 898)
    pyautogui.click(x=log_win_x, y=898)
    pyautogui.click(x=log_win_x, y=898)
    # pyautogui.drag(100, 0, 2, button='left')
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    copy_to_plot_x = 750
    copy_to_plot_y = 771
    pyautogui.moveTo(copy_to_plot_x, copy_to_plot_y)
    pyautogui.click(x=copy_to_plot_x, y=copy_to_plot_y)
    pyautogui.click(x=copy_to_plot_x, y=copy_to_plot_y)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.click(x=872, y=500)
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.press('j')
    pyautogui.keyUp('ctrl')


def copy_ppt():
    pyautogui.moveTo(1070, 1021)
    time.sleep(1)
    # pyautogui.click(x=1070, y=1021)
    # time.sleep(1)
    pyautogui.moveTo(899, 923)
    time.sleep(1)
    pyautogui.click(x=899, y=923)
    time.sleep(1)
    pyautogui.moveTo(118, 225)
    time.sleep(1)
    pyautogui.click(x=118, y=225)
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    time.sleep(1)


def back_to_org():
    # pyautogui.keyUp('ctrl')
    pyautogui.moveTo(884, 1021)
    time.sleep(1)
    pyautogui.click(x=884, y=1021)
    time.sleep(1)
    # pyautogui.click(x=884, y=1021)
    # time.sleep(1)
    del_graph_x =702
    del_graph_y = 579
    pyautogui.moveTo(del_graph_x, del_graph_y)
    time.sleep(1)
    pyautogui.click(x=del_graph_x, y=del_graph_y)
    time.sleep(1)
    pyautogui.press('delete')
    time.sleep(1)

def start_new(x):
    pyautogui.moveTo(1430, x)
    time.sleep(1)
    pyautogui.click(x=1430, y=x)
    time.sleep(1)
    pyautogui.moveTo(1430, x+15)
    time.sleep(1)
    pyautogui.click(x=1430, y=x+15)
    time.sleep(1)
    pyautogui.click(x=1480, y=x + 15)
    time.sleep(1)

# x,y=pyautogui.position()
# print(x,y)
# pyautogui.moveTo(972, 874)'
#
select_program()
x=286
for i in range(0,19,1):

    region_cal()
    copy_text()
    copy_ppt()
    back_to_org()
    start_new(x+i*15)
