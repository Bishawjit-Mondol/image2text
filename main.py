import pytesseract
import PIL.Image
import cv2

myconfig = r'--psm 6 --oem 3'

text = pytesseract.image_to_string(PIL.Image.open('test-1.png'), config=myconfig)
print(text)
