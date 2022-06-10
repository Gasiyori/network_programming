import zipfile
# sample.xlsx와 index.html 파일을 sample.zip으로 압축

zf = zipfile.ZipFile('sample.zip', 'w')
zf.write('sample.xlsx')
zf.write('index.html')
zf.close()

# sample.zip 파일을 D:\Desktop\network_programming 아래에 압축풀기
uzf = zipfile.ZipFile('sample.zip', 'r')
uzf.extractall(path='D:\Desktop\network_programming')