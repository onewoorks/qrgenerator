from PIL import Image, ImageDraw, ImageFont
import os

# qr_code = Image.open("./qr_with_logo.png")
 
img = Image.new('RGB', (400, 410), color = (255, 255, 255))
 
fnt = ImageFont.truetype('Scada-Regular.ttf', 25)
d = ImageDraw.Draw(img)
# d.text((10,10), "Hello world", font=fnt, fill=(255, 255, 0))
d.text((10,60), "Line 1 : AAAAAA".upper(), fill=(0, 0, 0), font=fnt)
d.text((10,90), "Line 2 : BBBBBB".upper(), fill=(0, 0, 0), font=fnt)
d.text((10,120), "Line 2 : CCCCCC".upper(), fill=(0, 0, 0), font=fnt)
d.text((10,150), "Line 1 : AAAAAA".upper(), fill=(0, 0, 0), font=fnt)
d.text((10,180), "Line 2 : BBBBBB".upper(), fill=(0, 0, 0), font=fnt)
d.text((10,210), "Line 2 : CCCCCC".upper(), fill=(0, 0, 0), font=fnt)

img.save('pil_text_font.png')
os.system('pil_text_font.png')
