try:
    import Image
except ImportError:
    from PIL import Image 

import pytesseract
# print(pytesseract.image_to_string(Image.open('2.png'), lang='chi_sim'))
ps = pytesseract.image_to_string(Image.open('1.jpg'), config='-psm 8 digits_old', lang='eng')
print(ps)
ps1 = pytesseract.image_to_string(Image.open('3.jpg'), config='-psm 8 digits_old', lang='eng')
print(ps1)