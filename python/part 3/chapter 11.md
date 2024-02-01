# 모듈과 패키지

## 01 모듈과 패키지의 이해

- 이미 작성된 프로그램 `모듈`, 이 프로그램의 묶음 `패키지`

### 모듈의 개념

- 모듈은 프로그래밍에서만 나오는 개념이 아님. 여러 분야에서 매우 다양하게 사용되고 있음.
- 프로그래밍에서 모듈이란 `작은 프로그램 조각`을 뜻함. 즉 하나하나 연결해 어떤 목적으로 가진 프로그램을 만들기 위한 작은 프로그램임.
- 파이썬에서 기본으로 제공하는 내장 모듈 `random` 예시

```py
# import 이용하여 모듈 호출
>>> import random
>>> random.randint(1, 1000)
198
```

### 패키지의 개념

- 패키지는 `모듈의 묶음`임
- 패키지를 호출하는 명령어는 `from`
- 하나의 패키지 안에 여러개의 모듈이 존재함

<br>

## 02 모듈 만들기

### 모듈 만들기 실습

- 파이썬에서는 `.py` 파일 자체를 모듈로 사용할 수 있음

```py
# 모듈 코드 작성
# fah_converter.py
def covert_c_to_f(celcius_value):
    return celcius_value * 9.0 / 5 + 32
```

```py
# 모듈을 사용하는 코드(클라이언트 코드) 작성
# module_ex.py
import fah_converter

print("Enter a celsius value:")
celsius = float(input())
fahrenheit = fah_converter.covert_c_to_f(celsius)
print("That's", fahrenheit, "degrees Fahrenheit.")
```

- `fahrenheit = fah_converter.covert_c_to_f(celsius)`를 이용하여 모듈 내 함수를 가져다 사용할 수 있게 됨
- 꼭!! **같은 디렉토리 안**에 있어야 함

### 네임 스페이스

**모듈의 사용 범위를 명확히 지정**하도록 네임 스페이스를 만들어줘야 함

1. 모듈 이름에 `알리아스`를 생성하여 모듈 안으로 코드를 호출하는 방법

```py
# as이용하여 모듈 이름을 간단하게 바꿔줌
import fah_cinverter as fah
print(fah.covert_x_to_f(41.6))
```

2. `from 구문`을 사용하여 모듈에서 특정 함수 또는 클래스만 호출하는 방법

```py
from fah_converter import covert_c_to_f
print(covert_c_to_f(41.6))
```

3. 모듈 안의 모든 함수, 클래스, 변수를 가져오는 `별표(*)`를 사용하는 방법

```py
from ha_converter import *
print(covert_c_to_f(41.6))
```

세 가지중 가장 선호하는 방법은 무엇일까?

- `일리아스`를 사용하여 호출하는 방법!
- 각각의 함수나 클래스가 어디서 나오는지 명확히 표기하는 것이 좋음

### 내장 모듈의 사용

1. `random` 모듈

   - `random.randint(0, 100)`: 0 ~ 100 사이의 정수 난수를 생성
   - `random.randint()`: 일반적인 난수 생성

2. `time` 모듈

   - `time.localtime()`: 현재 시각 출력

3. `urllib` 모듈
   - 웹 주소의 정보를 불러오는 모듈
   - `urllib.request.urlopen()`: 괄호 안에 특정 웹 주소 입력 시 해당 주소의 HTML 정보를 가져옴

<br>

## 03 패키지 만들기

### 패키지의 구성

- 패키지: 여러개의 .py 파일이 하나의 디렉터리에 들어가 있는 것
- 라이브러리: 다른 사람이 만들 프로그램을 불러와 사용하는 것

### 패키지 만들기 실습

1. 디렉터리 구성하기
   - 만들어낼 패키지 `roboadvisor` 안에는 세가지 기능이 들어가 있음
     1. crawling: 주식 관련 데이터를 인터넷에서 가져오는 기능
     2. database: 가져온 데이터를 데이터베이스에 저장하는 기능
     3. analysis: 해당 정보를 분석하여 의미 있는 값을 뽑아내는 기능

```py
# 디렉터리 생성
mkdir roboadvisor
cd roboadvisor
mkdir crawling
mkdir database
mkdir analysis
```

