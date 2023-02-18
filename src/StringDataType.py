data = 'Hello World'
print(data)

data = "Dont you know that \'I am savage\'?"
print(data)

#문자열 연산
a = "Hello"
b = "World"
print(a+" "+b)

a = "String"
print(a*3)

#파이썬은 문자열을 내부적으로 리스트와 같이 처리한다 문자열은 여러개의 문자가 합쳐진 리스트라고 볼수있다
a = "ABDDFD"
print(a[:4])
print(a[1:])

#튜플자료형 : 리스트와 거의 비슷한데 다른 차이가 있다
#튜플은 한번 선언된 값을 변경할 수 없다.
#리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이요한다.
a = (1,2,3,4,5)
print(a)
#a[2] = 7  #TypeError: 'tuple' object does not support item assignment
print(a[2])
#튜플은 그래프 알고리즘을 구현할 때 자주 사용된다
#다익스트라 최단 경로 알고리즘처럼 최단 경로를 찾아주는 알고리즘의 내부에서는 우선순위 큐를 사용하는데
#이는 해당 알고리즘에서 우선순위 큐에 한번 들어간 값은 변경되지 않는다

