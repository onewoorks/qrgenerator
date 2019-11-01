from PIL import Image,  ImageDraw
import os


im1 = Image.open('qr_with_logo.png')
im2 = Image.open('pil_text_font.png')

dst = Image.new('RGB', (im1.width + im2.width + 2, im1.height + 4), color=(0,0,0))
dst.paste(im1, (2, 2))
dst.paste(im2, (im1.width, 2))

dst.save('full_.png')
os.system('full_.png')