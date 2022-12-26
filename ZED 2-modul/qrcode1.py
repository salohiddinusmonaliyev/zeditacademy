# What it does?
# - Creates QR CODE with Image in the center / Branding your QR CODE
# - Creates QR CODE with respective color automatically

# Required - pip install qrcode
# All types of images format works eg. jpg, png, bmp, gif, etc.

import qrcode
from PIL import Image
import os

# for ignoring warnings
import warnings

warnings.filterwarnings("ignore")

####################################
# Enter your text or url
YOUR_TEXT_OR_URL = 'hello world'
####################################
# set size of the logo
logosize = 75
####################################
####################################
# set path to your file
# infile = 'youtube.png'
####################################
####################################
# set path to your file from batch file
import sys

infile = sys.argv[-1]


####################################
####################################

# convert RGB to HEX function
def rgb_to_hex(rgb):
    return '#' + '%02x%02x%02x' % rgb


# get filename
filename = infile.split('.')[0]
# read image
logo = Image.open(infile)
# convert to RGB mode
logo_rgb = logo.convert("RGB")
# getting the RGB color from 10x10 pixel
rgb = logo_rgb.getpixel((10, 10))
# set size of the logo
basewidth = logosize
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.add_data(YOUR_TEXT_OR_URL)
qr_big.make()

# Using the same color of the image automatically
# OR type color code as 'black'  or #0b4e39
colorcode = rgb_to_hex(rgb)
img_qr_big = qr_big.make_image(fill_color=colorcode, back_color="white").convert('RGB')
pos = (
    (img_qr_big.size[0] - logo.size[0]) // 2,
    (img_qr_big.size[1] - logo.size[1]) // 2
)
img_qr_big.paste(logo, pos)

# Create final_QR directory
try:
    os.mkdir("final_QR")
except:
    print("folder exists")

# save as filenameQR.png format
img_qr_big.save("final_QR/" + filename + 'QR' + '.png')