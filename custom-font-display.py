import lcd
import image
import time

lcd.init(type = 2, freq=15000000, width=240, height=240, color=(0, 0, 0))
lcd.rotation(1)
lcd.clear(lcd.BLACK)

canvas = image.Image(size=(240, 240))

from cocorobo import display_font

# Uncomment below to use font from SD card.
# font_path = "/sd/user/Dinkie9px-16pt_24w-24h-hoff-1voff+7.Dzk"

# Load font from flash.
# font_path = 0x200000      # Dinkie9px
# font_path = 0x850000      # Dinkie7px
font_path = 0xA50000        # Dinkie9px
noncjk_ratio = 0.9
cjk_ratio = 16

def display_custom_font(canvas, x, y, text, color = (255, 255, 255), font_size = 1):
    display_font(canvas, x, y, text, color = color, font_size = font_size, load_path = font_path, cjk_ratio = cjk_ratio, noncjk_ratio = noncjk_ratio, font_wh = 16)

def test_size_1():
    font_size = 1

    display_custom_font(canvas, 0, 0, "abcdefghijklmnopqrstuvwxyza", color = (255, 255, 255), font_size = font_size)
    display_custom_font(canvas, 0, 20, "abcdefghijklmnopqrstuvwxyza".upper()[0:13], color = (255, 255, 255), font_size = font_size)
    display_custom_font(canvas, 0, 40, "abcdefghijklmnopqrstuvwxyza".upper()[10:27], color = (255, 255, 255), font_size = font_size)
    display_custom_font(canvas, 0, 100, "0123456789", color = (255, 255, 255), font_size = font_size)

    display_custom_font(canvas, 0, 200, "越过长城，走向世界", color = (255, 255, 255), font_size = font_size)
    display_custom_font(canvas, 0, 220, "1987 年 9 月 20 日", color = (255, 255, 255), font_size = font_size)

def test_size_2():
    font_size = 2

    display_custom_font(canvas, 0, 0, "abcdefghijklmn", color = (255, 255, 255), font_size = font_size)
    display_custom_font(canvas, 0, 30, "opqrstuvwxyza", color = (255, 255, 255), font_size = font_size)

    display_custom_font(canvas, 0, 60, "abcdefghijklm".upper(), color = (255, 255, 255), font_size = font_size)
    display_custom_font(canvas, 0, 90, "pqrstuvwxyza".upper(), color = (255, 255, 255), font_size = font_size)
    display_custom_font(canvas, 0, 210, "0123456789", color = (255, 255, 255), font_size = font_size)

font_size = 5

# test_size_1()
# test_size_2()

'''
canvas.draw_rectangle(0, 0, 240, 240, color = (255, 0, 0), fill = True)
display_font(canvas, 45, 30, "喜氣", color = (255, 255, 255), font_size = font_size, load_path = font_path, cjk_ratio = cjk_ratio, noncjk_ratio = noncjk_ratio, font_wh = 16)
display_font(canvas, 45, 120, "洋洋", color = (255, 255, 255), font_size = font_size, load_path = font_path, cjk_ratio = cjk_ratio, noncjk_ratio = noncjk_ratio, font_wh = 16)
'''

display_custom_font(canvas, 0, 0, "MaixPy on K210 (2021-08-04)", color = (125, 125, 125), font_size = 1)
display_custom_font(canvas, 0, 20, "Type \"help()\" for more info.", color = (125, 125, 125), font_size = 1)
display_custom_font(canvas, 0, 40, ">>> print('Hello CocoRobo!')", color = (255, 255, 255), font_size = 1)
display_custom_font(canvas, 0, 60, "'Hello CocoRobo!'", color = (0, 255, 0), font_size = 1)
display_custom_font(canvas, 0, 80, ">>> 1+1 == 0", color = (255, 255, 255), font_size = 1)
display_custom_font(canvas, 0, 100, "False", color = (255, 0, 0), font_size = 1)
display_custom_font(canvas, 0, 120, ">>> os.listdir('/sd/preset/songs')", color = (255, 255, 255), font_size = 1)
display_custom_font(canvas, 0, 140, str(os.listdir('/sd/preset/songs')[2:4]), color = (0, 255, 0), font_size = 1)

lcd.display(canvas, oft=(0, 0))


