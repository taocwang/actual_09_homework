port = 80
servername = 'test.com'
access_log = 'test.log'
home = '/home/test'
proxy_port = 8080

handle = open('nginx.template1','r')
rf = handle.read().format(port=port,servername=servername,access_log=access_log,home=home,proxy_port=proxy_port)
handle.close()


handlewr = open('nnginx.conf1','w')
handlewr.write(rf)
handlewr.close()

#handle.close()
#print nginxfile.format(port=port,servername=servername,access_log=access_log,home=home,proxy_port=proxy_port)
