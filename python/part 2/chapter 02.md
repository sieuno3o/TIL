# 변수와 자료형

## 01 변수의 이해

### 변수와 값

```py
professor = "Sieun kim"
```

위 코드의 뜻은 파이썬에서 `professor`라는 공간에 `Sieun Kim`이라는 글자를 넣으라는 뜻.  
-> 정확하게는 `professor`라는 변수에 `Sieun Kim`이라는 값을 넣으라는 뜻.  
-> 변수에 값을 넣는 과정을 **할당**이라고 부름

```py
print(a+b)    # a 변수의 값 + b 변수의 값을 출력하라
print("a+b")  # 'a+b'라는 문자를 그대로 화면에 출력하라
```

### 변수와 메모리

- 변수 : 어떠한 값을 저장하는 장소
- 변수에 값이 저장되는 공간 -> 메모리
- 변수의 저장위치 -> 메모리 주소

`a = 3`이라고 했을 때, a는 3이라는 것이 아니라 a라고 하는 메모리 공간(메모리 주소, 변수)에 3이라는 값을 넣어라는 뜻.

### 변수명 선언

- 알파벳, 숫자, 밑줄로 선언
- 대소문자 구분
- 특별한 의미가 있는 예약어 사용 x

<br>

## 02 자료형과 기본 연산

### 메모리 공간

컴퓨터는 이진수 사용. 이진수 한 자리 -> bit  
8bit -> 2byte, 1024byte -> 1kilobyte(KB), 1024KB -> 1megabyte(MB)

### 기본 자료형

| 자료형          | 설명                 | 예시        | 선언형태     |
| --------------- | -------------------- | ----------- | ------------ |
| 정수형(int)     | 양수, 정수           | 1, 2, -10   | data = 1     |
| 실수형(float)   | 소수점 포함된 실수   | 10.2, 9.0   | data = 9.0   |
| 문자형(str)     | 따옴표 들어간 문자형 | abc         | data = 'abc' |
| 불린형(boolean) | 참 또는 거짓         | True, False | data = True  |

### 간단한 연산

- 연산자 : 기호
- 피연산자 : 연산자에 의해 계산되는 숫자

1. 사칙연산 : `+` `-` `\` `*`
2. 제곱승 : `**`
3. 나눗셈 몫과 나머지 : `//` -> 몫, `%` -> 나머지
4. 증가 연산, 감소 연산 : `+=` `-=`

<br>

## 03 자료형 변환

1. 정수 - 실수
   - 변수 간 계산할 때 필요하다고 생각되면 스스로 정수를 실수로 변환
   - 실수형이 정수형으로 변환될 때는 소수점 이하 **내림**이 발생

```py
>>> a = 10.0
>>> b = 3
>>> print (a/b)
3.333333333333
```

```py
>>> a = int(10.7)
>>> print(a)
10
```

2. 숫자 - 문자

```py
>>> a = '76.3'
>>> b = float(a)
>>> print(a+b)     # 문자열과 숫자열의 덧셈이 불가능하여 에러 발생
Error

>>> a = float (a)
>>> b = a
>>> print(a+b)
152.6
```

```py
>>> a = str(a)
>>> b = str(b)
>>> print(a+b)
76.376.3          # 문자열 간 덧셈은 단순 연결!
```

### 자료형 확인하기

- `type(data)` 사용
