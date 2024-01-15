# 파이썬 스타일 코드 I

## 01 파이썬 스타일 코드의 이해

### 파이썬 스타일 코드의 개념

- 파이썬 스타일의 코드 작성 기법

```py
# 여러 단어를 연결하는 코드
colors = ['red', 'blue', 'grren', 'yellow']
result = ''
for s in colors:
    result += s

print(result)
```

    redbluegreenyellow

- 하지만 파이썬에서는 위처럼 여러 줄에 걸쳐 코딩하지 않음

```py
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)
```

    redbluegreenyellow

- 파이썬 스타일 코드: 특별한 문법이 아니라 파이썬에서 기본으로 제공하는 문법들을 활용하여 코딩 하는 것

### 파이썬 스타일 코드를 사용하는 이유

- 파이썬 스타일 코드를 알아야 다른사람이 작성한 코드를 쉽게 이해할 수 있음
- 파이썬 스타일 코드에 익숙해지면 코드 자체도 간결해지고 코드 작성 시간도 줄일 수 있음

<br>

## 02 문자열의 분리 및 결합

### 문자열의 분리: split() 함수

- 특정 값을 기준으로 문자열을 분리하여 리스트 형태로 변환

```py
>>> example = 'python,jquery,javascript'

>>> example.split(",")
['python', 'jquery', 'javascript']

>>> a, b, c = example.split(",") # 언패킹
>>> print(a, b, c)
python python javascript
```

### 문자열의 결합: join() 함수

- 문자열로 구성된 리스트를 합쳐 하나의 문자열로 만들 때 사용

```py
>>> colors = ['red', 'blue', 'green', 'yellow']

>>> result = ''.join(colors)
>>> result
'redbluegreenyellow'

>>> result = '-'.join(colors)
>>> result
'red-blue-green-yellow'
```

<br>

## 03 리스트 컴프리헨션

### 리스트 컴프리헨션 다루기

- 리스트 컴프리헨션: 기존 리스트형을 사용하여 간단하게 새로운 리스트를 만드는 기법

```py
# 일반적인 반복문 + 리스트
>>> result = []
>>> for i in range(10):
>>>     result.append(i)

>>> result
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```py
# 리스트 컴프리헨션
>>> result = [i for i in range(10)]
>>> result
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 리스트 컴프리헨션의 사용법

1. 필터링

```py
# i가 짝수라면 리스트에 i 추가
>>> result = [i for i in range(10) if i % 2 == 0]
>>> result
[0, 2, 4, 6, 8]

# if문을 앞으로 옮겨 else문과 함께 사용할 수 있음
# i가 짝수라면 리스트에 i 추가, 그렇지 않다면 10 추가
>>> result = [i if i % 2 == 0 else 10 for i in range(10)]
>>> result
[0, 10, 2, 10, 4, 10, 6, 10, 8, 10]
```

2. 중첩 반복문

```py
>>> word_1 = "ab"
>>> word_2 = "cd"
>>> result = [i + j for i in word_1 for j in word_2]
>>> result
['ac', 'ad', 'bc', 'bd']
```

```py
# 중첩 반복문에서도 필터링 적용 가능
>>> word_1 = "abc"
>>> word_2 = "cdf"
>>> result = [i + j for i in word_1 for j in word_2 if not (i==j)]
>>> result
['ac', 'ad', 'af', 'bc', 'bd', 'bf', 'cd', 'cf']
```

3. 이차원 리스트

```py
>>> words = 'The quick brown fox jumps over the lazy dog'.split()
>>> print(words)
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

>>> stuff = [[w.upper(), w.lower (), len(w)] for w in words]
>>> for i in stuff:
>>>     print(i)

['THE', 'the', 3]
['QUICK', 'quick', 5]
['BROWN', 'brown', 5]
['FOX', 'fox', 3]
['JUMPS', 'jumps', 5]
['OVER', 'over', 4]
['THE', 'the', 3]
['LAZY', 'lazy', 4]
['DOG', 'dog', 3]
```

```py
>>> case_1 = ["A", "B", "C"]
>>> case_2 = ["D", "E", "А"]

# 일차원 리스트를 만드는 코드, 앞의 for문이 먼저 실행됨
>>> result_1 = [i + j for i in case_1 for j in case 2]
›>> result_1
['AD', 'AE', 'AA', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']

# 이차원 리스트를 만드는 코드, 뒤의 for문이 먼저 실행됨
>>> result = [[i + j for i in case_1] for j in case_2]
>>> result
[['AD', 'BD', 'CD'], ['АЕ', 'ВЕ', 'СЕ'], ['АА', 'ВА', 'СА']]
```

### 리스트 컴프리헨션의 기능

- 리스트 컴프리헨션은 내부적으로 잘 구성된 메모리 사용 방식으로 기존 for문보다 시간면에서 효율적인 연산을 수행할 수 있음

<br>

## 04 다양한 방식의 리스트값 출력

1. 리스트값에 인덱스를 붙여 출력: enumerate() 함수
   - 리스트의 값을 추출 할 때 인덱스를 붙여 함께 출력하는 방법

```py
# 리스트에 있는 인덱스와 값을 언패킹
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
>>>     print(i, v)
0 tic
1 tac
2 toe
```

```py
# 주로 딕셔너리형 인덱스를 키로, 단어를 값으로 하여 쌍으로 묶어 결과를 출력하는 방식을 사용함
>>> {i:j for i, j in enumerate('TEAMLAB is an academic institute located in South Korea.'.split())}
{0:'TEAMLAB', 1:'is', 2:'an', 3:'academic', 4:'institute', 5:'located', 6:'in', 7:'South', 8:'Korea.'}
```

2. 리스트값을 병렬로 묶어 출력: zip() 함수
   - 1개 이상의 리스트값이 같은 인덱스에 있을 때 병렬로 묶는 함수

```py
>>> alist = ['a1', 'a2', 'a3']
>>> blist = ['b1', 'b2', 'b3']
>>> for a, b in zip(alist, blist): # 병렬로 값을 추출
>>>     print(a, b)

a1 b1
a2 b2
a3 b3
```

```py
# 인덱스끼리 값을 더하는 것도 가능
>>> a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
(1, 10, 100) (2, 20, 200) (3, 30, 300)

>>> [sum(x) ofr x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
[111, 222, 333]
```