2. 디렉터리별로 필요한 모듈 만들기

   - 패키지 안에 또 하나의 패키지가 들어갈 수 있음
   - 각각의 디렉터리를 하나의 패키지로 선언하기 위해선 예약 파일인 `__init__.py`를 만들어야 함
     - 각 디렉터리가 패키지임을 나타내는 예약 파일
     - 해당 파일을 추가하면 패키지의 기본 구조가 만들어짐

```py
#analysis/series.py
def series_test() :
    print("series")
```

```py
#analysis/statics.py
def statics_test() :
    print("statics")
```

```py
>>> from roboadvisor.analysis import series
>>> series.series_test
series
```

- 코드 실행 시 `__pycache__`라는 디렉터리 생성됨 (파이썬의 언어적 특성 때문!)

  - 해당 프로그램이 작동될 때 사용하기 위한 모듈들의 컴파일 결과가 저장됨
  - 해당 프로그램 또는 파이선 셸이 완전히 종료한 후 수정해야 모듈의 결과가 반영 된다는 사실 기억하기 . . .

3.  디렉터리 별로 `__init__.py` 구성하기

    - 패키지 개발자나 설치 시 확인해야 할 내용 등의 메타데이터라고 할 수 있음
    - 하지만 가장 중요한 것은 **패키지의 구조**!!

```py
# roboadvisor/__init__.py
# 각각의 패키지를 __init__.py 안에 __all__과 import문을 사용해 선언
import analysis
import crawling
import database

__all__ = ['analysis', 'crawling', 'database']
```

```py
# analysis/__init__.py
# 각 패키지에 포함된 모듈명을 모두 작성해야 함
# 패키지로 표시하기 위해 꼭 해야 하는 작업, 패키지별로 모두 처리

# from . 이용하여 현재 디렉터리인 analysis의 패키지를 호출함
from . import series
from . import statics

__all__ = ['series', 'statics']
```

4. `__main__.py` 파일 만들기 (패키지 자체를 실행하기 위함)

```py
#__main__.py
from analysis.series import series_test
from crawling.parser import parser_test

if __name__ == '__main__' :
    series_test()
    parser_test()
```

5. 실행하기 (패키지 이름만 호출)
   - 해당 패키지의 최상위 디렉터리에서 'python 패키지명' 을 입력하여 실행

### 패키지 네임스페이스

패키지 내에서 모듈을 서로 호출할 때 사용

1. 절대 참조: 모듈의 경로를 모두 호출하는 것
   - `from 전체 패키지.서브 패키지 import 모듈` 형식

```py
from roboadvisor.analysis import series
```

```py
# __init__ 파일을 만들 때도 절대 참조로 호출하는 것이 좋음
__all__ = ["analysis", "crawling", "database"]

from roboadvisor import analysis
from roboadvisor import crawling
from roboadvisor import database
```

2. 상대 참조: 호출하는 디렉터리 기준으로 호출하는 것

```py
from . series import series_test
from .. crawling.parser import parser_test
```

**패키지 내에서는 상대 참조로 호출하는 것을 추천하지 않음~!!**

<br>

## 04 가상환경 사용하기

### 가상환경의 개념

- 패키지를 설치할 때 서로 다른 프로젝트가 영향을 주지 않도록 독립적인 프로젝트 수행 환경

|  가상환경 도구   | 특징                                                                                 |
| :--------------: | :----------------------------------------------------------------------------------- |
| virtualenv + pip | 가장 대표적인 가상환경 관리도구 <br> 레퍼런스와 패키지가 가장 많음                   |
|      conda       | 상용 가상환경 도구인 miniconda의 기본 가상환경 도구 <br> 설치가 쉬워 윈도에서 유용함 |

### 가상환경 설정하기 (conda 사용)

```py
conda create -n my_project python=3.4
# conda create: 가상환경 새로 만들기
# -n my_project: 가상환경 이름
# python=3.4: 파이썬 버전
```

```py
# my_project라는 가상환경을 활성화
activate my_project

# 현재 실행되는 파이썬의 위치가 어디인지 출력됨
where python

# 가상환경 종료
deactivate
```

```py
#가상환경 패키지 설치하고 실습해보기 ...~
conda install matplotlib
```