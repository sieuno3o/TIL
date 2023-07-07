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
    ul li{ //조상 자손 선택자
      color:red;
    }
    #lecture>li{ //부모 자식 선택자
      border:1px solid red;
    }
    ul,ol{ //ui, oi 동시선택
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
  a:link{ //방문하지 않은 사이트
    color:black;
  }
  a:visited{ //방문한 사이트 빨간색
    color:red;
  }
  a:hover{ //커서 올렸을 때 노란색
    color:yellow;
  }
  a:active{ //누른 상태에서 초록색
    color:green;
  }
  input:focus{ //탭 눌럿을 때.. 어쩌구.. 무조건 맨 뒤에 적어줘야함
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

## 속성 - 타이포그래피
