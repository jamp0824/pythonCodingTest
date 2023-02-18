#동일한 알고리즘을 반복적으로 수행해야 할 때 함수는 중요하게 사용된다.
#함수를 작성할 때는 함수 내부에서 사용되는 변수의 값을 전달받기 위해 정의할 수 있다.
#어떠한 값을 반환하고자 할 때는 return을 이용한다. return문은 조냊하지 않을 수 있다.
def add(a,b):
    return a+b
print(add(1,3))
#동일한 함수의 결과까지 출력하는 경우 return문 없이 함수를 작성한다.
def show(a,b):
    print(a+b)
show(1,3)

#함수의 인자값을 넣어서 사용하는 경우가 있다.
def test(a,b):
    print(a+b)
test(b=1,a=2)

#함수 안에서 한수 밖의 데이터를 변경해야 되는 경우 global키워드를 사용하면 된다.
a= 0
result =0
def func(i):
    global a
    a+=i

for i in range(10):
    func(i)

print(a)

#Lambda Express

def add(a,b):
    return a+b

#일반적인 add()메서드 사용
print(add(3,5))

#람다 표현식으로 구현한 add() 메서드
print((lambda a,b : a+b)(3,7))