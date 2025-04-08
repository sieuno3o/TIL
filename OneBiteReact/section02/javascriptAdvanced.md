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

## 배열 순회

### for of 반복문

```js
let arr = [1, 2, 3];
for (let item of arr) {
  console.log(item);
}
```

## 객체 순회

```js
let person = {
  name: "이정환",
  age: 27,
  hobby: "테니스",
};
```

### 1. Object.keys 사용

객체에서 key 값들만 뽑아서 새로운 배열로 반환

```js
let keys = Object.keys(person);

for (let key of keys) {
  const value = person[key];
  console.log(key, value);
}
```

### 2. Object.values

객체에서 value 값들만 뽑아서 새로운 배열로 반환

```js
let values = Object.values(person);

for (let value of values) {
  console.log(value);
}
```

### 3. for in

```js
for (let key in person) {
  const value = person[key];
  console.log(key, value);
}
```

> **배열를 순회할 때는 for of, 객체를 순회할 떄는 for in!!!**

## 배열 요소 조작 메서드

### 1. push

push는 push되고 나면 해당 배열을 길이를 반환해줌... ㄷㄷ

```js
let a = [1, 2];
const length = push.a(3, 4);
console.log(length); // 4
```

### 2. pop

```js
let arr2 = [1, 2, 3];
const poppedItem = arr2.pop(); // 3
```

### 3. shift

맨 앞을 제거 반환

```js
let arr2 = [1, 2, 3];
const poppedItem = arr2.shift(); // 1
```

### 4. unshift

배열의 맨 앞에 새로운 요소를 추가하는 메서드

```js
let arr4 = [1, 2, 3];
const newLength2 = arr4.unshift(0);
```

shift와 unshift는 push pop보다 느리게 동작함

### 5. slice

배열의 특정 범위를 잘라내서 새로운 배열로 반환

```js
let arr5 = [1, 2, 3, 4, 5];
let sliced = arr5.slice(2, 5); // 3 4 5
let sliced2 = arr5.slice(2); // 3 4 5
let sliced3 = arr5.slice(-3); // 3 4 5
```

### 6. concat

두개의 서로 다른 배열을 이어 붙여서 새로운 배열을 반환

```js
let arr6 = [1, 2];
let arr7 = [3, 4];

let concatedArr = arr6.concat(arr7); // 1, 2, 3, 4
```

# 순회 및 탐색 메서드

## 1. forEach

모든 요소를 순회하면서, 각각의 요소에 특정 동작을 수행시키는 메서드

```js
let arr1 = [1, 2, 3];

arr1.forEach(function (item, idx, arr) {
  console.log(idx, item * 2);
  // 0 2
  // 1 4
  // 2 6
});

let doubledArr = [];

arr1.forEach((item) => {
  doubledArr.push(item * 2);
});

// doubledArr 의 값: 2, 4, 6
```

## 2. includes

배열에 특정 요소가 있는지 확인하는 그런 메서드

```js
let arr2 = [1, 2, 3];
let isInclude = arr2.includes(10); // false
```

## 3. indexOf

특정 요소의 인덱스(위치)를 찾아서 반환하는 메서드

```js
let arr3 = [2, 2, 2];
let index = arr3.indexOf(2); // 0
let index = arr3.indexOf(20); // -1

// let objectArr = [
//   { name: "이정환" },
//   { name: "홍길동" },
// ];

// console.log(
//   objectArr.indexOf({ name: "이정환" })
// );

// console.log(
//   objectArr.findIndex(
//     (item) => item.name === "이정환"
//   )
// );
```

## 4. findIndex

모든 요소를 순회하면서, 콜백함수를 만족하는 그런
특정 요소의 인덱스(위치)를 반환하는 메서드

```js
let arr4 = [1, 2, 3];
const findedIndex = arr4.findIndex((item) => item === 999);

console.log(findedIndex);
```

## 5. find

모든 요소를 순회하면서 콜백함수를 만족하는 요소를 찾는데, 요소를 그대로 반환

```js
let arr5 = [{ name: "이정환" }, { name: "홍길동" }];

const finded = arr5.find((item) => item.name === "이정환");

console.log(finded);
```
