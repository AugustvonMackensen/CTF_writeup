## Description

Let's take a look at the code

```html
<html>
<head>
<title>Challenge 54</title>
</head>
<body>
<h1><b>Password is <font id=aview></font></b></h1>
<script>
function run(){
  if(window.ActiveXObject){
   try {
    return new ActiveXObject('Msxml2.XMLHTTP');
   } catch (e) {
    try {
     return new ActiveXObject('Microsoft.XMLHTTP');
    } catch (e) {
     return null;
    }
   }
  }else if(window.XMLHttpRequest){
   return new XMLHttpRequest();
 
  }else{
   return null;
  }
 }
x=run();
function answer(i){
  x.open('GET','?m='+i,false);
  x.send(null);
  aview.innerHTML=x.responseText;
  i++;
  if(x.responseText) setTimeout("answer("+i+")",20);
  if(x.responseText=="") aview.innerHTML="?";
}
setTimeout("answer(0)",1000);
</script>
</body>
</html>
```

Oh, It shows that I can got a letter for the answer during 20 seconds.
So, I will write the code for console.

```javascript
var answer ="";

for(var i=0; i<38; i++){
    x.open('GET','?m='+i,false);
    x.send(null);
    answer += x.responseText
}

console.log(answer);
```

then you can get the flag. so Copy and paste it into Auth