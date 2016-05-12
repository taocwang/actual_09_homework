server
{{
    listen       {port};
    server_name  {server};
    index index.html index.htm index.php;
    root  {root_path};
    access_log  {log_path}/access.log;
    error_log  {log_path}/access_error.log;
}}
