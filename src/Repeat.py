#while문은 익숙하니 넘어가고
#for문은 for 변수 in 리스트
#           실행할 소스코드

i = 1
result = 0
while(result< 55):
    result += i
    i+=1
print(result)

result = 0
for i in range(1,11):
    result += i
print(result)

#range()의 값을 하나의 값만을 넣으면 자동으로 시작값은 0이다. 주로 리스트 유플의 데이터의 모든 원소를 첫번쨰부터 방문해야할 때 이방법을 사용한다.

result = 0
for i in range(11):
    result += i
    i+=1
print(result)

#반복문안에서 continue를 만나면 프로그램의 흐름은 처음으로 돌아간다.

score = [90,100,40,77,80]
ban = {1,4}
for i in range(5):
    if i+1 in ban:
        continue
    if score[i] >60 : print(i+1,'번째 학생은 합격입니다')