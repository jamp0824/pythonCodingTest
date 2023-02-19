#수학적 기능이 포함되어 있는 라이브러리이다 .Math
#팩토리얼, 제곱근, 최대공약수GCD등을 계산해주는 기능을 포함하고 있으므로, 수학 계산을 요구하는 문제를 만났을 때 효과적으로 사용할 수 있따.

#factorial(x) 함수는 x! 값을 반환한다.

import math

print(math.factorial(5)) #5 팩토리얼 출력

#그리고 math 라이브러리의 sqrt(x) 함수는 x의 제곱근을 반환한다. 7의 제곱근을 출력하는 예시코드는 다음과 같다

print(math.sqrt(7))

#최대 공약수를 구해야 할 때 math 라이브러리 gcd(a,b)의 함수를 이용할 수 있다.

print(math.gcd(21,14))

#수학 공식에 자주 등장하는 상수가 필요할 때에도 math 라이브러리를 사용할 수 있다. math 라이브러리는 파이(pi)나 자연상수 e를 제공한다.

print(math.pi)
print(math.e)