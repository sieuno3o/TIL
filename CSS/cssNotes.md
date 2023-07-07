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
