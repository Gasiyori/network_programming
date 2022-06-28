# 문제 기억 안남
# url을 parse하고, 다시 합쳐서 리퀘스트 받아서 출력하는 듯?

from urllib import parse
import requests

url = 'https://search.naver.com/search.naver?query=iot'

parsed_url = parse.urlparse(url)
print(parsed_url)

unparsed_url = parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path
print(unparsed_url)

rsp = requests.get(unparsed_url)
print(rsp.headers) # 응답 헤더