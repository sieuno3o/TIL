다시 정립할 것을 간단히 정리힘

# Section3
## 수학 연산자
```py
# floor division(소수점을 없앰)
print(7 // 2)
```

## f-string
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

## 논리 연산자
- `isinstance (value, int)` 자료형을 확인하는 함수
- `not` True와 False를 반대로 바꿈
```py
value = 3

if isinstance(value, int) or value > 5: 
    print("Correct")
else:
    print("Not correct")
# 출력: Correct

if not isinstance(value, float):
    print(f"{value} is not float")
# 출력: 3 is not float
```
<br>

# Section4

## List data structure
```py
countries = ["South Korea", "USA", "Japan", "China"]

print(countries[len(countries) - 1])
# China

print(countries[-2])
# Vietnam

print(countries.pop())
# China

print(countries.pop(0))
# South Korea

print(countries)
# ['USA', 'Vietnam']


element = "c"
alphabets = ["b", element, "d"]

print(alphabets)
# ['b', 'c', 'd']

alphabets.append("e")
print(alphabets)
# ['b', 'c', 'd', 'e']

alphabets += ["f", "g"]
print(alphabets)
# ['b', 'c', 'd', 'e', 'f', 'g']

alphabets.insert(0, "a")
print(alphabets)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

## For loop
```py
alphabets = ['a', 'b', 'c', 'd']

for alphabet in alphabets:
    print(f"{alphabet} is char")

# a is char
# b is char
# c is char
# d is char


# 문자열 반복
for char in "South":
    print(char)

# S
# o
# u
# t
# h



numbers = [1, 2, 3, 4]
sum = 0

for number in numbers:
    sum += number

print(sum / len(numbers))
# 2.5


# Max value (최댓값)
numbers = [1, 2, 3, 4]
max_num = 0

for number in numbers:
    if number > max_num:
        max_num = number

print(max_num)
# 4

print(max(numbers))
# 4

print(max(1, 5))
# 5


# 1부터 10까지의 합
sum = 0

for i in range(1, 11):
    sum += i

print(sum)
# 55


# Odd number (홀수)
for i in range(1, 11, 2):
    print(i)

# 1
# 3
# 5
# 7
# 9
```