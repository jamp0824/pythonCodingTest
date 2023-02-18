#리스트나 튜플은 값을 순차적으로 저장한다.
#하지만 사전 자료현은 키-값 쌍을 데이터로 가진다.
#우리가 변경 불가능한 데이터를 키로 사용할 수 있다.
#변경 불가능한 자료형이란 수 자료형, 문자열 자료형, 튜플 자료형 같이 한번 초기화 되면 변경이 불가능한 자료형을 의미한다.
#흔히 사용되지 않지만 튜플 자료형은 사전 자료형의 키로 사용되기도 하는데 이는 Q 22블록 이동하기 문제풀이에서 사용된다

# 해시 테이블 : 파이썬에서 내부적으로 해시 테이블을 이용 데이터 검색 수정에 있어 O(1)의 시간을 처리
#이와 같이 키-값 쌍으로 이용하는 값을 처리하는하는데 있어 리스트보다 빠르게 동작한다.

data= dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

#사저 자료형에 특정한 원소가 있는지 검사할 때는 '원소in 사전'의 형태를 사용하라 수 있다.
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

#사전 자료형 관련 함수

#키 데이터만 담은 리스트
key_lists = data.keys()
print(key_lists)

value_lists = data.values()
print(value_lists)

#각 키에 따른 값을 하나씩 출력
for key in key_lists:
    print(data[key])
