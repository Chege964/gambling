from pynput import *
def get_coords(x, y):
    print("Your  X & Y are: {} ".format((x,y)))

with mouse.Listener(on_move = get_coords) as listen:
    listen.join()