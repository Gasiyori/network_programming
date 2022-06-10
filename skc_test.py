from cryptography.fernet import Fernet

key = Fernet.generate_key() #128bit key 생성
print(key)

cipher_suite = Fernet(key)

# 암호화
cipher_text = cipher_suite.encrypt(b'Internet of Things')

# 복호화
plain_text = cipher_suite.decrypt(cipher_text)

# 암호화된 문자열
print('Encrypted Text:', cipher_text)

# 복호화된 문자열
print('Decrypted Text:', plain_text)