# 예외 처리와 파일 다루기

## 예외 처리

### 예외의 개념과 사례

- 예외: 프로그램을 개발하면서 예상하지 못한 상황이 발생하는 것

### 예측 가능한 예외와 예측 불가능한 예외

- 예측 가능한 예: 발생 여부를 개발자가 사전에 인지할 수 있는 예외 (대책 마련 가능!)
- 예측 불가능한 예외: 대부분 인터프리터가 자동으로 이것이 예외라고 사용자에게 알려줌 동시에 프로그램이 종료되므로 **예외 처리 구문**을 이용하여 적절한 조치를 해야 함

### 예외 처리 구문

1. try-except문

```py
try :
    예외 발생 가능한 코드
except 예외 타입 :
    예외 발생 시 실행되는 코드
```

```py
>>> for i in range(10) :
>>>     try :
>>>         print(10 / i)
>>>     except ZeroDivisionError :
>>>         print("Not divided by 0")

Not divided by 0
10.0
5.0
3.333333333333335
...
```

2. try-except-else문

```py
try :
    예외 발생 가능한 코드
except 예외 타입 :
    예외 발생 시 실행되는 코드
else :
    예외가 발생하지 않을 때 실행되는 코드
```

```py
for i in range(10) :
    try :
        result = 10/i
    except ZeroDivisionError :
        print("Not divided by 0")
    else :
        print(10/i)
```

3. try-except-finally문

```py
try :
    예외 발생 가능한 코드
except 예외 타입 :
    예외 발생 시 실행되는 코드
finally :
    예외 발생 여부와 상관없이 실행되는 코드
```

```py
try :
    for i in range(1, 10) :
        result = 10//i
        print(result)
except ZeroDivisionError :
    print("Not divided by 0")
finally :
    print("종료되었다.")
```

4. raise문

    - 필요할 때 예외를 발생 시키는 코드
    - `raise 예외 타입(예외 정보)` 이용

5. assert문

    - 미리 알아야 할 예외 정보가 조건을 만족하지 않을 경우 예외를 발생
    - True or False의 변환이 가능한 함수를 이용. False가 반환되면 예외 발생
    - `ssert 예외 조건` 이용

<br>

## 02 파일 다루기

### 파일의 개념

- 파일: 컴퓨터를 실행할 때 가장 기본이 되는 단위

### 파일의 종류

|                      바이너리 파일                       |                      텍스트 파일                       |
| :------------------------------------------------------: | :----------------------------------------------------: |
| 컴퓨터만 이해할 수 있는 형태인 <br> 이진법 형식으로 저장 | 사람도 이해할 수 있는 형태인 <br> 문자열 혀식으로 저장 |
|             메모장으로 열면 내용이 깨져보임              |           메모장으로 열면 내용 확인이 가능함           |
|             엑셀, 워드와 같은 프로그램 파일              |  메모장에 저장된 파일, HTML 파일, 파이썬 코드 파일 등  |

- 텍스트 파일도 **컴퓨터가 처리하기 위해 바이너리 형태로 저장된 파일**임
- 텍스트 파일은 컴퓨터가 이해할 수 있는 형태로 변경하여 저장됨
  - 변경 기준: 아스키코드(ASCII), 유니코드(Unicode)

### 파일 읽기

- `open()` 함수 사용.

```py
f = open("파일명", "파일 열기 모드")
f.close()
```

| 종류 | 설명                                                 |
| :--: | ---------------------------------------------------- |
|  r   | 읽기 모드 : 파일을 읽기만 할 때                      |
|  w   | 쓰기 모드 : 파일에 내용을 쓸 때                      |
|  a   | 추가 모드 : 파일의 마지막에 새로운 내용을 추가 할 때 |

1. 파일 읽기

```py
f = open("dream.txt", "r")
contents = f.read()
print(contents)
f.close
```

2. with문과 함께 사용하기

   - 들여쓰기 동안 open()함수 유지, 끝나면 open()함수도 종료

```py
# as문을 사용하여 변수명 할당
with open("dream.txt","r") as my_file:
    contents = my_file.read()
    print(type(contents), contents)
```

3. 한 줄씩 읽어 리스트형으로 반환하기

   - `readlines()` 함수를 사용하여 한 줄씩 내용을 읽어와 문자열 형태로 저장할 수 있음

