import numpy as np

# 사용자가 원하는 횟수를 입력 받습니다.
n = int(input("몇 번 숫자를 뽑으시겠습니까? "))

# 1부터 45까지의 숫자를 리스트로 만듭니다.
numbers = list(range(1, 46))

# n번 반복하면서 무작위로 6개의 숫자를 뽑습니다.
for i in range(n):
    # numpy 모듈을 사용하여 무작위로 6개의 숫자를 선택합니다.
    selected_numbers = np.random.choice(numbers, size=6, replace=False)
    # 선택된 숫자를 출력합니다.
    print(selected_numbers)
