## Description
- https://webhacking.kr/challenge/js-2

- When you initially access this site, you will see an "Access Denied" alert.

- So the first thing we should do is look at the source code.

- You can view the source code in the browser by using view-source: followed by the URL.

- Here is the code I found:
```html
<html>
<head>
<title>Challenge 15</title>
</head>
<body>
<script>
  alert("Access_Denied");
  location.href='/';
  document.write("<a href=?getFlag>[Get Flag]</a>");
</script>
</body>
```

Did you see the key point? Yes! You can solve this challenge by accessing the URL:
https://webhacking.kr/challenge/js-2?getFlag

Accessing the above link will let you solve the challenge.


