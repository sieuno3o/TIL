def Fahrenheit():
    celsius = float(input("변환하고 싶은 섭씨온도를 입력하세요 : "))
    fahrenheit = (celsius * 1.8) + 32

    print("섭씨온도: %.1f" % (celsius))
    print("화씨온도: %.1f" % (fahrenheit))


if __name__ == "__main__":
    Fahrenheit()
