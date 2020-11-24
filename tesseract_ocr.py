# """
# Tesseract - OCR 프로그램 중 하나, 다양한 운영체제에서 사용 가능한 엔진, 오픈 소스!

# 1.이미지 -> 텍스트 추출 과정
# 2. pytesseract에서 Tesseract 사용하기

# """
from PIL import Image
import pytesseract

# pytesseract에서 실행 파일이 어디 있는지 지정해 주어야함 .
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# image_to_string 메서드를 이용하여 실제 이미지를 변환하는 작업을 함.
text = pytesseract.image_to_string(Image.open('news2.png'), lang='kor')
# 
# print(text)
# replace 메서드를 이용해 변환중 생기는 공백을 없애도록함.
print(text.replace(' ',''))

with open('news2.txt', 'w', encoding='utf-8') as f:
    f.write(text)
    f.write('\n\n\n')
    f.write(text.replace(' ', ''))
    