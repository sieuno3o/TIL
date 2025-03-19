# JavaScript 기초

## 변수와 상수

### 1. 변수

```js
let age = 27; // 선언 및 초기화 (초기화 하지 않아도 됨)
console.log(age);

age = 60;
console.log(age);
```

### 2. 상수

```js
const birth = "2003. 03. 22."; // 꼭 초기화 해야함! 재선언 불가
console.log(birth);
```

### 3. 변수 명명 규칙 (네이밍 규칙)

#### 3-1. $, \_ 제외한 기호는 사용할 수 없다.

```js
let $_name;
```

#### 3-2. 숫자로 시작할 수 없다.

```js
let name1;
let _2name;
```

#### 3-3. 예약어를 사용할 수 없다.

### 4. 변수 명명 가이드

```js
let salesCount = 1;
let refundCount = 1;
let totalSalesCount = salesCount - refundCount;
```

## 자료형

### 원시타입

- 기본형 타입이라고도 불림
- 프로그래밍에 있어 가장 기본적인 값들의 타입

#### 1. Number Type

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

#### 2. String Type

```js
let myName = "이정환";
let myLocation = "목동";
let introduce = myName + myLocation;
// -> 이정환목동

// 템플릿 리터럴 문법
let introduceText = `${myName}은 ${myLocation}에 거주합니다`;
// -> 이정환은 목동에 거주합니다
```

#### 3. Boolean Type

```js
let isSwitchOn = true;
let isEmpty = false;
```

#### 4. Null Type (아무것도 없다)

```js
let empty = null;
```

#### 5. Undefined Type

- 선언 후 아무 값도 넣지 않았을 때
- 존재하지 않는 값을 불러오려고 할 때

```js
let none;
console.log(none);
```

## 형 변환 (Type Casting)

어떤 값의 타입을 다른 타입으로 변경하는 것

1. 묵시적 형 변환: 개발자가 직접 설정하지 않아도 JS가 알아서 형을 변환함 (암묵적 형 변환)
2. 명시적 형 변환: 개발자가 직접 함수 등을 이용해 형 변환을 일으킴

### 묵시적 형 변환

```js
let num = 10;
let str = "20";

const result = num + str;
// -> 1020
```

- 묵시적으로 num이 string으로 변환 됨!!

### 명시적 형 변환

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

<br />

> # 이제부터는 모르는 것만 기재하겠습니다 ..!!!ㅜㅜ
>
> <br />

## 연산자

### 증강 연산자

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

### 비교 연산자

```js
let comp1 = 1 === "1";
let comp2 = 1 !== 2;
```

- `=`을 3개나 사용하는 이유: 자료형까지 함께 비교할 수 있음!

### null 병합 연산자

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

### typeof 연산자

값의 타입을 문자열로 반환하는 기능을 하는 연산자

```js
let var7 = 1;
var7 = "hello";
var7 = true;

let t1 = typeof var7;
console.log(t1); // string
```

### 삼항 연산자

항을 3개 사용하는 연산자  
조건식을 이용해서 참, 거짓일 때의 값을 다르게 반환

```js
let var8 = 10;

// 요구사항: 변수 res에 var8의 값이 짝수 -> "짝", 홀수 -> "홀"
let res = var8 % 2 === 0 ? "짝수" : "홀수";
console.log(res); // 짝수
```

## 반복문 복습

```js
for (let idx = 1; idx <= 10; idx++) {
  if (idx % 2 === 0) {
    continue;
  }
  console.log(idx);

  if (idx >= 5) {
    break;
  }
}
```

## 함수

```js
function getArea(width, height) {
  let area = width * height;
  return area;
}

let area1 = getArea(10, 20);
console.log(area1); // 200

let area2 = getArea(30, 20);
console.log(area2); // 600
```

선언 하지 않은 함수를 먼저 사용하고 뒤에 함수를 선언해도 잘 작동함!
JS의 호이스팅 기능때문... 끌어올리다 라는 뜻

```js
function getArea(width, height) {
  function another() {
    // 중첩 함수
    console.log("another");
  }

  another();
  let area = width * height;

  return area;
}

let area1 = getArea(10, 20);
console.log(area1);
// another
// 200
```

## 함수 표현식과 화살표 함수

### 함수 표현식

```js
function funcA() {
  console.log("funcA");
}

let varA = funcA;
console.log(varA);
// 함수가 그대로 출력됨 ;; ㄷㄷ
```

