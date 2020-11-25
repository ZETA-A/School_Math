a = [1,2,3]
b = [3,4,5]

c = a + []              # c는 a와 똑같은 list가 되게 복사한다
for i in b:             # b원소가
    if i in a:          # 만약 i원소안에 a가 속해있다면
        c.remove(i)     # c에서 i를 지운다
print (c)
