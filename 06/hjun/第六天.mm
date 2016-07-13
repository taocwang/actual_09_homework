<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1465023948025" ID="ID_1187997553" MODIFIED="1465024139484" TEXT="&#x7b2c;&#x516d;&#x5929;">
<node CREATED="1465024142633" ID="ID_751838730" MODIFIED="1465025845256" POSITION="right" TEXT="session">
<node CREATED="1465024316962" ID="ID_1003019724" MODIFIED="1465024331538" TEXT="&#x4ec0;&#x4e48;&#x662f;session">
<node CREATED="1465024187497" ID="ID_129548998" MODIFIED="1465024235018" TEXT="&#x6d4f;&#x89c8;&#x5668;&#x8bf7;&#x6c42;&#x670d;&#x52a1;&#x5668;&#xff0c;&#x670d;&#x52a1;&#x5668;&#x5206;&#x914d;&#x7684;&#x4e00;&#x5757;&#x5185;&#x5b58;&#x5b58;&#x50a8;&#x7a7a;&#x95f4;"/>
</node>
<node CREATED="1465024170337" ID="ID_1617390072" MODIFIED="1465024186050" TEXT="sessionID">
<node CREATED="1465024352339" ID="ID_1735652083" MODIFIED="1465024513574" TEXT="&#x6bcf;&#x4e00;&#x4e2a;&#x5ba2;&#x6237;&#x7aef;&#x8bf7;&#x6c42;&#x90fd;&#x4f1a;&#x5206;&#x914d;&#x4e00;&#x4e2a;&#x5c5e;&#x4e8e;&#x81ea;&#x5df1;&#x7684;session&#xff0c;sessionID&#x548c;session&#x5b58;&#x50a8;&#x7a7a;&#x95f4;&#x4e00;&#x4e00;&#x5bf9;&#x5e94;,&#x7c7b;&#x4f3c;&#x4e8e;&#x8fd9;&#x5757;session&#x5b58;&#x50a8;&#x7a7a;&#x95f4;&#x7684;&#x94a5;&#x5319;"/>
</node>
<node CREATED="1465025856269" ID="ID_91690709" MODIFIED="1465025903691" TEXT="flask&#x5bfc;&#x5165;session&#x51fd;&#x6570;">
<node CREATED="1465025920273" ID="ID_1785287969" MODIFIED="1465025939148" TEXT="from flask import session"/>
</node>
<node CREATED="1465025984710" ID="ID_862517545" MODIFIED="1465025995942" TEXT="session&#x52a0;&#x5bc6;">
<node CREATED="1465025998005" ID="ID_1748949569" MODIFIED="1465026081985" TEXT="&#x4f7f;&#x7528;python&#x751f;&#x6210;&#x7684;&#x968f;&#x65f6;&#x6570;&#x8fdb;&#x884c;&#x52a0;&#x5bc6;">
<node CREATED="1465026082987" ID="ID_634419933" MODIFIED="1465026439945" TEXT="import os&#xa;app = Flask(__name__)  #&#x5b9e;&#x4f8b;&#x5316;Flask&#x7c7b;&#x5b9e;&#x4f8b;&#x540d;&#x4e3a;app, &#x5728;&#x7b2c;&#x4e94;&#x8282;&#x65f6;&#x5df2;&#x7ecf;&#x521b;&#x5efa;.&#xa;app.secret_key = os.urandom(32)"/>
</node>
</node>
<node CREATED="1465025541256" ID="ID_447104168" MODIFIED="1465025551992" TEXT="session&#x5b58;&#x503c;">
<node CREATED="1465025553411" ID="ID_171104831" MODIFIED="1465025598041" TEXT="session[&apos;session_name&apos;] = session_value">
<node CREATED="1465027297511" ID="ID_437684867" MODIFIED="1465027327217" TEXT="session[&apos;user&apos;] = {&apos;username&apos;: username}"/>
<node CREATED="1465027110929" ID="ID_1593813341" MODIFIED="1465027157572" TEXT="session&#x7c7b;&#x4f3c;&#x4e8e;dict&#x7c7b;&#x578b;,&#x5b58;&#x53d6;&#x503c;&#x7684;&#x65b9;&#x6cd5;&#x7c7b;&#x4f3c;&#x4e8e;dict"/>
</node>
</node>
<node CREATED="1465027337128" ID="ID_1532454046" MODIFIED="1465027345908" TEXT="session&#x53d6;&#x503c;">
<node CREATED="1465027347035" ID="ID_614585023" MODIFIED="1465029024486" TEXT="print session">
<node CREATED="1465029087568" ID="ID_707699049" MODIFIED="1465029101967" TEXT="&#x4f7f;&#x7528;print&#x6253;&#x5370;session&#x5185;&#x7684;&#x6240;&#x6709;&#x4fe1;&#x606f;"/>
</node>
<node CREATED="1465029025107" ID="ID_754476225" MODIFIED="1465029082603" TEXT="session.get(&apos;user&apos;)">
<node CREATED="1465029104543" ID="ID_790288318" MODIFIED="1465029157687" TEXT="session&#x7c7b;&#x4f3c;&#x4e8e;dict&#x7c7b;&#x578b;&#xff0c;&#x53ef;&#x4ee5;&#x4f7f;&#x7528;get(&apos;user&apos;)&#x83b7;&#x53d6;value&#x7684;&#x503c;"/>
</node>
</node>
<node CREATED="1465025602442" ID="ID_1035690630" MODIFIED="1465029178832" TEXT="session&#x6e05;&#x9664;">
<node CREATED="1465029179667" ID="ID_1675873370" MODIFIED="1465029194406" TEXT="session.clean()">
<node CREATED="1465029195411" ID="ID_1031787049" MODIFIED="1465029230528" TEXT="&#x540c;&#x6837;dict&#x7c7b;&#x578b;&#x7684;clean()&#x529f;&#x80fd;&#x5728;session&#x4e2d;&#x4e5f;&#x540c;&#x6837;&#x9002;&#x7528;"/>
</node>
</node>
<node CREATED="1465029297934" ID="ID_1132712052" MODIFIED="1465029302697" TEXT="session&#x8fc7;&#x671f;">
<node CREATED="1465029304074" ID="ID_72382686" MODIFIED="1465029455953" TEXT="&#x5f53;&#x6d4f;&#x89c8;&#x5668;&#x5173;&#x95ed;&#x65f6;,session&#x503c;&#x81ea;&#x52a8;&#x6e05;&#x9664;"/>
</node>
<node CREATED="1465025407950" ID="ID_1502492397" MODIFIED="1465025427582" TEXT="&#x7528;&#x4e8e;&#x8eab;&#x4efd;&#x8ba4;&#x8bc1;">
<node CREATED="1465025428748" ID="ID_618513586" MODIFIED="1465025473123" TEXT="&#x7528;&#x6237;&#x8ba4;&#x8bc1;&#x6210;&#x529f;&#xff0c;&#x8bbe;&#x7f6e;session&#x503c;"/>
<node CREATED="1465025505779" ID="ID_917836204" MODIFIED="1465025537957" TEXT="&#x7528;&#x6237;&#x9000;&#x51fa;&#x767b;&#x9646;,&#x5220;&#x6389;session&#x503c;"/>
</node>
</node>
<node CREATED="1465024267409" ID="ID_1520138377" MODIFIED="1465024532796" POSITION="right" TEXT="cookie">
<node CREATED="1465024536855" ID="ID_326229591" MODIFIED="1465024601220" TEXT="session&#x5b58;&#x50a8;&#x4e8e;&#x670d;&#x52a1;&#x5668;,cookie&#x5b58;&#x4e8e;&#x5ba2;&#x6237;&#x7aef;&#x5982;&#x6d4f;&#x89c8;&#x5668;.&#x7528;&#x4e8e;&#x5b58;&#x653e;&#x670d;&#x52a1;&#x5668;&#x8fd4;&#x56de;&#x7684;&#x4fe1;&#x606f;&#x5982;&#x5b58;&#x653e;&#x670d;&#x52a1;&#x5668;&#x53d1;&#x8fc7;&#x6765;&#x7684;sessionID"/>
</node>
<node CREATED="1465031072835" ID="ID_892190552" MODIFIED="1465031102004" POSITION="right" TEXT="&#x83b7;&#x53d6;&#x51fd;&#x6570;(fun)&#x540d;&#x79f0;">
<node CREATED="1465030952889" ID="ID_1003466393" MODIFIED="1465031071700" TEXT="fun.__name__"/>
</node>
<node CREATED="1465031177753" ID="ID_812209386" MODIFIED="1465031191947" POSITION="right" TEXT="&#x8bb0;&#x5f55;&#x51fd;&#x6570;&#x6267;&#x884c;&#x65f6;&#x95f4;">
<node CREATED="1465031192448" ID="ID_900262749" MODIFIED="1465042508446" TEXT="import time&#xa;start = time.time()&#xa;&#x8981;&#x6267;&#x884c;&#x7684;&#x51fd;&#x6570;&#xa;exec_time = time.time() - start&#xa;print exec_time"/>
<node CREATED="1465042417630" ID="ID_219571930" MODIFIED="1465042518268" TEXT="import time&#xa;start = time.clock()&#xa;&#x8981;&#x6267;&#x884c;&#x7684;&#x51fd;&#x6570;&#xa;end = time.clock()&#xa;print end - start"/>
</node>
<node CREATED="1465043952791" ID="ID_1175524713" MODIFIED="1465046879736" POSITION="right" TEXT="&#x88c5;&#x9970;&#x5668;">
<node CREATED="1465043962526" ID="ID_1551339836" MODIFIED="1465043966554" TEXT="&#x88c5;&#x9970;&#x5668;&#x53ef;&#x4ee5;&#x5bf9;&#x4e00;&#x4e2a;&#x51fd;&#x6570;&#x3001;&#x65b9;&#x6cd5;&#x6216;&#x8005;&#x7c7b;&#x8fdb;&#x884c;&#x52a0;&#x5de5;"/>
<node CREATED="1465044775494" ID="ID_1121462845" MODIFIED="1465045143103" TEXT="&#x88c5;&#x9970;&#x5668;&#x53ef;&#x4ee5;&#x7528;def&#x7684;&#x5f62;&#x5f0f;&#x5b9a;&#x4e49;.&#x88c5;&#x9970;&#x5668;&#x63a5;&#x6536;&#x4e00;&#x4e2a;&#x53ef;&#x8c03;&#x7528;&#x5bf9;&#x8c61;&#x4f5c;&#x4e3a;&#x8f93;&#x5165;&#x53c2;&#x6570;&#xa;,&#x5e76;&#x8fd4;&#x56de;&#x4e00;&#x4e2a;&#x65b0;&#x7684;&#x53ef;&#x8c03;&#x7528;&#x5bf9;&#x8c61;.&#xa;&#x88c5;&#x9970;&#x5668;&#x7684;&#x5f15;&#x7528;&#x4f7f;&#x7528;@&#x7b26;&#x53f7;  &#xa;"/>
<node CREATED="1465045010089" ID="ID_1123745750" MODIFIED="1465045844967" TEXT="def decorate(F):   #&#x53c2;&#x6570;F&#x5f15;&#x7528;&#x4e86;&#x4e0b;&#x6587;&#x4e2d;&#x7684;plus(a, b)&#x51fd;&#x6570;&#x3002; F&#xff1d;plus(a, b)&#xa;    def liline(a, b):  #&#x65b0;&#x5efa;&#x4e86;&#x4e00;&#x4e2a;&#x51fd;&#x6570;.&#x5f62;&#x53c2;&#x4e3a;F&#x51fd;&#x6570;&#x4e2d;&#x7684;a,b&#x5f62;&#x53c2;&#xa;        print &apos;input&apos;, a, b  #&#x6253;&#x5370;&#x51fa;a, b&#x4e24;&#x4e2a;&#x503c;&#xa;        return F(a, b)   #&#x8fd4;&#x56de;F&#x51fd;&#x6570;&#x7684;&#x7ed3;&#x679c;&#xa;    return liline   #&#x8fd4;&#x56de;&#x5185;&#x5d4c;&#x51fd;&#x6570;&#xff0c;&#x4e0d;&#x9700;&#x8981;&#x52a0;()&#x53f7;&#xa;&#x9;&#x9;&#xa;@decorate  #&#x5728;&#x4e0b;&#x9762;&#x7684;&#x51fd;&#x6570;&#x4e0a;&#x5f15;&#x7528;&#x88c5;&#x9970;&#x5668;&#xa;def plus(a, b):&#xa;    return a + b&#xa;&#x9;&#xa;print plus(3, 4)&#x9;#&#x6267;&#x884c;&#x51fd;&#x6570;">
<node CREATED="1465045905059" ID="ID_75178534" MODIFIED="1465046094904" TEXT="from functools import wraps   #&#x52a0;&#x8f7d;python&#x81ea;&#x5e26;&#x7684;wraps&#x88c5;&#x9970;&#x5668;.&#xa;def login_required(func):&#xa;&#x9;&#xa;&#x9;@wraps(func)   #&#x5f53;&#x4e00;&#x4e2a;&#x51fd;&#x6570;&#x4e0a;&#x5f15;&#x7528;&#x4e86;&#x591a;&#x4e2a;&#x88c5;&#x9970;&#x5668;&#x65f6;,&#x9700;&#x8981;&#x5f15;&#x7528;&#x7cfb;&#x7edf;&#x88c5;&#x9970;&#x5668;wraps,&#x89e3;&#x51b3;python&#x88c5;&#x9970;&#x5668;&#x81ea;&#x8eab;bug&#xa;&#x9;def wrapper(*args, **kwargs):&#xa;&#x9;&#x9;if session.get(&apos;user&apos;) is None:&#xa;&#x9;&#x9;&#x9;return redirect(&apos;/&apos;)&#xa;&#x9;&#x9;rt = func(*args, **kwargs)&#xa;&#x9;&#x9;return rt&#xa;&#x9;&#x9;&#xa;&#x9;return wrapper&#x9;"/>
</node>
</node>
<node CREATED="1465046859469" ID="ID_766848080" MODIFIED="1465046868338" POSITION="right" TEXT="&#x6d88;&#x606f;&#x95ea;&#x73b0;">
<node CREATED="1465046881959" ID="ID_401652669" MODIFIED="1465047091599" TEXT="&#x4ece;&#x4e00;&#x4e2a;&#x9875;&#x9762;&#x8df3;&#x8f6c;&#x5230;&#x53e6;&#x4e00;&#x4e2a;&#x9875;&#x9762;&#x65f6;&#x4f20;&#x9012;&#x6d88;&#x606f;"/>
<node CREATED="1465047095080" ID="ID_1819490038" MODIFIED="1465047146433" TEXT="from flask import flash">
<node CREATED="1465047159065" ID="ID_1717428428" MODIFIED="1465047191065" TEXT="&#x5bfc;&#x5165;flask&#x6846;&#x67b6;&#x91cc;&#x7684;flash&#x51fd;&#x6570;&#x5b9e;&#x73b0;&#x6d88;&#x606f;&#x95ea;&#x73b0;"/>
<node CREATED="1465047437247" ID="ID_1009894453" MODIFIED="1465047847681" TEXT="flash(&apos;User [%s] successfully deleted&apos; % username)  #&#x5728;&#x7a0b;&#x5e8f;&#x5904;&#x7406;&#x65f6;&#x4f7f;&#x7528;flash()&#x5b9a;&#x4e49;&#x8981;&#x4f20;&#x9012;&#x7684;&#x6d88;&#x606f;&#xa;return redirect(&apos;/users/&apos;)   #&#x5f53;&#x91cd;&#x5b9a;&#x5411;&#x5230;/users/&#x9875;&#x9762;&#x65f6;&#x53ef;&#x4ee5;&#x4f7f;&#x7528;get_flashed_messages()&#x83b7;&#x53d6;&#x4f20;&#x9012;&#x7684;&#x6d88;&#x606f;&#x5185;&#x5bb9;&#xa;{% for msg in get_flashed_messages() %}   #html&#x9875;&#x9762;&#x4e0a;&#x5faa;&#x73af;git_flashed_messages()&#x83b7;&#x53d6;&#x4f20;&#x9012;&#x8fc7;&#x6765;&#x7684;&#x6d88;&#x606f;&#x5185;&#x5bb9;&#xa;    &lt;td&gt;&#xa;        &lt;span style=&quot;color:red&quot;&gt;{{ msg }} &lt;/span&gt;&#xa;    &lt;/td&gt;&#xa;{% endfor %}"/>
</node>
</node>
<node CREATED="1465047949079" ID="ID_194142076" MODIFIED="1465047952942" POSITION="right" TEXT="mysql">
<node CREATED="1465047956422" ID="ID_766993157" MODIFIED="1465048068662" TEXT="pip install mysql-python">
<node CREATED="1465048074073" ID="ID_1546618311" MODIFIED="1465048096848" TEXT="&#x5efa;&#x5e93;">
<node CREATED="1465048609493" ID="ID_319762545" MODIFIED="1465048624478" TEXT="create database dbname;"/>
</node>
<node CREATED="1465048097812" ID="ID_1826353872" MODIFIED="1465048102001" TEXT="&#x5efa;&#x8868;">
<node CREATED="1465048631423" ID="ID_1588197508" MODIFIED="1465048958874" TEXT="create table access_logs (IP varchar(32) DEFAULT NULL, URL text DEFAULT NULL, CODE varchar(10) DEFAULT NULL, TOTAL int DEFAULT NULL) ENGINE=TokuDB DEFAULT CHARSET=utf8&#xa;&#xa;&#x5217;&#x9ed8;&#x8ba4;&#x4e3a;&#x7a7a;:DEFAULT NULL&#xa;&#x5217;&#x81ea;&#x589e;&#x957f;: auto_increment&#xa;&#x5217;&#x4e3a;&#x4e3b;&#x952e;:primary    &#x5217;&#x4e3a;&#x4e3b;&#x952e;&#x610f;&#x5473;&#x7740;&#x4e3a;&#x5141;&#x8bb8;&#x4e3a;&#x7a7a;&#xff0c;&#x4e0d;&#x80fd;&#x91cd;&#x590d;&#xa;"/>
</node>
<node CREATED="1465048102541" ID="ID_320601530" MODIFIED="1465048121926" TEXT="&#x589e;">
<node CREATED="1465048702297" ID="ID_333582434" MODIFIED="1465050227728" TEXT="inert into user(username, password, age) values(&apos;kk&apos;, &apos;123456&apos;, 27);"/>
</node>
<node CREATED="1465048122480" ID="ID_144700606" MODIFIED="1465048124665" TEXT="&#x5220;">
<node CREATED="1465050010263" ID="ID_1905458391" MODIFIED="1465050233793" TEXT="delete from user where username = &apos;kk&apos;;">
<node CREATED="1465050253529" ID="ID_536162872" MODIFIED="1465050263172" TEXT="&#x4e0d;&#x52a0;&#x6761;&#x4ef6;&#x5220;&#x9664;&#x6240;&#x6709;"/>
</node>
</node>
<node CREATED="1465048125540" ID="ID_1261301318" MODIFIED="1465048128342" TEXT="&#x6539;">
<node CREATED="1465050092596" ID="ID_1021809223" MODIFIED="1465050274895" TEXT="update user set password=md5(123456), age=25 where username = &apos;kk&apos; ; &#x4e0d;&#x52a0;&#x6761;&#x4ef6;&#x66f4;&#x65b0;&#x6240;&#x6709;"/>
</node>
<node CREATED="1465048130078" ID="ID_1730438831" MODIFIED="1465048132320" TEXT="&#x67e5;">
<node CREATED="1465050112834" ID="ID_715787751" MODIFIED="1465050285202" TEXT="select * from user where username = &apos;kk&apos;;&#x4e0d;&#x52a0;&#x6761;&#x4ef6;&#x67e5;&#x8be2;&#x6240;&#x6709;"/>
</node>
<node CREATED="1465048136245" ID="ID_1411637901" MODIFIED="1465048573075" TEXT="import MySQLdb">
<node CREATED="1465048557374" ID="ID_607487021" MODIFIED="1465048567850" TEXT="&#x6253;&#x5f00;&#x6570;&#x636e;&#x5e93;&#x8fde;&#x63a5;">
<node CREATED="1465048198914" ID="ID_933063446" MODIFIED="1465048534536" TEXT="MySQLdb.connect()&#xa;&#x53c2;&#x6570;:host(IP), port(&#x7aef;&#x53e3;), user(&#x7528;&#x6237;), passwd(&#x5bc6;&#x7801;), db(&#x6570;&#x636e;&#x5e93;), charset(&#x5b57;&#x7b26;&#x96c6;)&#xa;&#x4f8b;:&#xa;conn=MySQLdb.connect(host=192.168.254.19, port=3306, user=&apos;reboot&apos;, passwd=&apos;reboot&apos;, db=&apos;app1&apos;, charset=&apos;utf8&apos;)"/>
</node>
<node CREATED="1465048573067" ID="ID_517620857" MODIFIED="1465048580854" TEXT="&#x5173;&#x95ed;&#x6570;&#x636e;&#x5e93;&#x8fde;&#x63a5;">
<node CREATED="1465048536684" ID="ID_1277755184" MODIFIED="1465048545140" TEXT="conn.close()"/>
</node>
<node CREATED="1465048969442" ID="ID_1894629293" MODIFIED="1465048997786" TEXT="&#x6e38;&#x6807;">
<node CREATED="1465049129336" ID="ID_482517943" MODIFIED="1465049152555" TEXT="&#x8981;&#x64cd;&#x4f5c;&#x6570;&#x636e;&#x5e93;&#x5fc5;&#x987b;&#x521b;&#x5efa;&#x6e38;&#x6807;"/>
<node CREATED="1465049201816" ID="ID_720332784" MODIFIED="1465049218836" TEXT="cur = conn.cursor()"/>
</node>
<node CREATED="1465049225193" ID="ID_1761168357" MODIFIED="1465049254253" TEXT="sql&#x4e8b;&#x52a1;">
<node CREATED="1465049236286" ID="ID_1607557228" MODIFIED="1465049284838" TEXT="&#x67e5;&#x8be2;&#x4e0d;&#x9700;&#x8981;&#x4e8b;&#x52a1;">
<node CREATED="1465049286830" ID="ID_565522083" MODIFIED="1465049360951" TEXT="count = cur.execute(selelct * from where username = %s, &apos;kk&apos;)"/>
<node CREATED="1465049726124" ID="ID_1006098118" MODIFIED="1465049770367" TEXT="rt_list = cur.fetchall() "/>
</node>
<node CREATED="1465049374900" ID="ID_840893265" MODIFIED="1465049403460" TEXT="&#x63d2;&#x5165;,&#x66f4;&#x65b0;,&#x5220;&#x9664;&#x9700;&#x8981;&#x4e8b;&#x52a1;">
<node CREATED="1465049405002" ID="ID_241112720" MODIFIED="1465049803591" TEXT="count = cur.execute(update user set password=md5(%s) , 123456)&#xa;conn.commit() &#x63d0;&#x4ea4;&#x4e8b;&#x52a1;&#xa;"/>
</node>
</node>
</node>
</node>
</node>
</node>
</map>
