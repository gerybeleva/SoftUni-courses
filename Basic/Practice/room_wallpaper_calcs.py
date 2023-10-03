import math
from math import ceil, floor
print("Application for calculation of wallpaper roler quantity needed for a single room.")

wallpaper_widght = float(input(f'Please specify the wallpaper roller widght (m): '))
wallpaper_lenght = float(input(f'Please specify the wallpaper roller lenght (m): '))
wallpaper_fitting_distance = float(input(f'Please specify the wallpaper fitting size (m): '))

if wallpaper_fitting_distance > 0:
    wallpaper_lenght = wallpaper_lenght - wallpaper_fitting_distance

windows_qty = float(input(f'Please specify total numbers of windows: '))
doors_qty = float(input(f'Please specify total numbers of doors: '))

room_lenght = float(input(f'Please specify the room lenght (m): '))
room_widght = float(input(f'Please specify the room wight (m): '))
room_height = float(input(f'Please specify the room height (m): '))

window1_w = 0
window1_h = 0
window2_w = 0
window2_h = 0
window3_w = 0
window3_h = 0
S_window1 = 0
S_window2 = 0
S_window3 = 0

door1_w = 0
door1_h = 0
door2_w = 0
door2_h = 0
S_door1 = 0
S_door2 = 0

S_walls = 0
S_wallpapers = 0
Wallpapers_rollers_qty = 0

if windows_qty == 1 and doors_qty == 1:
    window1_w = float(input(f'PLease enter 1st window W (m): '))
    window1_h = float(input(f'PLease enter 1st window H (m): '))
    door1_w = float(input(f'PLease enter the door W (m): '))
    door1_h = float(input(f'PLease enter the door H (m): '))
    S_window1 = window1_w * window1_h
    S_door1 = door1_w * door1_h
    S_walls = room_lenght * room_height * 2 + room_widght * room_height * 2
    S_wallpapers = (S_walls - S_window1 - S_door1)
    Wallpapers_rollers_qty = math.ceil(S_wallpapers / (wallpaper_widght * wallpaper_lenght))

elif windows_qty == 2 and doors_qty == 1:
    window1_w = float(input(f'PLease enter 1st window W (m): '))
    window1_h = float(input(f'PLease enter 1st window H (m): '))
    window2_w = float(input(f'PLease enter 2nd window W (m): '))
    window2_h = float(input(f'PLease enter 2nd window H (m): '))
    door1_w = float(input(f'PLease enter the door W (m): '))
    door1_h = float(input(f'PLease enter the door H (m): '))
    S_window1 = window1_w * window1_h
    S_window2 = window2_w * window2_h
    S_door1 = door1_w * door1_h
    S_walls = room_lenght * room_height * 2 + room_widght * room_height * 2
    S_wallpapers = (S_walls - S_window1 - S_window2 - S_door1)
    Wallpapers_rollers_qty = math.ceil(S_wallpapers / (wallpaper_widght * wallpaper_lenght))


print(f"The required quantity of Wallpaper rollers is: {Wallpapers_rollers_qty} pcs.")