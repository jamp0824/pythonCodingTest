import sys
#input함수는 느려서 시간 초과로 오답 판정을 받을 수 있음
#sys라이브러리에 있는 sys.stdin().readline()이용한다. sys라이브러리를 이용할 때는 한줄 입력을 받고 나서 rstrip()함수를 호출한다
#그러한 이유는 readline()으로 입력하면 입력후 Enter키가 발생하는데 이 공백 문자를 제거하려면 rstrip()함수를 사용해야한다.
#data = sys.stdin.readline().rstrip()
#print(data)

#print()는 기본적으로 출력 이휴에 줄바꿈을 수행한다.
#print(,) ,를 이용하여 매개변수를 넣으면서 출력시 띄어쓰기로 구분되어 사용된다.

#출력할 변수에서 +를 더하면 에러가 난다.
answer = 8
##print("test"+answer+"itis right")  #TypeError: can only concatenate str (not "int") to str

print("test"+str(answer)+" it is right")
#, 를 사용하면 의도치 않게 공백이 사용된다.
print("test",answer,'it is right')

#python 3.6버전 부터는 f-string문법을 사용할 수 있다.
answer = 7
print(f"정답은 {answer}입니다")