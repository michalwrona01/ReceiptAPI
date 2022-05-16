import cv2
import numpy as np
import pytesseract


def get_image_handler_to_img_cv2(file):
    contents = file.file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    return img


def correct_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1))
    img = cv2.erode(img, kernel, iterations=100)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    img = cv2.medianBlur(img, 3)

    return img


def ocr_receipt(file):
    img = get_image_handler_to_img_cv2(file)
    img_corrected = correct_image(img)

    return pytesseract.image_to_string(img_corrected, lang='pol')
