# 다시 정립할 것 간단히 정리
## Python REPL (대화형 인터프리터)
파이썬 코드를 한 줄씩 입력하고, 실행 결과를 즉시 확인할 수 있는 대화형 실행 환경
- Read: 코드를 읽고
- Eval: 입력 코드 실행하고 평가하고
- Print: 실행 결과 출력하고
- Loop: 다음 입력을 기다리며 과정을 반복 

```py
python

>>> print("hello")
hello
>>> 1 + 2
3
```
## 파이썬 기초 지식
### 알고리즘
특정 작업을 수행하기 위한 정확한 단계별 절차 또는 계획
### 클래스와 인스턴스
- 클래스: 객체를 만들기위한 설계도, 틀
- 인스턴스: 클래스의 틀을 기반으로 만들어진 실제
```py
# 1. 클래스(설계도) 정의
class Car:
    def __init__(self, name, color):
        self.name = name    # 속성 (변수)
        self.color = color  # 속성 (변수)

    def drive(self):       # 기능 (메소드)
        return f"{self.color} {self.name}가 달립니다."

# 2. 인스턴스(실체) 생성 -> 메모리에 할당됨
car1 = Car("소나타", "흰색")
car2 = Car("아반떼", "검은색")

# 3. 인스턴스 사용
print(car1.drive())  # 출력: 흰색 소나타가 달립니다.
print(car2.drive())  # 출력: 검은색 아반떼가 달립니다.
```

### 재귀 함수와 반복 함수
재귀 함수
- 함수가 자기 자신을 호출하는 방식
- 반드시 **종료 조건** 필요

```python
def factorial(n):
    if n == 0: # 종료 조건
        return 1
    return n * factorial(n - 1)
```

반복 함수
- `for`, `while`을 사용하여 반복하는 방식
- 일반적으로 재귀보다 메모리 효율적

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
### 오버 로딩과 오버 라이딩
- 오버 로딩: 같은 이름을 가진 메서드들이 다양한 파라미터 조합을 받는 것
- 오버 라이딩: 상속받은 메서드를 필요에 따라 변경 하는 것

### Process와 Thread
프로세스 (Process)
- 실행 중인 프로그램
- 각 프로세스는 독립적인 메모리 공간을 가짐
- 프로세스 간 데이터 공유가 상대적으로 어려움

스레드 (Thread)
- 프로세스 내부에서 실행되는 작업의 단위
- 하나의 프로세스에 여러 스레드가 존재할 수 있음
- 같은 프로세스의 스레드끼리는 메모리를 공유함

## 코드

### 수학 연산자
```py
# floor division(소수점을 없앰)
print(7 // 2)
```

### f-string
```py
# 과거 스타일
name = "Joon"
age = 30
print("Hello, %s." % name)
print("Hello, %s, I am %s" % (name, age))

# Python 2.6
print("Hello, {}. I am {}.".format(name, age))
print("Hello, {1}. I am {0}.".format(age, name))

# Python 3.6
person = {'name': 'Joon', 'age': 17}
print(f"Hello, {name}. I am {age}.")
print(F"Hello, {name}. I am {age}.")
print(f"{name.lower()} is cool.")
```