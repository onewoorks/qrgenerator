import qrcode
from PIL import Image

logo = Image.open('medivest_logo.jpg')

qr_big = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
)

qr_big.add_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJob3NwaXRhbCI6IlR1YW5rdSBKYWFmYXIsIE5lZ2VyaSBTZW1iaWxhbiIsImxvY2F0aW9uX2NvZGUiOiJXUFAiLCJsb2NhdGlvbl9uYW1lIjoiV2FkIFBlcmVtcHVhbiBQc2lraWF0cmkifQ.thsu0W3nQvQC5wrIiFaGJUXSTEyghx0tXEXR6I_1Y7k')
qr_big.make()

img_qr_big = qr_big.make_image().convert('RGB')

pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1])//2)

img_qr_big.paste(logo,pos)
img_qr_big.save('location_qr.png')