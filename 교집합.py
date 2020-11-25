a = [1,2,3]
b = [3,4,5]

c = []                  # 먼저 교집합을 공집합으로 만들고
for i in a:             # a에 속한 모든 요소 i에 대하여 순서대로 실행한다
    if i in b:          # 만약 i가 b에 속한다면
        c.append(i)     # 교집합 c에 추가시킨다
print (c)
