# JavaScript

## JavaScript와 HTML
### 차이점
```html
<h1>html</h1>
1+1
```
```
1+1
```
___

```html
<script>
  document.write(1+1);
</script>
```
```
2
```
html은 정적, js는 동적  
JS는 HTML과 마찬가지로 컴퓨터 언어이지만, 컴퓨터 프로그래밍 언어이기도 함.  
시간의 순서에 따라 실행되어야 할 기능을 프로그래밍 언어의 문법에 맞게 글로 적어두는 것이 중요함. (프로그래밍)  
html은 웹페이지를 묘사하는 언어이기에 시간의 순서에 따라 일을 할 필요가 없기 떄문에 차이가 있음. 

### EVENT 
웹 브라우저에서 일어나는 사건, 이벤트...
```html
<input type = "botton" value = "hi" onclick = "alert('hi')">
```
html에 아래 내용으로 기재된 바 있음
1. onclick의 속성값에는 반드시 js가 와야함
2. onclick 속성의 속성값은 웹 브라우저가 기억하고 있다가 onclick이 위치하고 있는 태그에 클릭 시 기억하고 있는 js코드를 js 문법에 따라 해석해서 그대로 동작할 것

<br>

## 데이터 타입
기존과 비슷함  
문자열 String, 숫자는 Number, Boolean...

<br>

## 변수와 연산자
변수 할당 똑같음  

### 대입연산자
```
var name = "id"
"apple banana icecream "+name+" orange"
```
```
apple banana icecream id orange
```

* 연산자 ===  
  * 값 뿐만 아니라 자료형까지 같아야 true (반대는 !== 자료형까지 달라야 함) 

<br>

## 제어할 태그 선택하기

```html
document.querySelector('.apple').style.color = "black";
```
apple 이름의 class 글자 색이 검정색으로 바뀜. 

<br>

## Refactoring 중복의 제거
```html
<input id="night_day" type="button" value="night" onclick="
  if(document.querySelector('#night_day').value === 'night'){
    document.querySelector('body').style.backgroundColor = 'black';
    document.querySelector('body').style.color = 'white';
    document.querySelector('#night_day').value = 'day';
  } else {
    document.querySelector('body').style.backgroundColor = 'white';
    document.querySelector('body').style.color = 'black';
    document.querySelector('#night_day').value = 'night';
  }
">
```
```html
<input type="button" value="night" onclick="
  var target = document.querySelector('body');
  if(this.value === 'night'){
    target.style.backgroundColor = 'black';
    target.style.color = 'white';
    this.value = 'day';
  } else {
    target.style.backgroundColor = 'white';
    target.style.color = 'black';
    this.value = 'night';
  }
">
```

<br>

## 배열

```html
<h2>Syntax</h2>
<script>
  var coworkers = ["egoing", "leezche"]; /* 배열생성 */
</script>

<h2>get</h2>
<script>
  document.write(coworkers[0]); /* 배열 [번째] 출력 */
  document.write(coworkers[1]);
</script>

<h2>add</h2>
<script>
  coworkers.push('duru'); /* 배열에 추가 */
  coworkers.push('taeho');
</script>

<h2>count</h2>
<script>
  document.write(coworkers.length); /* 배열 개수 */
</script>
```
[배열 관련 메서드](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array)

<br>

## 배열 반복문 활용
```html
<script>
  var alist = document.querySelectorAll('a');
  var i = 0;
  while(i < alist.length){
    alist[i].style.color = 'blue';
    i = i + 1;
}
</script>
```
<br>

## 함수
```html
<script>
  function onePlusOne(){
    document.write(1+1+'<br>');
  }
  onePlusOne();
  function sum(left, right){
    document.write(left+right+'<br>');
  }
  function sumColorRed(left, right){
    document.write('<div style="color:red">'+(left+right)+'</div><br>');
  }
  sum(2,3); // 5
  sumColorRed(2,3); // 5
</script>

<h2>Return</h2>
<script>
  function sum2(left, right){ 
    return left+right;
  }
  document.write(sum2(2,3)+'<br>');
  document.write('<div style="color:red">'+sum2(2,3)+'</div>');
  document.write('<div style="font-size:3rem;">'+sum2(2,3)+'</div>');
</script>
```

<br>



