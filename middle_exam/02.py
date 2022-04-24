lst = ['H', 'e', 'l', 'l', 'o', ' ', 'I', 'a', 'T']

lst[7] = 'o'
print(lst) # o 가뿌기

lst.append('?')
print(lst) # '?' 추가

print(len(lst)) # 길이

print("".join(lst)) # 하나로

lst.sort(reverse=True)
print(lst)