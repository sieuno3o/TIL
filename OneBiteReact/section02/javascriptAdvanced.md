# JavaScript 심화

## Truthy & Falsy

### 1. Falsy한 값

```js
let f1 = undefined;
let f2 = null;
let f3 = 0;
let f4 = -0;
let f5 = NaN;
let f6 = "";
let f7 = 0n;
```

### 2. Truthy 한 값

7가지 Falsy 한 값들 제외한 나머지 모든 값

```js
let t1 = "hello";
let t2 = 123;
let t3 = [];
let t4 = {};
let t5 = () => {};
```

### 3. 활용 사례

```js
function printName(person) {
  if (!person) {
    console.log("person의 값이 없음");
    return;
  }
  console.log(person.name);
}

let person = { name: "이정환" };
printName(person);
```

## 단락 평가

```js
function printName(person) {
  const name = person && person.name;
  console.log(name || "person의 값이 없음");
}

printName();
printName({ name: "이정환" });
```

앞에 것만 보고 확정지은 후 뒤에 것에는 접근조차 하지 않는 것... 그것이 JS의 단락평가  
첫번째 피연산자만 보고도 연산 결과를 확정할 수 있다면 뒤에 있는 피연산자에는 접근조차 하지 않음 ㄷㄷ  
Truthy한 값 && Truthy한 값을 했을 때 왜 뒤에거가 출력 되는거지 ???

## 구조 분해 할당

### 1. 배열의 구조 분해 할당

```js
let arr = [1, 2, 3];

let [one, two, three, four = 4] = arr;
// four에 값을 할당하지 않은 경우 undefined로 출력됨
```

### 2. 객체의 구조 분해 할당

```js
let person = {
  name: "이정환",
  age: 27,
  hobby: "테니스",
};

let { age: myAge, hobby, name, extra = "hello" } = person;
```

### 3. 객체 구조 분해 할당을 이용해서 함수의 매개변수를 받는 방법

```js
const func = ({ name, age, hobby, extra }) => {
  console.log(name, age, hobby, extra);
};

func(person);
// 이정환 27 테니스 undefined
```

## Spread 연산자

Spread : 흩뿌리다, 펼치다 라는 뜻
객체나 배열에 저장된 여러개의 값을 개별로 흩뿌려주는 역할

```js
let arr1 = [1, 2, 3];
let arr2 = [4, arr1[0], arr1[1], arr1[2], 5, 6];
let arr3 = [4, ...arr1, 5, 6];
// arr2 == arr3

let obj1 = {
  a: 1,
  b: 2,
};
let obj2 = {
  ...obj1,
  // a: obj1.a,
  // b: obj1.b,
  c: 3,
  d: 4,
};

function funcA(p1, p2, p3) {
  console.log(p1, p2, p3);
}

funcA(...arr1); // 1 2 3
```

## Rest 매개변수

Rest는 나머지, 나머지 매개변수
... 뒤에 아무 이름으로 붙이면 됨
rest 매개변수가 제일 뒤에 와야됨!

```js
function funcB(one, two, ...rest) {
  console.log(rest);
}

funcB(...arr1);
```
