# Challenge 10 Write-up

## Description

1. You need to register at [https://webhacking.kr](https://webhacking.kr)  
2. The challenge is **Challenge 10**  
3. The link is [https://webhacking.kr/challenge/code-1](https://webhacking.kr/challenge/code-1)  

If you open the Developer Tools by pressing **F12**, you can see the following code:

```html
<html>
<head>
<title>Challenge 10</title>
</head>

<body>
<hr style="height:100;background:brown;">
<table border=0 width=1800 style="background:gray">
<tr><td>
<a id="hackme" style="position:relative;left:0;top:0" onclick="this.style.left=parseInt(this.style.left,10)+1+'px';if(this.style.left=='1600px')this.href='?go='+this.style.left" onmouseover="this.innerHTML='yOu'" onmouseout="this.innerHTML='O'">O</a><br>
<font style="position:relative;left:1600;top:0" color=gold>|<br>|<br>|<br>|<br>Goal</font>
</td></tr>
</table>
<hr style="height:100;background:brown;">
</body>
</html>
```

## Attempt 1 — Direct HTML Editing
I first tried editing the HTML directly, but the result was "no hack".


## Attempt 2 - Using Jquery
Instead, I opened the Developer Tools, went to the Console, and adjusted the style using jQuery:

```javascript
$('a#hackme').style.left=1599
```

After doing that, I got the point and solved the challenge.