# import pytesseract
# from PIL import Image
# import cv2
#
# myconfig = r'--psm 6 --oem 3'
# text = pytesseract.image_to_string(Image.open('test-4.jpg'), lang='ben', config=myconfig)
# print(text)




# import pytesseract
# from PIL import Image
# import cv2
# myconfig = r'--psm 6 --oem 3'
# img = cv2.imread('test-4.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
# # Save temporarily if needed
# cv2.imwrite('processed.png', thresh)
#
# text = pytesseract.image_to_string(thresh, lang='ben', config=myconfig)
# print(text)





# import pytesseract
# from PIL import Image
# import cv2
# import numpy as np
#
# # Load image
# image_path = 'test-4.jpg'  # Change to your image name
# image = cv2.imread(image_path)
#
# # Step 1: Convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Step 2: Apply Otsu's thresholding
# _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
# # Step 3: (Optional) Denoise
# thresh = cv2.medianBlur(thresh, 3)
#
# # Step 4: Use pytesseract with Bangla language
# custom_config = r'--oem 3 --psm 6'
# text = pytesseract.image_to_string(thresh, lang='ben', config=custom_config)
# text = text.encode('utf-8').decode('utf-8')
#
# print(text)




import cv2
import pytesseract
from PIL import Image
import numpy as np

def basic_ocr(image_path, lang='eng'):
    try:
        # Try direct OCR first
        text = pytesseract.image_to_string(Image.open(image_path), lang=lang)
        if len(text.strip()) > 10:  # Arbitrary threshold
            return text
    except Exception as e:
        print("Basic OCR failed, fallback to OpenCV:", e)

    # Fallback to OpenCV preprocessing if text is too short
    return advanced_ocr(image_path, lang)

def advanced_ocr(image_path, lang='eng'):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]

    if h < 800 or w < 800:
        img = cv2.resize(img, (w*2, h*2), interpolation=cv2.INTER_LINEAR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    config = '--psm 6 --oem 3'
    text = pytesseract.image_to_string(thresh, lang=lang, config=config)
    return text

if __name__ == '__main__':
    image_path = 'test-4.jpg'  # or bangla-image.jpg
    lang = 'eng+ben'  # or 'ben' or 'eng+ben'
    result = basic_ocr(image_path, lang)
    print(result)
