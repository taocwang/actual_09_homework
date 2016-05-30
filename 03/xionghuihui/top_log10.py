#a='61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"'
line_dict={}

line = open('www_access.log','r')
for i in line:
    b= i.split(' ')
    key = (b[0],b[6],b[8])
    line_dict[key] = line_dict.get(key,0) + 1
 #   key = (ip,url,code)
  #  if key not in line_dict:
   #     line_dict[key] = 0
   # line_dict[key] += 1
line.close()
#print line_dict
line_list = line_dict.items()

#[(key,value),(key,value)]
for j in range(10):
  for i in range(len(line_list) - 1):
      if line_list[i][1] > line_list[i + 1][1]:
          temp = line_list[i]
          line_list[i] = line_list[i + 1]
          line_list[i + 1] = temp
html=open('top_log.txt','w')
#print line_list[-1:-11:-1]
for node in line_list[-1:-11:-1]:
   html.write('%s %s %s %s \n' % (node[1],node[0][0],node[0][1],node[0][2]))
html.close()

html1='''
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'/>
        <title>{biaoti}</title>
    </head>
    <body>
        <table>
             <trade>
                  <tr>
                    {kaitou}
                  </tr>
             </thead>
             <tbody>
                  <tr>
                    {ruilong}
                  </tr>
             </tbody>
        </table>
    </body>
</html>
'''
biaoti='top_10'
kaitou='<th>cishu</th><th>IP</th><th>URL</th><th>Code</th>'
ruilong=''

html2=open('top_log10.html','w')
for node in line_list[-1:-11:-1]:
   ruilong +='<tr><td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>' % (node[1],node[0][0],node[0][1],node[0][2])
html2=open('top_log10.html','w')
html2.write(html1.format(biaoti=biaoti,kaitou=kaitou,ruilong=ruilong))
html2.close()
