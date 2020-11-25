a = [1,2,3,1]

new_a = []                          # 공집합을 만들어 new_a로 저장하고
for i in a:                         # a의 원소에 대하여
    for i in a:                     # 만약 i가 new_a에 없으면
        if i not in new_a:          # new_a에 i를 추가합니다
            new_a.append(i)
print (new_a)