```py
with open("dream.txt","r") as my_file:
    # 파일 전체 리스트 반환
    content_list = my_file.readlines()
    print(type(content_list))
    print(content_list)
```

4. 실행할 때마다 한 줄씩 읽어 오기

```py
with open("dream.txt", "r") as my_file:
    i = 0
    while 1:
        line = my_file.readline()
        if not line:
            break
        print(str(i)+"==="+ line.replace("\n","")) # 한 줄씩 값 출력
        i = i + 1
```

5. 파일에 저장된 글자의 통계 정보 출력하기

- `split()`함수와 `len()`함수를 함께 사용

```py
with open("dream.txt", "r") as my_file :
    contents = my_file.read()
    word_list = contents.split(" ")
    line_list = contents.split("\n")

print("총 글자의 수:", len(contents))
print("총 단어의 수:", len(word_list))
print("총 줄의 수:", len(line_list))
```

### 파일 쓰기

- 인코딩 : 텍스트 파일을 저장하기 위해 저장할 때 사용하는 표준을 지정하는 것  
  (운영체제나 파일의 사용 환경에 따라 다르게 설정)

```py
f = open("count_log.txt", "w", encoding = "utf8")
for i in range(1, 11) :
    data = "%번째 줄이다.\n"%i
    f.write(data)
f.close()
```

1. 파일 열기 모드 a로 새로운 글 추가하기

   - w(쓰기 모드)는 항상 새로운 파일을 생성함
   - w로 파일을 부르면 기존 파일이 삭제되고 새로운 파일이 생겨 새로운 내용만 기록됨
   - 상황에 따라 기존 파일에 계속 추가하는 작업이 요구될 때는 `a(추가 모드)` 를 사용함

2. 디렉터리 만들기

   - os 모듈 사용
   - `os.path.isdir` 이용시 기존 디렉토리 존재여부 확인 가능

```py
import os
os.mkdir("log")

if not os.path.isdir("log")
    os.mkdir("log")
```

3. 로그 파일 만들기

- 로그 파일: 프로그램이 동작하는 동안 여러 가지 중간 기록을 저장하는 역할을 하는 파일

```py
import os

# 디렉토리 존재하지 않을 시 새로 만듦
if not os.path.isdir("log") :
    os.mkdir("log")

# 한번도 로그 기록이 없었다면 w모드로 파일 생성
if not os.path.exists("log/count_log.txt") :
    f = open("log/count_log.txt", "w", encoding = "utf8")
    f.write("기록이 시작된다.\n")
    f.close()

# 임의의 시간 기록과 숫자를 문구 안에 계속 기록하며 저장
with open("log/count_log.txt", "a", encoding = "utf8") as f :
    import random, datetime
    for i in range(1, 11) :
        stamp = str(datatime.datetime.now())
        value = random.random() * 1000000
        log_line = stamp + "\t" + str(value) + "값이 생성되었다." +"\n"
        f.write(log_line)
```

### pickle 모듈

- 파이썬 프로그램을 실행할 때 생성되는 여러 변수와 객체는 순간적으로 메모리에 로딩되었다가 프로그램이 종료되면 사라짐
- 사용되는 객체를 저장시켜 놓고 필요할 때 다시 불러야 하는 경우를 영속화라고 함
- **영속화** : 필요한 객체를 파일로 저장시켜 다시 사용할 수 있도록 하는 것
  - `pickle()` 모듈은 메모리에 로딩된 객체를 영속화 할 수 있도록 지원함

> 모듈 사용을 위해서는 객체를 저장할 수 있는 파일을 열고 저장하고자 하는 객체를 넘기면 됨
> - 파일을 생성할 때에는 `w`가 아닌 `wb`  
>   -> 여기서 b는 바이너리를 뜻하는 약자로, 텍스트 파일이 아닌 **바이너리 파일로 저장**한다는 의미

> dump() 함수에서는 저장할 객체, 저장될 파일 객체를 차례대로 인수로 넣으면 객체가 해당 파일에 저장됨

```py
import pickle

f = open("list.pickle", "wb")
test = [1, 2, 3, 4, 5]
pickle.dump(test, f)
f.close()
```

> 저장된 pickle 파일을 불러오는 프로세스도 저장 프로세스와 같음  
> list.pickle 파일을 `rb`모드로 읽어온 후 `load` 함수로 불러오면 됨!

> 단순히 생성된 객체를 저장하는 기능도 있지만, 사용자가 직접 생선한 클래스 객체도 저장함