# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 

# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

#예시 입출력
#입력(26) 출력(4)
#입력(55) 출력(3)
#입력(1) 출력(60)
#입력(0) 출력(1)
"""
[힌트]
1. 수를 각 자리별로 다루기 위해서는 string으로 전환해야합니다.
2. 인덱싱과 문자열에 대해 공부했던 것을 생각하며 str(), int()를 적절히 활용해봅시다.
"""

num = input("N을 입력하세요: ")
cycle = 0
def rightside(num):
    if len(num) == 1:
        return num[0]
    else:
        return num[1]

cycle = 0
original = input("N을 입력하세요: ")

#10의자리로 맞추자
if len(original) == 1:
    num = '0' + original 
else:
    num = original

num = num[1] + rightside(str(int(num[0])+int(num[1])))
cycle += 1
while int(num) != int(original):
    num = num[1] + rightside(str(int(num[0])+int(num[1])))
    cycle += 1

print(cycle)
