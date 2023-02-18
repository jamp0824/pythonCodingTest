#조건문
#if ~ elif ~else
#들여쓰기는 탭보다 스페이스바 4번을 추천한다

if(1<2):
    print("2가 1보다 크다")

#논리 연산자
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)
print(not False)

#기타 연산자
a = [1,2,3,4,5]
b = 3
print(b in a)
print(8 not in a)

#조건문이 True라고 해도 아무것도 처리하고 싶지 않을 때

score = 86

if score < 90:
    pass
else:
    print('123123123')
print('im here')

if score>90 : print('im above 90')
else: print("iam batman")

#conditional expression
result = "Success" if score<90 else "False"
print(result)

a = [1,2,3,4,5,5,5]
remove_set = [3,5]

result = []
result = [i for i in a if i not in remove_set]
print(result)

#다른 언어와 달리 파이썬은 조건문안에서 수항 부동식을 그대로 사용할 수 있따.
x = 15
if x > 10 and x < 20:
    print(True)

y = 20
if 15<y<21:
    print(True)

#다만 15<x<20 과정에서 의도치 않은 결과를 반환할 수 있으니 유의하자