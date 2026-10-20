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

##