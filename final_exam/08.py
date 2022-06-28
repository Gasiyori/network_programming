# 카카오 API를 사용한 썸네일 부분
# 상품 검출 강의 자료의 내용을 토대로 만들었음.

import requests
from PIL import Image, ImageDraw
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/thumbnail/crop'
REST_API_KEY = 'Your REST API KEY'

def thumb_product(image_url): # app_key와 이미지 파일의 URL을 POST로 전송하여 섬네일 생성
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'image_url' : image_url, 'width' : 200, 'height' : 200}
    resp = requests.post(API_URL, headers=headers, data=data)
    return resp.json() # 검출 결과를 딕셔너리로 변환하여 반환

def show_thumb(image_url, detection_result):
    image_rsp = requests.get(image_url) # URL 이미지 다운로드
    file_jpgdata = BytesIO(image_rsp.content)
    image = Image.open(file_jpgdata)
    return image

if __name__ == "__main__":
    IMAGE_URL = 'https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/07.jpg'
    thumb_result = thumb_product(IMAGE_URL)

    image = show_thumb(IMAGE_URL, thumb_result) 
    image.show()