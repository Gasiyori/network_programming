# from datetime import datetime

# days = ['Mon', 'The', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# print(datetime.now().month)

# datetime.now().strftime

# -----

# import time

# print(time.strftime('%c', time.localtime(time.time())))

# -----

# command, mboxID, *message = input().split() # 명령(send, receive), mboxID, message로 구분. message에 문자열 패킹

# message = " ".join(message)

# print(message)

#-----

# mbox_index = {} # mboxID 목록 딕셔너리 생성

# while (1):
#     msg = input()

#     if msg == 'q':
#         break

#     command, mboxID, *message = msg.split() # 명령(send, receive), mboxID, message로 구분. message에 문자열 패킹
#     message = " ".join(message) # 패킹된 문자열 합쳐서 문자열로 만듬

#     if mboxID not in mbox_index: # mboxID 목록에 딕셔너리 key가 존재하지 않으면
#         mbox_index[mboxID] = [] # 리스트를 키값으로 갖는 딕셔너리 생성
#     # 존재하면? >> 그냥 바로 아래처럼 키 값에 추가.
#     # 위에서 리스트로 생성했으니 append가 동작.
    
#     mbox_index[mboxID].append(message)
    
#     print(mbox_index) #디버깅용

# print(mbox_index[mboxID].pop(0)) # 가장 앞의 문자 끄집어냄
# print(mbox_index)

# print("---")

# print(not bool(mbox_index[mboxID])) # bool은 비어있으면 False 반환
# #not bool은 True 반환
# print(mbox_index)

# print("---")

#-----

