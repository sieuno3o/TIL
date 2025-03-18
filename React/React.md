# 변수와 상수

## 1. 변수

```js
let age = 27; // 선언 및 초기화 (초기화 하지 않아도 됨)
console.log(age);

age = 60;
console.log(age);
```

## 2. 상수

```js
const birth = "2003. 03. 22."; // 꼭 초기화 해야함! 재선언 불가
console.log(birth);
```

## 3. 변수 명명 규칙 (네이밍 규칙)

### 3-1. $, \_ 제외한 기호는 사용할 수 없다.

```js
let $_name;
```

### 3-2. 숫자로 시작할 수 없다.

```js
let name1;
let _2name;
```

### 3-3. 예약어를 사용할 수 없다.

## 4. 변수 명명 가이드

```js
let salesCount = 1;
let refundCount = 1;
let totalSalesCount = salesCount - refundCount;
```

# 자료형

## 원시타입

- 기본형 타입이라고도 불림
- 프로그래밍에 있어 가장 기본적인 값들의 타입

### 1. Number Type

- 사칙연산 가능! (+, -, \*, /)

```js
let num1 = 27;
let num2 = 1.5;
let num3 = -20;

// 나머지를 구하는 연산도 가능함 -> 모듈러 연산이라고 부름
console.log(num1 % num2);
```

- 양의 무한대, 음의 무한대도 표현 가능함

```js
let inf = Infinity;
let mInf = -Infinity;
```

- NaN 선언 가능 (Not a Number)

```js
let nan = NaN;

console.log(1 * "hello");
// -> NaN
```

### 2. String Type

```js
let myName = "이정환";
let myLocation = "목동";
let introduce = myName + myLocation;
// -> 이정환목동

// 템플릿 리터럴 문법
let introduceText = `${myName}은 ${myLocation}에 거주합니다`;
// -> 이정환은 목동에 거주합니다
```

### 3. Boolean Type

```js
let isSwitchOn = true;
let isEmpty = false;
```

### 4. Null Type (아무것도 없다)

```js
let empty = null;
```

### 5. Undefined Type

- 선언 후 아무 값도 넣지 않았을 때
- 존재하지 않는 값을 불러오려고 할 때

```js
let none;
console.log(none);
```

# 형 변환 (Type Casting)

어떤 값의 타입을 다른 타입으로 변경하는 것

1. 묵시적 형 변환: 개발자가 직접 설정하지 않아도 JS가 알아서 형을 변환함 (암묵적 형 변환)
2. 명시적 형 변환: 개발자가 직접 함수 등을 이용해 형 변환을 일으킴

## 묵시적 형 변환

```js
let num = 10;
let str = "20";

const result = num + str;
// -> 1020
```

- 묵시적으로 num이 string으로 변환 됨!!

## 명시적 형 변환

- 프로그래머 내장함수 등을 이용해서 직접 형 변환을 명시

```js
// 문자열 -> 숫자
let str1 = "10";
let strToNum1 = Number(str1);

let str2 = "10개";
let strToNum2 = parseInt(str2);

// 숫자 -> 문자열
let num1 = 20;
let numToStr1 = String(num1);

console.log(numToStr1 + "입니다");
// -> 20입니다
```

> # 이제부터는 모르는 것만 기재하겠습니다 ..!!!ㅜㅜ

# 연산자

## 증강 연산자

```js
let num = 10;
num++;
console.log(num);
// -> 11
```

```js
let num = 10;
console.log(num++); // (후위연산)
// -> 10으로 촐력됨 바로 추가된 값을 원한다면...

console.log(++num); // num += 1 와 같음 (전위연산)
// 이렇게 하면 바로 추가된 값이 나옴! 마이너스로도 가능함
```

## 비교 연산자

```js
let comp1 = 1 === "1";
let comp2 = 1 !== 2;
```

- `=`을 3개나 사용하는 이유: 자료형까지 함께 비교할 수 있음!

## null 병합 연산자

존재하는 값을 추려내는 기능  
null, undefined가 아닌 값을 찾아내는 연산자

```js
let var1;
let var2 = 10;
let var3 = 20;

let var4 = var1 ?? var2; // 10
let var5 = var1 ?? var3; // 20
let var6 = var3 ?? var2; // 20 (처음 값)

let userName;
let userNickName = "Winterlood";

let displayName = userName ?? userNickName; // Winterlood
```

## typeof 연산자

값의 타입을 문자열로 반환하는 기능을 하는 연산자

```js
let var7 = 1;
var7 = "hello";
var7 = true;

let t1 = typeof var7;
console.log(t1); // string
```

## 삼항 연산자

항을 3개 사용하는 연산자  
조건식을 이용해서 참, 거짓일 때의 값을 다르게 반환

```js
let var8 = 10;

// 요구사항: 변수 res에 var8의 값이 짝수 -> "짝", 홀수 -> "홀"
let res = var8 % 2 === 0 ? "짝수" : "홀수";
console.log(res); // 짝수
```
