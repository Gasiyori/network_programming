from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc") # 데이터를 덧붙여서 추가
digest.update(b"123")
hash = digest.finalize() # 해쉬값 계산
print(hash) # 해쉬로 변환된문자열 출력

digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc123") # 위의 예제 한번에 입력
hash = digest.finalize()
print(hash)

digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc124") # 다른 값이 나옴 
hash = digest.finalize()
print(hash)