```js
// 익명함수
let varB = function () {
  console.log("funcB");
};

varB(); // 호이스팅 불가능 !!
// funcB
```

### 화살표 함수

```js
let varH = () => 1;
console.log(varH());
// 1

let varC = (value) => {
  console.log(value);
  return value + 1;
};

console.log(varC(10));
// 11
```

## 콜백 함수

### 콜백함수

```js
function main(value) {
  value();
}

function sub() {
  console.log("i am sub");
}
main();
// 위 함수와 아래 함수는 동일함!
main(() => {
  console.log("i am sub");
});

// 출력은 두개 다 i am sub로 나옴
```

### 콜백함수의 활용

```js
function repeat(count, callback) {
  for (let idx = 1; idx <= count; idx++) {
    callback(idx);
  }
}

repeat(5, (idx) => {
  console.log(idx);
});

repeat(5, (idx) => {
  console.log(idx \* 2);
});

repeat(5, (idx) => {
  console.log(idx \* 3);
});
```

## 스코프

전역(전체 영역) 스코프 / 지역(특정 영역) 스코프

- 전역 스코프 : 전체 영역에서 접근 가능
- 지역 스코프 : 특정 영역에서만 접근 가능

```js
let a = 1; // 전역 스코프

function funcA() {
  let b = 2; // 지역 스코프
  console.log(a);
}

funcA();

if (true) {
  let c = 1;
}

for (let i = 0; i < 10; i++) {
  let d = 1;
}

console.log(b);
// b is not definded
// c나 d도 마찬가지!
```

함수 선언식은 함수 안에서만 지역 스코프가 되고, 반복문이나 if문은 전역임!

## 객체

### 1. 객체 생성

```js
let obj1 = new Object(); // 객체 생성자
let obj2 = {}; // 객체 리터럴 (대부분 사용)
```

### 2. 객체 프로퍼티 (객체 속성)

Value에는 값이든 속성으로 들어올 수 있음 (문자, 숫자, 함수, 객체...)
Key에 띄어쓰기를 포함하고 싶을 경우 " " 붙여줘야 됨

```js
let person = {
  name: "이정환",
  age: 27,
  hobby: "테니스",
  job: "FE Developer",
  extra: {},
  10: 20,
  "like cat": true,
};
```

### 3. 객체 프로퍼티를 다루는 방법

#### 3.1 특정 프로퍼티에 접근 (점 표기법, 괄호 표기법)

```js
let name = person.name;
console.log(name); // 이정환

let age = person["age"];
console.log(age); // 27

let property = "hobby";
let hobby = person[property];
console.hobby(hobby); //테니스
```

#### 3.2 새로운 프로퍼티를 추가하는 방법

```js
person.job = "fe developer";
person["favoriteFood"] = "떡볶이";
```

#### 3.3 프로퍼티를 수정하는 방법

```js
person.job = "educator";
person["favoriteFood"] = "초콜릿";
```

#### 3.4 프로퍼티를 삭제하는 방법

```js
delete person.job;
delete person["favoriteFood"];
```

#### 3.5 프로퍼티의 존재 유무를 확인하는 방법 (in 연산자)

```js
let result2 = "cat" in person;
console.log(result2); // false
```

### 4. 상수 객체

아예 새로운 값을 할당 하는건 불가능 하지만, 추가나 수정 삭제는 가능함

```js
const animal = {
  type: "고양이",
  name: "나비",
  color: "black",
};

animal.age = 2; // 추가
animal.name = "까망이"; // 수정
delete animal.color; // 삭제
```

### 5. 메서드

값이 함수인 프로퍼티

```js
const person = {
  name: "이정환",
  // 메서드 선언
  sayHi() {
    console.log("안녕!");
  },
  sayBy: function () {
    console.log("잘가!");
  },
  sayTy: () => {
    console.log("고마워!");
  },
};

person.sayHi();
person["sayHi"]();
```

## 배열

### 1. 배열 생성

```js
let arrA = new Array(); // 배열 생성자
let arrB = []; // 배열 리터럴 (대부분 사용)

let arrC = [1, 2, 3, true, "hello", null, undefined, () => {}, {}, []];
```

### 2. 배열 요소 접근

```js
let item1 = arrC[0];
let item2 = arrC[1];

arrC[0] = "hello";
console.log(arrC);
```
