#문제풀이 첫번째 데이터를 입력받는것
#input()
#여러 줄로 입력받는 경우
#입력받는 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장하는 코드의 사용빈도가 높다
# list(map(int,input().split()))
#가장먼저 input으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 바꾼뒤 map을 이용하여 해당 리스트의 모든 함수를 int로 적용한다.
#최종적으로 그 결과를 list()로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분하여 각각 숫자 자료형으로 저장하게 되는 것이다.

#데이터의 개수 입력
# n = int(input())
#각 데이터를 공백으로 구분하여 입력
# data = list(map(int, input().split()))

# data.sort(reverse = True)
# print(data)

# n, m, k = map(int,input().split())
# print(n,m,k)

