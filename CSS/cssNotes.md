# CSS (Cascading Style Sheets)

## HTML에 CSS 적용방법 2가지

스타일 -> head에 작성해야함

```css
<style>
  h1{
    color:blue;
    text-decoration:underline;
  }
</style>
```

```css
<h1 style = "color:red">Hello World</h1>
```

<br>

## 선택자 종류

중복되는 선택자가 존재할 경우 id 대신 class 사용

```css
<style>
    #select{
      font-size:50px;
    }
    .deactive{
      text-decoration: line-through;
    }
</style>
<ul>
    <li class="deactive">HTML</li>
    <li id="select">CSS</li>
    <li class="deactive">JavaScript</li>
</ul>
```

### 부모 자식 선택자

```css
<head>
  <style>
    ul li{      /* 조상 자손 선택자 */
      color:red;
    }
    #lecture>li{/* 부모 자식 선택자 */
      border:1px solid red;
    }
    ul,ol{      /* ui, oi 동시선택 */
      background-color: powderblue;
    }
</style>
</head>
<body>
  <ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
  </ul>
  <ol id="lecture">
    <li>HTML</li>
    <li>CSS
      <ol>
        <li>selector</li>
        <li>declaration</li>
      </ol>
    </li>
    <li>JavaScript</li>
  </ol>
</body>
```

### 가상 클래스 선택자

css는 뒤에 나오는 코드를 우선으로 실행

```css
<style>
  a:link{       /* 방문하지 않은 사이트 */
    color:black;
  }
  a:visited{    /* 방문한 사이트 빨간색 */
    color:red;
  }
  a:hover{      /* 커서 올렸을 때 노란색 */
    color:yellow;
  }
  a:active{     /* 누른 상태에서 초록색 */
    color:green;
  }
  input:focus{  /* 탭 눌럿을 때.. 어쩌구.. 무조건 맨 뒤에 적어줘야함 */
    background-color:black;
    color:white;
  }
</style>
  <a href = "사이트"> 방문함 </a>
  <a href = "사이트2"> 방문안함</a>
  <input type = "text">
```

### 추가 선택자

[게임으로 선택자 공부하기](https://flukeout.github.io/)

```
* 모든 것 선택
+ 옆에 있는 것 하나 선택
~ 여러개 동시에 선택
> 오른쪽 바로 밑에 있는 왼쪽만 선택
child-first 첫번째로 등장하는 것만 선택
...
무수히 많음 ㅠ ㅠ 게임으로 공부해보고 검색도 해보고 하기...
```

<br>

## 타이포그래피

### font-size

- px 폰트 크기 절대적
- em, rem 폰트 크기 상대적 (사용자의 설정에 따라 바뀜)
  - 결론적으로 오늘날은 rem을 사용

### color

1. color name
2. hex
3. rgb

[컬러 지정 방법](https://www.w3schools.com/css/css_colors.asp)

### text-align

```css
<style>
  p{
    text-align: left;      /* 왼쪽 정렬 */
    text-align: center;    /* 가운데 정렬 */
    text-align: right;     /* 오른쪽 정렬 */
    text-align: justify;   /* 오른쪽 왼쪽 공백 없이... */
    bolder:1px solid gray; /* 테두리 1px 회색 */
  }
</style>
```

### font

#### font-family

- 띄어쓰기가 있는 경우 큰 따옴표로 묶어줌
- h1 태그의 font를 Times New Roman로 지정, 사용자의 컴퓨터에 폰트가 없다면 Times 사용, Times도 없다면 serif 사용.

```css
h1 {
  font-family: "Times New Roman", Times, serif;
}
```

#### font-weight

- 폰트 두껍게 표시

```css
h1 {
  font-weight: bold;
}
```

#### line-height

- 행 간격 표시. 기본 행 간격 1.2

```css
p {
  line-height: 1.3;
}
```

#### 축약

```css
<style>
  #type1{
    font-size:5rem;
    font-family: arial, verdana, "Helvetica Neue", serif;
    font-weight: bold;
    line-height: 2;
  }
  #type2{
    font:bold 5rem/2 arial, verdana, "Helvetica Neue", serif;
  }
</style>
```

<br>

## 상속

```css
<style>
  html{color:red;}
  #select{color:black;}
  body{border:1px solid red;}
</style>
<body>
  <ul>
    <li>html</li>
    <li>css</li>
    <li id="select">javascript</li>
  </ul>
</body>
```

html의 색을 red로 지정 -> 모든 글자 색 red  
하지만 select id를 가진 속성값만 black으로 표시.

[상속하는 속성과 상속하지 않는 속성](https://www.w3.org/TR/CSS21/propidx.html)

<br>

## Cascading
