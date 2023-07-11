# JavaScript

## JavaScript와 HTML
### 차이점
```html
<h1>html</h1>
1+1
```
```
출력결과: 1+1
```
___

```html
<script>
  document.write(1+1);
</script>
```
```
출력결과: 2
```
html은 정적, js는 동적

<br>

### EVENT 
웹 브라우저에서 일어나는 사건, 이벤트...
```html
<input type = "botton" value = "hi" onclick = "alert('hi')">
```
html에 아래 내용으로 기재된 바 있음
1.  onclick의 속성값에는 반드시 js가 와야함
2. onclick 속성의 속성값은 웹 브라우저가 기억하고 있다가 onclick이 위치하고 있는 태그에 클릭 시 기억하고 있는 js코드를 js 문법에 따라 해석해서 그대로 동작할 것

## 데이터 타입
기존과 비슷함  
문자열 String, 숫자는 Number, Boolean...

<br>

## 변수와 대입연산자
변수 할당 똑같음  

### 대입연산자
```
var name = "id"
"apple banana icecream "+name+" orange"
```
```
apple banana icecream id orange
```