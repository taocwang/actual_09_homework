def nginx_config(filename,ngdict):
    ngtemplate = '''
    server {{
        listen {port} {server};
        server_name {servername};
        access_log {access_log} main;
        location / {{
            root  {home};
            index index.htm index.html;
            proxy_pass http://127.0.0.1:{proxy_port};

        }}
    }}
    '''.format(port=ngdict['port'],server=ngdict['server'],)
