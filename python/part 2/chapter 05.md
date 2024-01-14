# 함수

## 01 함수 기초 

### 함수의 개념과 장점

- 함수 : 어떤 일을 수행하는 코드의 덩어리 (코드의 묶음)
1. 필요할 때마다 호출 가능
2. 논리적인 단위로 분할 가능 
3. 코드의 캡슐화

### 함수의 선언 
```py
def 함수 이름 (매개변수):
    명령문 1
    명령문 2
    return <반환값>
```
1. def: 함수의 정의를 시작한다는 말
2. 함수 이름: 소문자, 띄어쓰기는 _로, 동사와 명사를 함께, 명료하고 짧게 
3. 매개변수: 함수에서 입력값으로 사용하는 변수, 한개 이상의 값 기재 가능
4. 명령문: 반드시 들여쓰기 하여 수행해야 하는 코드 입력

### 함수의 실행순서
```py
def calculate_rectangle_area(x,y):
    return x * y

rectangle_x = 10
rectangle_y = 20 

print("사각형 x의 길이:", rectangle_x)
print("사각형 y의 길이:", rectangle_y)
print("사각형의 넓이:", calculate_rectangle_area(rectangle_x, rectangle_y))
```
    사각형 x의 길이: 10
    사각형 y의 길이: 20
    사각형의 넓이: 200

### 프로그래밍의 함수와 수학의 함수
```py
def f(x):
    return 2 * x + 7
def g(x):
    return x ** 2
x = 2
print(f(x) + g(x) + f(g(x)) + g(f(x)))
```
    151

### 함수의 형태 
```py
def a(): # 매개변수 x, 반환값 x
    print(5 * 7)
def b(): # 매개변수 o, 반환값 x
    print(x * y)
def c(): # 매개변수 x, 반환값 o
    return(5 * 7)
def d(): # 매개변수 o, 반환값 o
    return(x * y)
```

<br>

## 02 함수 심화

### 함수의 호출 방식
```py
def f(x):
    y = x
    x = 5
    return y * y

x = 3
print(f(x))
print(x)
```
    9
    3
1. 값에 의한 호출 
    - 함수에 인수를 넘길 때 `값`
    - 함수 내부 인수값 변경시 호출 변수 영향 X
2. 참조 호출
    - 함수에 인수를 넘길 때 `메모리 주소`
    - 함수 내부 인수값 변경시 호출된 변수값도 변경
3. 객체 호출
    - 새로운 값을 할당하기 전까지는 기존에 넘어온 인수 객체 주소값을 그대로 사용하는 방식 

```py
def spam(eggs):
    eggs.append(1)
    eggs = [2,3]

ham = [0]
spam(ham)
print(ham)
```
    [0, 1]

### 변수의 사용 법위
- 지역 변수 : 함수 내부에서만 사용 
- 전역 변수 : 프로그램 전체에서 사용
```py
def f() :
    s = "I love London!" # 지역변수
    print(s)

s = "I love Paris!" # 전역변수
f()
print(s) 
```
    I love London!
    I love Paris!
```py
def f() :
    global s # 지역변수를 전역변수로 사용
    s = "I love London!"
    print(s)             

s = "I love Paris!"      
f()
print(s)     
```
    I love London!
    I love London!

### 재귀함수 
```py
# 팩토리얼 점화식
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Input Number for Factorial Calculation: "))))
```
    Input Number for Factorial Calculation: 5 <- 사용자 입력
    120

<br>

## 03 함수의 인수

### 키워드 인수
- 함수에 입력되는 매개변수의 변수명을 사용하여 함수의 인수를 지정하는 방법
```py
def print_something(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something("Sungchul", "TEAMLAB")
print_something(your_name = "TEAMLAB", my_name = "Sungchul") 
# 변수명만 잘 기재된다면 순서에 상관없이 원하는 변수에 넣을 수 있음 
```
    Hello TEAMLAB, My name is Sungchul
    Hello TEAMLAB, My name is Sungchul

### 디폴트 인수 
- 매개변수에 기본값 설정
- 아무런 값도 인수로 넘어가지 않을 때 지정된 기본값을 사용
```py
def print_something_2(my_name, your_name = "TEAMLAB"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something_2("Sungchul", "TEAMLAB")
print_something_2("Sungchul")
```
    Hello TEAMLAB, My name is Sungchul
    Hello TEAMLAB, My name is Sungchul

### 가변 인수
- *로 표현 가능
- *는 일반적인 키워드 인수에 대한 선언이 모두 끝난 후 마지막에 선언
- 리스트와 비슷한 튜플 형태의 함수 안에서 사용되어지므로 인덱스를 사용
```py
def asterisk_test(a, b, *args):
    return a + b + sum(args)

print(asterisk_test(1, 2, 3, 4, 5))
```
    15
```py
def asterisk_test_2 (*args) :
    x, y, *z = args
    return x, y, z

print(asterisk_test_2(3, 4, 5, 10, 20))
```
    (3, 4, [5, 10, 20])

### 키워드 가변 인수
- 가변 인수의 단점인 변수의 이름을 저장할 수 없는 부분을 보완
- `**` 이용하여 함수의 매개변수 표시 
```py
def kwargs_test(**kwargs) :
    print(kwargs)
    print("First valu is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))

kwargs_test(first = 3, second = 4, third = 5)
```
    {'first': 3, 'second': 4, 'third': 5}
    First valu is 3
    Second value is 4
    Third value is 5

<br>

## 04 좋은 코드를 작성하는 방법

### 좋은 코드의 의미
- 많은 사람이 쉽게 읽고 이해할 수 있도록 가독성이 좋아야 함

### 코딩 규칙
1. 들여쓰기 4 스페이스
2. 한 줄에 최대 79자까지
3. 불필요한 공백 없애기
4. = 연산자는 1칸 이상 띄우지 않기
5. 주석은 항상 갱신하고 불필요한 주석 삭제하기
6. 소문자l , 대문자O, 대문자I 구분하기 어려우니 사용금지
7. 함수명은 소문자로 구성, 필요하면 밑줄로

### 함수 개발 가이드 라인
- 함수이름 : 함수 내용 짧게, 함수의 역할과 의도가 명확하게 드러나게
- 함수역할 : 한 가지 역할을 명확하게
- 함수를 만들어야 하는 경우
    - 공통으로 사용되는 코드
    - 복잡한 로직이 사용 되었을 때 식별 가능한 이름의 함수로 변환
