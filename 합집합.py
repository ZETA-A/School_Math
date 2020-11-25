a = [1,2,3]
b = [4,5,6]
c = a + b
c = []                  # 먼저 합집합을 공집합으로 만들고
for i in a:             # a에 속한 모든 요소 i에 대하여 순서대로 실행시킨다
    if i not in b:      # 만약 i가 b에 속하지 않는다면
        c.append(i)     # 합집합 c에 i를 추가한다
c = c + b
c.sort()
print (c)
