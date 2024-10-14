import cv2
import pytesseract
import re


image = cv2.imread('target_reciept.jpg')
# grayscale it
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# improve accuracy by thresholding
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# perform the OCR

grocery_raw_text = pytesseract.image_to_string(gray)
lines = grocery_raw_text.split("\n")
filtered_lines = [line for line in lines if '$' in line and re.search(r'\b\d{9}\b', line)]

print(filtered_lines)