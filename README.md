![Pytesseract](https://i.ytimg.com/vi/4DrCIVS5U3Y/maxresdefault.jpg)

### png, 이미지 파일
<img src='news2.png' with='400' height='400'/>

### 추출된 텍스트(txt파일)
<img src='추출된 텍스트.png' with='400' height='400'/>

---
# 소개

>OCR = 광학 문자 인식. 즉, OCR 시스템은 기계 인쇄 또는 수기 텍스트를 포함 할 수있는 2 차원 텍스트 이미지를 이미지 표현에서 기계 판독 가능 텍스트로 변환합니다. 프로세스로서의 OCR은 일반적으로 가능한 한 정확하게 수행하기 위해 여러 하위 프로세스로 구성됩니다. 하위 프로세스는 다음과 같습니다.


- 이미지 전처리
- 텍스트 현지화
- 캐릭터 분할
- 문자 인식
- 후 처리
---
![OCR Process](https://nanonets.com/blog/content/images/2019/11/OCR.jpg)
물론 위 목록의 하위 프로세스는 다를 수 있지만 이는 자동 문자 인식에 접근하는 데 필요한 대략적인 단계입니다. OCR 소프트웨어에서는 작성된 텍스트 문자와 다른 언어를 사용하여 모든 고유 단어를 식별하고 캡처하는 것이 주요 목표입니다.

> 결국 OCR을 하기 위해서 사용하는 것 중 하나로 Tesseract가 있다.
테서렉트는 다양한 운영체제에서 사용할 수 있는 광학 문자 인식 엔진이다. 아파치 라이선스 2.0에 따르는 무료 소프트웨어이며 2006년 부터 구글이 개발을 후원하고 있다고 위키피디아에 나와 있다.
테서렉트 OCR을 이용하는 주된 이유는 이미지에서 글자를 추출하고자 함이다. CLI를 이용하여도 가능합니다.

### Tesseract 인스톨러 및 pytesseract 라이브러리 설치

- `https://github.com/ub-mannheim/tesseract/wiki` <--주소로 가서 설치해 주세요. 참고로 윈도우에요.
  
###### window버전 설치
<img src='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbxUS7B%2FbtqzMev8ZbJ%2FHCy80KYZh1JCHYJPW4K3I0%2Fimg.png' with='300' height='300'/>

```
$ pip install pytesseract Pillow

#두 가지 라이브러리를 다운 받을게요.
```
---
###### 추가 언어 선택란(Additional Language data) 체크하고 한국어를 선택하세요.
<img src='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc1VhMg%2FbtqzI5nx1yk%2Fjo15sE32C2cVNI57yB0u31%2Fimg.png
' with='300' height='300'/>

##### 

아래 링크를 타고 2개 파일을 추가로 다운받을게요.
https://github.com/tesseract-ocr/tessdata

제목에서 물씬 풍겨 나오듯이 한국어에 대한 자료를 더 추출할 수 있는 추가 파일이라고 보시면 되요.
- kor.traineddata
- kor_vert.traineddata
- 다운 받은 파일 2개를 `C:\Program Files\Tesseract-OCR\tessdata`에 붙여 넣어주세요. 중복 메시지가 나와도 무시하고 진행 해주세요.

##### 소스코드
```
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
```