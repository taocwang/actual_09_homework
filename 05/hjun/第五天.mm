<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1464091777891" ID="ID_972785198" MODIFIED="1464091793140" TEXT="&#x7b2c;&#x4e94;&#x5929;">
<node CREATED="1464090236630" ID="ID_1662482230" MODIFIED="1464090252907" POSITION="right" TEXT="flask">
<node CREATED="1464090254621" ID="ID_1408748877" MODIFIED="1464090266159" TEXT="&#x4e00;&#x4e2a;python&#x5199;&#x7684;web&#x6846;&#x67b6;"/>
<node CREATED="1464090294554" ID="ID_276162823" MODIFIED="1464090449931" TEXT="from flask import Flask &#x4ece;flask&#x5305;&#x5bfc;&#x5165;&#x4e00;&#x4e2a;Flask&#x7c7b;"/>
<node CREATED="1464090453668" ID="ID_1746411094" MODIFIED="1464090708556" TEXT="app = Flask(__name__) &#x751f;&#x6210;&#x4e86;&#x4e00;&#x4e2a;Flask&#x5bf9;&#x8c61;"/>
<node CREATED="1464090718805" ID="ID_675574920" MODIFIED="1464090827177" TEXT="@app.route(&apos;/&apos;)  url&#x8bbf;&#x95ee;&#x8def;&#x5f84;&#x5904;&#x7406;">
<node CREATED="1464090829896" ID="ID_1961720288" MODIFIED="1464090874967" TEXT="@app.route(&quot;/&quot;)  &#x4e0b;&#x9762;&#x8ddf;&#x8981;&#x5904;&#x7406;&#x7684;&#x51fd;&#x6570;.">
<node CREATED="1464092174694" ID="ID_1580348003" MODIFIED="1464092320679" TEXT="@app.route(&quot;/&quot;)&#xa;def index():&#xa;    return &quot;hello,work&quot;&#xa;"/>
</node>
<node CREATED="1464094545551" ID="ID_212110906" MODIFIED="1464094603197" TEXT="@app.route(&quot;/login/&quot;, methods=[&apos;get&apos;,&apos;post&apos;])">
<node CREATED="1464094607781" ID="ID_474540613" MODIFIED="1464094706426" TEXT="methods&#x5b9a;&#x4e49;&#x5141;&#x8bb8;&#x4ec0;&#x4e48;&#x65b9;&#x5f0f;&#x63a5;&#x6536;&#x8bf7;&#x6c42;"/>
</node>
</node>
<node CREATED="1464090959286" ID="ID_1298010384" MODIFIED="1464091262979" TEXT="if __name__ == &apos;__main__&apos;:&#xa;    app.run(host=&apos;0.0.0.0&apos;, port=80, debug=True)    #&#x8fd0;&#x884c;&#x4e00;&#x4e2a;&#x670d;&#x52a1;"/>
<node CREATED="1464090964099" ID="ID_1414204250" MODIFIED="1464092503338" TEXT="json&#x6a21;&#x5757;">
<node CREATED="1464092505538" ID="ID_1712960339" MODIFIED="1464092752220" TEXT="import json &#x52a0;&#x8f7d;json&#x6a21;&#x5757;">
<node CREATED="1464092524335" ID="ID_1060183932" MODIFIED="1464092595903" TEXT="json.loads(str())  &#x628a;&#x5b57;&#x7b26;&#x4e32;&#x7c7b;&#x578b;&#x8f6c;&#x4e3a;list&#x7c7b;&#x578b;"/>
<node CREATED="1464092601234" ID="ID_214615949" MODIFIED="1464092640270" TEXT="json.dumps(list()) &#x628a;list&#x7c7b;&#x578b;&#x8f6c;&#x4e3a;&#x5b57;&#x7b26;&#x4e32;&#x7c7b;&#x578b;"/>
</node>
</node>
<node CREATED="1464090897470" ID="ID_1711481802" MODIFIED="1464092951328" TEXT="form&#x8868;&#x5355;">
<node CREATED="1464092954824" ID="ID_1621822408" MODIFIED="1464092967316" TEXT="action=&quot;&quot;">
<node CREATED="1464093035935" ID="ID_603762893" MODIFIED="1464093135729" TEXT="&#x63d0;&#x4ea4;&#x5230;&#x54ea;&#x91cc;&#x5728;&#x53bb;">
<node CREATED="1464093144696" ID="ID_972173295" MODIFIED="1464093224853" TEXT="@app.route(&quot;/login/&quot;)&#xa;def  login():&#xa;    return "/>
</node>
</node>
<node CREATED="1464092982784" ID="ID_1781250266" MODIFIED="1464093028117" TEXT="method=&quot;get|post&quot;">
<node CREATED="1464093092359" ID="ID_663215267" MODIFIED="1464093116995" TEXT="&#x7528;&#x6237;&#x63d0;&#x4ea4;&#x4f7f;&#x7528;post&#x8bf7;&#x6c42;"/>
</node>
<node CREATED="1464093235095" ID="ID_174974457" MODIFIED="1464093242899" TEXT="input&#x6807;&#x7b7e;">
<node CREATED="1464093244245" ID="ID_1289688569" MODIFIED="1464093692449" TEXT="&lt;input type=&quot;text&quot; name=&quot;username&quot; /&gt;">
<node CREATED="1464093403700" ID="ID_985592027" MODIFIED="1464093492458" TEXT="type=&quot;text&quot;&#x5c5e;&#x6027;&#x8868;&#x793a;&#x53ef;&#x89c1;&#x5185;&#x5bb9;&#x6587;&#x672c;&#x6846;"/>
<node CREATED="1464093470202" ID="ID_118722047" MODIFIED="1464093579752" TEXT="name=&quot;username&quot; &#x8868;&#x793a;&#x7a0b;&#x5e8f;&#x8bfb;&#x53d6;username&#x83b7;&#x53d6;&#x8fd9;&#x4e2a;&#x6587;&#x672c;&#x6846;&#x7684;&#x503c;"/>
</node>
<node CREATED="1464093645936" ID="ID_1726423210" MODIFIED="1464093755406" TEXT="&lt;input type=&quot;password&quot; name=&quot;password&quot; /&gt;">
<node CREATED="1464093723388" ID="ID_743535214" MODIFIED="1464093817907" TEXT="type=&quot;password&quot; &#x8868;&#x793a;&#x6587;&#x672c;&#x6846;&#x8f93;&#x5165;&#x7684;&#x5185;&#x5bb9;&#x4e0d;&#x663e;&#x793a;&#x51fa;&#x6765;,&#x7528;&#x4e8e;&#x8f93;&#x5165;&#x5bc6;&#x7801;"/>
</node>
<node CREATED="1464093832340" ID="ID_397752476" MODIFIED="1464093954241" TEXT="&lt;input type=&quot;submit&quot; value=&quot;&#x767b;&#x9646;&quot; /&gt;">
<node CREATED="1464093955962" ID="ID_978364819" MODIFIED="1464093984845" TEXT="type=&quot;submit&quot;&#x63d0;&#x4ea4;&#x5c5e;&#x6027;"/>
<node CREATED="1464093992141" ID="ID_182098365" MODIFIED="1464094207472" TEXT="value&#xff1d;&quot;&#x767b;&#x9646;&quot; &#x9875;&#x9762;&#x4e0a;&#x663e;&#x793a;&#x767b;&#x9646;&#x6309;&#x94ae;,&#x5f53;&#x70b9;&#x51fb;&#x6309;&#x94ae;&#x65f6;&#x5c31;&#x4f1a;&#x628a;&#x4e0a;&#x9762;&#x4e24;&#x4e2a;&#x6587;&#x672c;&#x6846;&#x7684;&#x5185;&#x5bb9;&#x63d0;&#x4ea4;&#x5230;python&#x7a0b;&#x5e8f;,python&#x4ee3;&#x7801;&#x8bfb;&#x53d6;username&#x548c;password&#x83b7;&#x53d6;&#x6587;&#x672c;&#x6846;&#x7684;&#x503c; "/>
</node>
</node>
</node>
<node CREATED="1464094835722" ID="ID_1626010301" MODIFIED="1464094886948" TEXT="from flask import request">
<node CREATED="1464094894614" ID="ID_1515172507" MODIFIED="1464094953179" TEXT="request.args.get(&apos;cut&apos;)">
<node CREATED="1464094956463" ID="ID_29322460" MODIFIED="1464095306114" TEXT="&#x5f53;&#x4f7f;&#x7528;get&#x8bf7;&#x6c42;&#x65f6;http://logs/?cut=10  &#x9700;&#x8981;&#x4f7f;&#x7528;request.args&#x63a5;&#x6536;&#x8bf7;&#x6c42;"/>
</node>
<node CREATED="1464095081070" ID="ID_1044969637" MODIFIED="1464095177651" TEXT="request.form.get(&apos;username&apos;, &apos;&apos;)">
<node CREATED="1464095193354" ID="ID_1356455172" MODIFIED="1464095285398" TEXT="&#x5f53;&#x4f7f;&#x7528;post&#x8bf7;&#x6c42;&#x65f6;&lt;form action=&quot;/login/&quot; method=&quot;post&quot;&gt; &#x9700;&#x8981;&#x4f7f;&#x7528;request.form&#x63a5;&#x6536;&#x8bf7;&#x6c42;"/>
</node>
<node CREATED="1464095409951" ID="ID_224819071" MODIFIED="1464095667891" TEXT="params = request.args if request.method == &apos;GET&apos; else request.form">
<node CREATED="1464095670522" ID="ID_518032471" MODIFIED="1464095751190" TEXT="if&#x4e09;&#x6728;&#x8868;&#x8fbe;&#x5f0f; &#x5f53;if&#x4e3a;True&#x65f6;params=request.args&#x4e3a;flast&#x65f6;params=request.form"/>
</node>
</node>
<node CREATED="1464095881582" ID="ID_1286477746" MODIFIED="1464095910966" TEXT="from flask import render_template">
<node CREATED="1464095912671" ID="ID_166982218" MODIFIED="1464096042701" TEXT="&#x8fd4;&#x56de;&#x67d0;&#x4e2a;&#x9759;&#x6001;&#x9875;&#x9762;">
<node CREATED="1464096049364" ID="ID_1260924435" MODIFIED="1464096228009" TEXT="@app.route(&apos;/&apos;)&#xa;def index():&#xa;    return render_template(&apos;login.html&apos;)   #&#x81ea;&#x52a8;&#x8fd4;&#x56de;templates&#x76ee;&#x5f55;&#x91cc;&#x7684;login.html&#x9759;&#x6001;&#x6587;&#x4ef6;"/>
<node CREATED="1464096393414" ID="ID_1736968967" MODIFIED="1464096688297" TEXT="return  render_template(&quot;login.html&quot;, username=username, error=&quot;username error&quot;)  ">
<node CREATED="1464096692721" ID="ID_185662036" MODIFIED="1464096883850" TEXT="username=username &#x8868;&#x793a;&#x5411;login.html&#x9875;&#x9762;&#x7684;form&#x8868;&#x5355;name&#x4e3a;username&#x7684;&#x6587;&#x672c;&#x6846;&#x56de;&#x663e;&#x503c;"/>
<node CREATED="1464096908762" ID="ID_794672203" MODIFIED="1464097010741" TEXT="error=&quot;username error&quot; &#x8868;&#x793a;&#x5411;login.html&#x9875;&#x9762;&#x56de;&#x663e;&#x9519;&#x8bef;&#x4fe1;&#x606f;,&#x53ef;&#x4ee5;&#x4f7f;&#x7528;{{error}}&#x63a5;&#x6536;"/>
</node>
</node>
</node>
<node CREATED="1464097161885" ID="ID_1993052867" MODIFIED="1464097179392" TEXT="from flask import redirect">
<node CREATED="1464097180632" ID="ID_382287369" MODIFIED="1464097200729" TEXT="302&#x8df3;&#x8f6c;">
<node CREATED="1464097202127" ID="ID_808969534" MODIFIED="1464097326395" TEXT="if user.validate_login(username, password):&#xa;    return redirect(&quot;/logs/&quot;)">
<node CREATED="1464097328912" ID="ID_1085317458" MODIFIED="1464097421036" TEXT="&#x5f53;&#x6ee1;&#x8db3;if&#x6761;&#x4ef6;&#x540e;, 302&#x8df3;&#x8f6c;&#x5230;&#x6307;&#x5b9a;url"/>
</node>
</node>
</node>
<node CREATED="1464097679904" ID="ID_1648667856" MODIFIED="1464097685341" TEXT="a&#x6807;&#x7b7e;">
<node CREATED="1464097687965" ID="ID_934511261" MODIFIED="1464097692292" TEXT="&lt;a href=&quot;/useredit/index/&quot;&gt;&#x66f4;&#x65b0;&lt;/a&gt;">
<node CREATED="1464097693666" ID="ID_1156086067" MODIFIED="1464097870329" TEXT="&#x505a;&#x8df3;&#x8f6c;,&#x4e0d;&#x540c;&#x4e8e;301,302&#x5ba2;&#x6237;&#x7aef;&#x91cd;&#x5b9a;&#x5411;.a&#x6807;&#x7b7e;&#x662f;&#x670d;&#x52a1;&#x7aef;&#x8df3;&#x8f6c;"/>
</node>
</node>
<node CREATED="1464097892408" ID="ID_1197316769" MODIFIED="1464097931925" TEXT="html&#x5f15;&#x7528;python&#x8fd4;&#x56de;&#x503c;">
<node CREATED="1464097943024" ID="ID_27988106" MODIFIED="1464098128920" TEXT="{% for user in user_list %}&#xa;    &lt;tr&gt;&#xa;        &lt;td&gt; {{ user[&apos;username&apos;] }} &lt;/td&gt;&#xa;        &lt;td&gt; {{ user[&apos;age&apos;] }} &lt;/td&gt;&#xa;    &lt;/tr&gt;&#xa;&lt;% endfor %&gt;">
<node CREATED="1464098133152" ID="ID_33205897" MODIFIED="1464098217659" TEXT="&#x4f7f;&#x7528;{% for ...... %} ......&lt;% endfor %&gt; &#x6267;&#x884c;&#x5faa;&#x73af;"/>
</node>
<node CREATED="1464098255785" ID="ID_125555223" MODIFIED="1464098406107" TEXT="{% if userdel_info %}&#xa;    &lt;tr&gt;&#xa;        &lt;span style=&quot;color:red&quot;&gt;{{ userdel_info }} &lt;/span&gt;&#xa;    &lt;/tr&gt;&#xa;&lt;% endif %&gt;">
<node CREATED="1464098408135" ID="ID_199554502" MODIFIED="1464098448941" TEXT="&#x4f7f;&#x7528;{% if ...... %} ...... &lt;% endif %&gt; &#x6267;&#x884c;if&#x8bed;&#x53e5;"/>
</node>
<node CREATED="1464098452453" ID="ID_769030128" MODIFIED="1464098478497" TEXT="{{ username }}">
<node CREATED="1464098479907" ID="ID_1368026229" MODIFIED="1464098515455" TEXT="&#x4f7f;&#x7528;{{ }} &#x65b9;&#x5f0f;&#x4ece;html&#x9875;&#x9762;&#x83b7;&#x53d6;python&#x8fd4;&#x56de;&#x503c;"/>
</node>
<node CREATED="1464098520445" ID="ID_1399008677" MODIFIED="1464099046516" TEXT="&lt;form action = &quot;/userdel/&quot; method=&quot;post&quot;&gt;&#xa;    &lt;input type=&quot;text&quot; name=&quot;username&quot; value=&quot;{{ username }}&quot;&gt;&#xa;&lt;/form&gt;">
<node CREATED="1464099049020" ID="ID_1564711869" MODIFIED="1464099132386" TEXT="&#x5728;form&#x8868;&#x5355;&#x6587;&#x672c;&#x6846;&#x4e2d;&#x4f7f;&#x7528;value&#xff1d;{{ }} &#x65b9;&#x5f0f;&#x83b7;&#x53d6;python&#x8fd4;&#x56de;&#x503c;"/>
</node>
</node>
</node>
</node>
</map>
