## Description

```html 
<script>alert('old-14 Pwned!');</script><hr>old-14 Pwned. You got 10point. Congratz!<hr><html>
<head>
<title>Challenge 14</title>
<style type="text/css">
body { background:black; color:white; font-size:10pt; }
</style>
</head>
<body>
<br><br>
<form name=pw onsubmit="ck();return false"><input type=text name=input_pwd><input type=button value="check" onclick=ck()></form>
<script>
function ck(){
  var ul=document.URL;
  ul=ul.indexOf(".kr");
  ul=ul*30;
  if(ul==pw.input_pwd.value) { location.href="?"+ul*pw.input_pwd.value; }
  else { alert("Wrong"); }
  return false;
}
</script>
</body>
</html>
```

1. You must press F12 and access to console
2. Check out document.URL
3. Find out where ".kr" starts
4. mutiply the index of "." to 30
5. input the value then you pwned the question