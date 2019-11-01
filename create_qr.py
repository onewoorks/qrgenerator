import qrcode
from PIL import Image

logo = Image.open('medivest_logo.jpg')

qr_big = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
)

qr_big.add_data('0100998000000000000SBN17725-01000998')
qr_big.make()

img_qr_big = qr_big.make_image().convert('RGB')

pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1])//2)

img_qr_big.paste(logo,pos)
img_qr_big.save('2_trust_qr_with_logo.png')
# img = qrcode.make('eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjEyMzE1NSIsImFjdCI6W3sibmFtZSI6ImJhdGVyeSBjaGVjayJ9XX0.U6tCwOcOkPr73nmdnfUc4RgOgHQgOooqOmpnYheiYK0')

# print(type(img))
# print(img.size)

# img.save('test_.png')