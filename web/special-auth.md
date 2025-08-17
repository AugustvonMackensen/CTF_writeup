## Question

Access the link and get the flag

## Description

When you access the link, you get "Unauthorized".
After checking the file, I found the following nginx.conf:

```conf
user www-data;
events {
	worker_connections 768;
}

http{
        server{
                listen 80 default_server;
                server_name _;
                location / {
                        return 504 "unauthorized";
                }
                
        }
        server {
                listen 80;
                server_name kr.admin.0;
                location /flag {
                        return 200 "H4CGM{NotFlag}";
                }
        }
}
```
From this configuration, the flag can be accessed only when the server_name is set to kr.admin.0.

To do this, open WSL or a Windows command prompt and run:

```bash
curl http://web.h4ckingga.me:20007/flag -H "Host: kr.admin.0"
```

then you can get the flag!
