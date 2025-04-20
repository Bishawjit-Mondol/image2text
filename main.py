import pytesseract
import PIL.Image
import cv2

myconfig = r'--psm 6 --oem 3'

# text = pytesseract.image_to_string(PIL.Image.open('test-4.jpg'), config=myconfig)
# print(text)


img = cv2.imread('test-4.jpg')
height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
for box in boxes.splitlines():
    box = box.split(' ')
    # print(b)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, height - y), (w, height - h), (0, 255, 0), 2)
    cv2.putText(img, box[0], (x, height - y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

cv2.imshow('img', img)
cv2.waitKey(0)