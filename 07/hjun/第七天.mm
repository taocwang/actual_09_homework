<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1465816500966" ID="ID_1060111679" MODIFIED="1465816510412" TEXT="&#x7b2c;&#x4e03;&#x5929;">
<node CREATED="1465816538358" ID="ID_292903503" MODIFIED="1465816982767" POSITION="right" TEXT="html">
<node CREATED="1465817310898" ID="ID_1976375605" MODIFIED="1465817582451" TEXT="form&#x8868;&#x5355;">
<node CREATED="1465817585561" ID="ID_1874317938" MODIFIED="1465817701162" TEXT="&lt;input type=&quot;text&quot; name=&quot;username&quot; value=&quot;{{username}}&quot; readonly=&quot;readonly&quot; /&gt;">
<node CREATED="1465817712039" ID="ID_1976882045" MODIFIED="1465817763495" TEXT="readonly&#x4f7f;&#x8f93;&#x5165;&#x6846;&#x4e0d;&#x53ef;&#x4fee;&#x6539;"/>
</node>
<node CREATED="1465817779135" ID="ID_411859398" MODIFIED="1465817904299" TEXT="&lt;input type=&quot;text&quot; name=&quot;username&quot; value=&quot;{{username}}  disabled=&quot;disabled&quot;&quot; /&gt;">
<node CREATED="1465817907025" ID="ID_602991961" MODIFIED="1465817978946" TEXT="disabled&#x8f93;&#x5165;&#x6846;&#x4e0d;&#x53ef;&#x4fee;&#x6539;&#x5e76;&#x4e14;&#x4e0d;&#x63d0;&#x4ea4;value&#x7684;&#x503c;"/>
</node>
<node CREATED="1465818137050" ID="ID_748658802" MODIFIED="1465818199737" TEXT="&lt;input type=&quot;hidden&quot; name=&quot;id&quot; value=&quot;{{id}} /&quot;&gt;">
<node CREATED="1465818283419" ID="ID_938824869" MODIFIED="1465818584136" TEXT="hidden&#x9690;&#x85cf;&#x8f93;&#x5165;&#x6846;,&#x7528;&#x4e8e;&#x4e0d;&#x5728;&#x9875;&#x9762;&#x4e0a;&#x663e;&#x793a;&#x4f46;&#x9700;&#x8981;&#x628a;value&#x63d0;&#x4ea4;&#x5230;&#x540e;&#x7aef;&#x7684;&#x60c5;&#x51b5;"/>
</node>
<node CREATED="1465818696381" ID="ID_526845419" MODIFIED="1465819143077" TEXT="&#x6027;&#x522b;:&lt;input type=&quot;radio&quot; name=&quot;gender&quot; value=&quot;&#x7537;&quot; checked=&quot;checked&quot; /&gt;&#x7537;&#xa;         &lt;input type=&quot;radio&quot; name=&quot;gender&quot; value=&quot;&#x5973;&quot; /&gt;&#x5973;">
<node CREATED="1465819149348" ID="ID_959921301" MODIFIED="1465819360032" TEXT="radio&#x5355;&#x9009;&#x6309;&#x94ae;&#x7c7b;&#x578b;,checked&#x8868;&#x793a;&#x8bbe;&#x4e3a;&#x9ed8;&#x8ba4;"/>
</node>
<node CREATED="1465819464266" ID="ID_1846089214" MODIFIED="1465820128148">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#29233;&#22909;:&lt;input type=&quot;cleckbox&quot; name=&quot;hobby&quot; value=&quot;football&quot; /&gt; &#36275;&#29699;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;input type=&quot;checkbox' name=&quot;hobby&quot; value=&quot;basketball&quot; /&gt;&#31726;&#29699;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;input type=&quot;checkbox&quot; name=&quot;hobby&quot; value=&quot;computer&quot; checked=&quot;checked&quot; /&gt;&#35745;&#31639;&#26426;
    </p>
  </body>
</html></richcontent>
<node CREATED="1465820133881" ID="ID_552636913" MODIFIED="1465820308383" TEXT="request.form.getlist(&quot;hobby&quot;, [])">
<node CREATED="1465820414878" ID="ID_839572455" MODIFIED="1465820469057" TEXT="&#x540e;&#x7aef;&#x4f7f;&#x7528;getlist&#x83b7;&#x53d6;&#x591a;&#x4e2a;&#x503c;&#x800c;&#x4e0d;&#x662f;&#x4f7f;&#x7528;get&#x83b7;&#x53d6;"/>
</node>
<node CREATED="1465820315810" ID="ID_522516033" MODIFIED="1465820394550" TEXT="checkbox&#x591a;&#x9009;&#x6309;&#x94ae;&#x7c7b;&#x578b;,&#x53ef;&#x4ee5;&#x540c;&#x65f6;&#x9009;&#x62e9;&#x591a;&#x4e2a;&#x503c;"/>
</node>
<node CREATED="1465820587221" ID="ID_77897809" MODIFIED="1465821281036">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#37096;&#38376;:&lt;select name =&quot;department&quot;&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;option value=&quot;de_01&quot;&gt;&#30740;&#21457;&#19968;&#37096;&lt;/option&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;option value=&quot;de_02&quot; selected=&quot;selected&quot;&gt;&#30740;&#21457;&#20108;&#37096;&lt;/option&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/select&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1465820984047" ID="ID_511947070" MODIFIED="1465821082689" TEXT="select, option&#x6807;&#x7b7e;&#x5b9e;&#x73b0;&#x4e0b;&#x62c9;&#x6846;&#xff0c;selected&#x8868;&#x793a;&#x9ed8;&#x8ba4;&#x9009;&#x4e2d;"/>
<node CREATED="1465821084452" ID="ID_1029574475" MODIFIED="1465821261005" TEXT="select name=&quot;department&quot; multiple=&quot;multiple&quot;&gt;">
<node CREATED="1465821286144" ID="ID_369801542" MODIFIED="1465821345448" TEXT="multiple&#x8868;&#x793a;&#x53ef;&#x4ee5;&#x591a;&#x9009;,&#x4e0d;&#x5e38;&#x7528;"/>
</node>
</node>
<node CREATED="1465821407029" ID="ID_974368284" MODIFIED="1465821952561">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#22791;&#27880;: &lt;textarea name=&quot;remark&quot;&gt;&lt;/textarea&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1465821556511" ID="ID_1738512535" MODIFIED="1465822065117" TEXT="&#x6587;&#x672c;&#x6846;"/>
</node>
<node CREATED="1465821684350" ID="ID_1161723979" MODIFIED="1465822049358">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;form action=&quot;/user/add/&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
    </p>
    <p>
      &#22836;&#20687;:&lt;input type=&quot;file&quot; name=&quot;img&quot; /&gt;
    </p>
    <p>
      &lt;/form&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1465822051393" ID="ID_1775063860" MODIFIED="1465822232164" TEXT="&#x6587;&#x4ef6;&#x4e0a;&#x4f20;, &#x5fc5;&#x987b;&#x8981;&#x8bbe;&#x7f6e;form&#x63d0;&#x4ea4;&#x7c7b;&#x578b;&#x4e3a;&quot;multipart/form-data&quot;"/>
<node CREATED="1465822237482" ID="ID_747567139" MODIFIED="1465822564265">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      request.files.get('img')
    </p>
    <p>
      if img:
    </p>
    <p>
      &#160;&#160;&#160;&#160;print img.filename
    </p>
    <p>
      &#160;&#160;&#160;&#160;img.save('/tmp/kk.png')
    </p>
  </body>
</html></richcontent>
<node CREATED="1465822567748" ID="ID_1778450525" MODIFIED="1465822601791" TEXT="&#x540e;&#x7aef;&#x83b7;&#x53d6;&#x4e0a;&#x4f20;&#x7684;&#x6570;&#x636e;&#x5e76;&#x4fdd;&#x5b58;"/>
<node CREATED="1465822606760" ID="ID_475028262" MODIFIED="1465822634740" TEXT="img.filename &#x53ef;&#x4ee5;&#x83b7;&#x53d6;&#x88ab;&#x4e0a;&#x4f20;&#x7684;&#x539f;&#x59cb;&#x6587;&#x4ef6;&#x540d;"/>
<node CREATED="1465822638526" ID="ID_1790300153" MODIFIED="1465822705706" TEXT="img.save(&quot;/tmp/kk.png&quot;) &#x540e;&#x7aef;&#x4fdd;&#x5b58;&#x6587;&#x4ef6;"/>
</node>
</node>
<node CREATED="1465823121207" ID="ID_1882286179" MODIFIED="1465823225294">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;img src=&quot;xxxx.png&quot; /&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1465823227264" ID="ID_263261825" MODIFIED="1465823237684" TEXT="&#x663e;&#x793a;&#x56fe;&#x7247;"/>
</node>
</node>
<node CREATED="1465823387145" ID="ID_397080914" MODIFIED="1465823500492" TEXT="request.headers">
<node COLOR="#338800" CREATED="1465823503146" ID="ID_1462008159" MODIFIED="1465823548133" TEXT="&#x8fd4;&#x56de;&#x5ba2;&#x6237;&#x7aef;&#x7684;header&#x4fe1;&#x606f;"/>
</node>
<node CREATED="1465822771613" ID="ID_1895268580" MODIFIED="1465822779455" TEXT="&lt;br /&gt;">
<node CREATED="1465822780165" ID="ID_624901647" MODIFIED="1465822788242" TEXT="&#x6362;&#x884c;"/>
</node>
<node CREATED="1465823627684" ID="ID_1103650818" MODIFIED="1465823685977">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;span&gt;xxx&lt;/span&gt; &#34892;&#32423;
    </p>
    <p>
      &lt;div&gt;xxx&lt;/div&gt;&#160;&#160;&#22359;&#32423;
    </p>
    <p>
      &lt;p&gt;xxx&lt;/p&gt; &#27573;&#33853;&#32423;
    </p>
  </body>
</html></richcontent>
<node CREATED="1465823813346" ID="ID_1209629257" MODIFIED="1465823836523" TEXT="&#x591a;&#x4e2a;span&#x4f1a;&#x663e;&#x793a;&#x4e00;&#x884c;"/>
<node CREATED="1465823846226" ID="ID_1392480301" MODIFIED="1465824020585" TEXT="&#x591a;&#x4e2a;div&#x5c31;&#x6709;&#x591a;&#x4e2a;&#x5757;"/>
<node CREATED="1465823878309" ID="ID_1445046231" MODIFIED="1465823992658" TEXT="&#x591a;&#x4e2a;p&#x4f1a;&#x4ee5;&#x6bb5;&#x843d;&#x5f62;&#x5f0f;&#x5c55;&#x73b0;,&#x5e76;&#x4e14;&#x80fd;&#x5f88;&#x660e;&#x663e;&#x770b;&#x51fa;&#x6bb5;&#x843d;&#x95f4;&#x7684;&#x95f4;&#x8ddd;"/>
</node>
<node CREATED="1465824053384" ID="ID_37675713" MODIFIED="1465824165503" TEXT="&lt;iframe src=&quot;http://xxx&quot; &gt;&lt;/iframe&gt;">
<node CREATED="1465824178260" ID="ID_1642833674" MODIFIED="1465824235314" TEXT="&#x94fe;&#x63a5;&#x522b;&#x4eba;&#x7684;&#x9875;&#x9762;&#x5c55;&#x793a;&#x5728;&#x81ea;&#x5df1;&#x7684;&#x9875;&#x9762;&#x4e0a;,&#x73b0;&#x5728;&#x5df2;&#x7ecf;&#x4e0d;&#x5e38;&#x7528;&#x4e86;"/>
</node>
</node>
<node CREATED="1465906342853" ID="ID_565488832" MODIFIED="1465906349212" POSITION="right" TEXT="css">
<node CREATED="1465907608047" ID="ID_1999681165" MODIFIED="1466088225111" TEXT="css&#x89c4;&#x5219;&#x7531;&#x4e24;&#x4e2a;&#x4e3b;&#x8981;&#x7684;&#x90e8;&#x5206;&#x6784;&#x6210;:&#x9009;&#x62e9;&#x5668;, &#x4ee5;&#x53ca;&#x4e00;&#x6761;&#x6216;&#x591a;&#x6761;&#x58f0;&#x660e;"/>
<node CREATED="1465906351193" ID="ID_989320059" MODIFIED="1465906606186" TEXT="&#x9009;&#x62e9;&#x5668;">
<node CREATED="1465906593167" ID="ID_1982423976" MODIFIED="1465906627030" TEXT="&#x6807;&#x8bb0;&#x9009;&#x62e9;&#x5668;">
<node CREATED="1465906644729" ID="ID_513411983" MODIFIED="1465911169530">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#30452;&#25509;&#20351;&#29992;HTML&#26631;&#31614;&#20316;&#20026;&#36873;&#25321;&#22120;&#24403;&#23450;&#20041;&#20102;&#26576;&#20010;&#26631;&#31614;&#30340;&#26631;&#31614;&#36873;&#25321;&#22120;&#26102;
    </p>
    <p>
      &#39029;&#38754;&#19978;&#25152;&#26377;&#30340;&#36825;&#20010;&#26631;&#31614;&#37117;&#23558;&#34987;&#24341;&#29992;&#36825;&#20010;&#26679;&#24335;
    </p>
  </body>
</html></richcontent>
<node CREATED="1465911020409" ID="ID_312411044" MODIFIED="1466062269730">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;head&gt;
    </p>
    <p>
      &lt;style&gt;
    </p>
    <p>
      p{
    </p>
    <p>
      &#160;&#160;&#160;&#160;font-size:12px;
    </p>
    <p>
      &#160;&#160;&#160;&#160;background:#900;
    </p>
    <p>
      &#160;&#160;&#160;&#160;color:090;
    </p>
    <p>
      }
    </p>
    <p>
      &lt;/style&gt;
    </p>
    <p>
      &lt;/head&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1466062165983" ID="ID_1360449793" MODIFIED="1466062232503" TEXT="&#x5185;&#x90e8;&#x6837;&#x5f0f;&#x8868;,&#x4f7f;&#x7528;&lt;style&gt;&#x6807;&#x7b7e;&#x5728;&#x6587;&#x6863;&#x5934;&#x90e8;&#x5b9a;&#x4e49;&#x5185;&#x90e8;&#x6837;&#x5f0f;&#x8868;"/>
</node>
</node>
</node>
<node CREATED="1465906629210" ID="ID_791961133" MODIFIED="1465906637003" TEXT="&#x7c7b;&#x522b;&#x9009;&#x62e9;&#x5668;">
<node CREATED="1465909422402" ID="ID_1937001957" MODIFIED="1466062922347">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#31867;&#36873;&#25321;&#22120;&#21487;&#20197;&#34987;&#24341;&#29992;&#22810;&#27425;
    </p>
  </body>
</html></richcontent>
<node CREATED="1466062471161" ID="ID_1921662174" MODIFIED="1466062666344" TEXT="cat mystyle.css&#xa;.center {text-align: center}">
<node CREATED="1466062502814" ID="ID_214520112" MODIFIED="1466062644009" TEXT="&lt;head&gt;&#xa;&lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot;  href=&quot;mystyle.css&quot;&gt;&#xa;&lt;/head&gt;&#xa;&#xa;&lt;h1 class=&quot;center&quot;&gt;&#xa;This heading will be center-aligned&#xa;&lt;/h1&gt;&#xa;&lt;p class=&quot;center&quot;&gt;&#xa;This paragraph will also be center-aligned.&#xa;&lt;/p&gt;">
<node CREATED="1466062691288" ID="ID_630811775" MODIFIED="1466062759203" TEXT="&#x5916;&#x90e8;&#x6837;&#x5f0f;&#x8868;&#x5728;head&#x6807;&#x7b7e;&#x4f7f;&#x7528;link&#x5f15;&#x7528;,"/>
<node CREATED="1466062761129" ID="ID_1915778742" MODIFIED="1466062805097" TEXT="&#x7c7b;&#x522b;&#x9009;&#x62e9;&#x5668;,&#x4f7f;&#x7528;.&#x53f7;&#x58f0;&#x660e;&#x6837;&#x5f0f;,&#x4f7f;&#x7528;class=&quot;xxx&quot;&#x5f15;&#x7528;&#x6837;&#x5f0f;"/>
</node>
</node>
</node>
</node>
<node CREATED="1465906637331" ID="ID_1373017756" MODIFIED="1465906642003" TEXT="ID&#x9009;&#x62e9;&#x5668;">
<node CREATED="1465908936000" ID="ID_264496977" MODIFIED="1466062939395">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      ID&#36873;&#25321;&#22120;&#21487;&#20197;&#20026;&#26631;&#26377;&#29305;&#23450;id&#30340;HTML&#20803;&#32032;&#25351;&#23450;&#29305;&#23450;&#30340;&#26679;&#24335;
    </p>
    <p>
      id&#23646;&#24615;&#21482;&#33021;&#22312;&#27599;&#20010;HTML&#25991;&#26723;&#20013;&#20986;&#29616;&#19968;&#27425;.
    </p>
  </body>
</html></richcontent>
<node CREATED="1465909068541" ID="ID_1106905423" MODIFIED="1465909136947">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      #red {color:red;}
    </p>
    <p>
      
    </p>
    <p>
      &lt;p id=&quot;red&quot;&gt;&#36825;&#20010;&#27573;&#33853;&#26159;&#32418;&#33394;.&lt;/p&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1466062809931" ID="ID_844550562" MODIFIED="1466062890623" TEXT="ID&#x9009;&#x62e9;&#x5668;,&#x4f7f;&#x7528;#&#x53f7;&#x58f0;&#x660e;&#x6837;&#x5f0f;.&#x4f7f;&#x7528;id=&quot;xxx&quot;&#x5f15;&#x7528;&#x6837;&#x5f0f;"/>
</node>
</node>
</node>
<node CREATED="1466067170822" ID="ID_317523079" MODIFIED="1466067183041" TEXT="&#x5d4c;&#x5957;&#x9009;&#x62e9;&#x5668;">
<node CREATED="1466067183043" ID="ID_430422043" MODIFIED="1466067208669" TEXT="&#x9002;&#x7528;&#x4e8e;&#x9009;&#x62e9;&#x5668;&#x5185;&#x90e8;&#x7684;&#x9009;&#x62e9;&#x5668;&#x6837;&#x5f0f;">
<node CREATED="1466067218704" ID="ID_265396027" MODIFIED="1466067293604" TEXT="p&#xa;{&#xa;color:blue;&#xa;text-align:center;&#xa;}&#xa;&#xa;.marked&#xa;{&#xa;background-color:red;&#xa;}&#xa;&#xa;.marked p&#xa;{&#xa;color:white;&#xa;}">
<node CREATED="1466067298155" ID="ID_436865444" MODIFIED="1466067422562" TEXT="&#x5b9a;&#x4e49;&#x4e86;.marked&#x9009;&#x62e9;&#x5668;&#x4e2d;p&#x6807;&#x7b7e;&#x9009;&#x62e9;&#x5668;color&#x5c5e;&#x6027;&#x7528;&#x4e8e;&#x8986;&#x76d6;&#x4e0a;&#x9762;&#x5168;&#x5c40;p&#x6807;&#x7b7e;&#x9009;&#x62e9;&#x5668;&#x7684;color&#x5c5e;&#x6027;"/>
</node>
</node>
</node>
</node>
<node CREATED="1465907297832" ID="ID_1819991596" MODIFIED="1465907312112" TEXT="&#x5c42;&#x53e0;&#x6b21;&#x5e8f;">
<node CREATED="1465907312923" ID="ID_583991503" MODIFIED="1465910471120">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      1.&#27983;&#35272;&#22120;&#32570;&#30465;&#35774;&#32622;
    </p>
    <p>
      2.&#22806;&#37096;&#26679;&#24335;&#34920;
    </p>
    <p>
      3.&#20869;&#37096;&#26679;&#24335;&#34920;(&#20301;&#20110;&lt;head&gt;&#26631;&#31614;&#20869;&#37096;)
    </p>
    <p>
      4.&#20869;&#32852;&#26679;&#24335;(&#22312;HTML&#20803;&#32032;&#20869;&#37096;&#20351;&#29992;stype=&quot;width:200px;..&quot;)
    </p>
  </body>
</html></richcontent>
<node CREATED="1465907447083" ID="ID_1429672243" MODIFIED="1465907468235" TEXT="&#x5185;&#x8054;&#x6837;&#x5f0f;&#x4f18;&#x5148;&#x7ea7;&#x6700;&#x9ad8;"/>
</node>
</node>
<node CREATED="1466066818860" ID="ID_1190060921" MODIFIED="1466066832098" TEXT="css&#x5206;&#x7ec4;">
<node CREATED="1466066833921" ID="ID_938917448" MODIFIED="1466066893602" TEXT="h1&#xa;{&#xa;color:green;&#xa;}&#xa;h2&#xa;{&#xa;color:green;&#xa;}&#xa;p&#xa;{&#xa;color:green;&#xa;}">
<node CREATED="1466066895342" ID="ID_116458448" MODIFIED="1466066904245" TEXT="&#x5206;&#x7ec4;&#x540e;">
<node CREATED="1466066904247" ID="ID_301938983" MODIFIED="1466066924278" TEXT="h1,h2,p&#xa;{&#xa;color:green;&#xa;}">
<node CREATED="1466066931234" ID="ID_1358302894" MODIFIED="1466067010491" TEXT="&#x901a;&#x8fc7;&#x5206;&#x7ec4;&#x5b9a;&#x4e49;&#x4e86;&#x591a;&#x4e2a;&#x6807;&#x7b7e;&#x6837;&#x5f0f;&#x51cf;&#x5c11;&#x4e86;&#x4ee3;&#x7801;&#x91cf;"/>
</node>
</node>
</node>
</node>
<node CREATED="1466067696713" ID="ID_893556619" MODIFIED="1466067703901" TEXT="css&#x76d2;&#x5b50;&#x6a21;&#x578b;">
<node CREATED="1466067723038" ID="ID_243836853" MODIFIED="1466068654565" TEXT="Margin(&#x5916;&#x8fb9;&#x8ddd;)-&#x6e05;&#x9664;&#x8fb9;&#x6846;&#x5916;&#x7684;&#x533a;&#x57df;,&#x5916;&#x8fb9;&#x8ddd;&#x662f;&#x900f;&#x660e;&#x7684;&#xa;Border(&#x8fb9;&#x6846;)-&#x56f4;&#x7ed5;&#x5728;&#x5185;&#x8fb9;&#x8ddd;&#x548c;&#x5185;&#x5bb9;&#x5916;&#x7684;&#x8fb9;&#x6846;.&#xa;Padding(&#x5185;&#x8fb9;&#x8ddd;)-&#x6e05;&#x9664;&#x5185;&#x5bb9;&#x5468;&#x56f4;&#x7684;&#x533a;&#x57df;,&#x5185;&#x8fb9;&#x8ddd;&#x662f;&#x900f;&#x660e;&#x7684;&#xa;Content(&#x5185;&#x5bb9;)-&#x4f8b;&#x5b50;&#x7684;&#x5185;&#x5bb9;,&#x663e;&#x793a;&#x6587;&#x672c;&#x548c;&#x56fe;&#x50cf;">
<node CREATED="1466069466442" ID="ID_508401734" MODIFIED="1466070353894" TEXT="&lt;head&gt;&#xa;&lt;style&gt;&#xa;.ex&#xa;{&#xa;width:220px;&#xa;padding:10px;  #&#x4e0a;&#x53f3;&#x4e0b;&#x5de6;&#x5185;&#x8fb9;&#x8ddd;&#x662f;10&#x4e2a;&#x50cf;&#x7d20;&#xa;border:5px solid gray;  #&#x4e0a;&#x53f3;&#x4e0b;&#x5de6;&#x8fb9;&#x6846;&#x662f;5&#x4e2a;&#x50cf;&#x7d20;,&#x5e76;&#x4e14;&#x989c;&#x8272;&#x4e3a;&#x7070;&#x8272;&#xa;margin:0px; #&#x4e0a;&#x53f3;&#x4e0b;&#x5de6;&#x5916;&#x8fb9;&#x8ddd;&#x662f;0&#x50cf;&#x7d20;&#xa;}&#xa;&lt;/style&gt;&#xa;&lt;/head&gt;">
<node CREATED="1466069656714" ID="ID_1827594841" MODIFIED="1466069704646" TEXT="&#x8fd9;&#x91cc;&#x8fd9;&#x4e2a;&#x6837;&#x5f0f;&#x5b9a;&#x4e49;&#x7684;&#x603b;&#x5bbd;&#x5ea6;&#x4e3a;220+20+10=250px">
<node CREATED="1466069898597" ID="ID_233905356" MODIFIED="1466070068502" TEXT="* {   #&#x5168;&#x5c40;&#x6837;&#x5f0f;&#x9009;&#x62e9;&#x5668;&#xa;    padding: 0;  #&#x5185;&#x8fb9;&#x8ddd;&#x4e3a;0&#x50cf;&#x7d20;&#xa;    margin: 0;  #&#x5916;&#x8fb9;&#x8ddd;&#x4e3a;0&#x50cf;&#x7d20;&#xa;}">
<node CREATED="1466070073515" ID="ID_156300532" MODIFIED="1466070120643" TEXT="&#x8bbe;&#x7f6e;&#x5168;&#x5c40;&#x6837;&#x5f0f;,&#x53d6;&#x6d88;&#x5185;&#x5916;&#x8fb9;&#x8ddd;&#x5360;&#x4f4d;"/>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1466061498561" ID="ID_1443738631" MODIFIED="1466061532806" TEXT="&#x6ce8;&#x91ca;">
<node CREATED="1466061542505" ID="ID_658232534" MODIFIED="1466061600545" TEXT="&#x6ce8;&#x91ca;&#x662f;&#x7528;&#x6765;&#x89e3;&#x91ca;&#x4f60;&#x7684;&#x4ee3;&#x7801;,&#x5e76;&#x4e14;&#x53ef;&#x4ee5;&#x968f;&#x610f;&#x7f16;&#x8f91;&#x5b83;,&#x6d4f;&#x89c8;&#x5668;&#x4f1a;&#x5ffd;&#x7565;&#x5b83;.">
<node CREATED="1466061623547" ID="ID_1231217012" MODIFIED="1466061870708" TEXT="/*&#x8fd9;&#x662f;&#x4e2a;&#x6ce8;&#x91ca;*/&#xa;p&#xa;{&#xa;text-align:center;    #&#x5c45;&#x4e2d;&#xa;/*&#x8fd9;&#x662f;&#x53e6;&#x4e00;&#x4e2a;&#x6ce8;&#x91ca;*/&#xa;color:black;  #&#x5b57;&#x4f53;&#x989c;&#x8272;&#xa;font-family:arial;  #&#x4ec0;&#x4e48;&#x5b57;&#x4f53;&#xa;}"/>
</node>
</node>
<node CREATED="1466065872015" ID="ID_1102703203" MODIFIED="1466065884680" TEXT="&#x5e38;&#x7528;&#x5c5e;&#x6027;">
<node CREATED="1466065907812" ID="ID_1952530688" MODIFIED="1466066292491" TEXT="background: &#x80cc;&#x666f;&#xa;background-attachme: &#x80cc;&#x666f;&#x56fe;&#x6027;&#x662f;&#x5426;&#x56fa;&#x5b9a;&#xa;background-color: &#x80cc;&#x666f;&#x989c;&#x8272;&#xa;background-image:&#x80cc;&#x666f;&#x56fe;&#x7247;&#xa;background-position:&#x80cc;&#x666f;&#x56fe;&#x4f4d;&#x7f6e;&#xa;background-repeat:&#x80cc;&#x666f;&#x662f;&#x5426;&#x91cd;&#x590d;&#xa;width:&#x5bbd;&#x5ea6;&#xa;height:&#x9ad8;&#x5ea6;&#xa;z-index: z&#x8f74;&#x9ad8;&#x5ea6;&#xa;font:&#x6587;&#x5b57;&#x8bbe;&#x5b9a;&#xa;font-family:&#x5b57;&#x4f53;&#xa;font-size:&#x5b57;&#x4f53;&#x5927;&#x5c0f;&#xa;font-style:&#x5b57;&#x5f62;&#x6837;&#x5f0f;&#xa;text-align:&#x5b57;&#x7b26;&#x5bf9;&#x9f50;&#xa;border: &#x8868;&#x683c;&#x8fb9;&#x6846;&#x8bbe;&#x5b9a;&#xa;border-color: &#x8fb9;&#x6846;&#x989c;&#x8272;&#xa;border-width:&#x8fb9;&#x6846;&#x5bbd;&#x5ea6;&#xa;padding:&#x8fb9;&#x6846;&#x8865;&#x767d;"/>
</node>
</node>
<node CREATED="1466088078551" ID="ID_164320530" MODIFIED="1466088127556" POSITION="right" TEXT="bootstrap">
<node CREATED="1466088273447" ID="ID_1888524364" MODIFIED="1466088453567">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;head&gt;
    </p>
    <p>
      &lt;link rel=&quot;stylesheet&quot; href=&quot;http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css&quot;&gt;
    </p>
    <p>
      &lt;/head&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1466088468126" ID="ID_317892324" MODIFIED="1466088488941" TEXT="&#x5f15;&#x5165;bootstraps&#x6837;&#x5f0f;"/>
</node>
<node CREATED="1466090205244" ID="ID_223570947" MODIFIED="1466090277748" TEXT="bootstrap&#x9700;&#x8981;&#x4e3a;&#x9875;&#x9762;&#x5185;&#x5bb9;&#x548c;&#x6805;&#x683c;&#x7cfb;&#x7edf;&#x5305;&#x88f9;&#x4e00;&#x4e2a;&#x5e03;&#x5c40;&#x5bb9;&#x5668;">
<node CREATED="1466089988349" ID="ID_28826765" MODIFIED="1466090115483">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;div class=&quot;container&quot;&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;...
    </p>
    <p>
      &lt;/div&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1466090408363" ID="ID_1637856991" MODIFIED="1466090472073" TEXT=".container &#x7c7b;&#x7528;&#x4e8e;&#x56fa;&#x5b9a;&#x5bbd;&#x5ea6;&#x5e76;&#x652f;&#x6301;&#x54cd;&#x5e94;&#x5f0f;&#x5e03;&#x5c40;&#x7684;&#x5bb9;&#x5668;"/>
</node>
<node CREATED="1466090298664" ID="ID_164165339" MODIFIED="1466090355825">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;div class=&quot;container-fluid&quot;&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;...
    </p>
    <p>
      &lt;/div&gt;
    </p>
  </body>
</html></richcontent>
<node CREATED="1466090477958" ID="ID_391588390" MODIFIED="1466090533916" TEXT=".container-fluid&#x7c7b;&#x7528;100%&#x5bbd;&#x5ea6;&#x7684;&#x5bb9;&#x5668;"/>
</node>
</node>
<node CREATED="1466227352577" ID="ID_469929142" MODIFIED="1466227365018" TEXT="&#x6805;&#x683c;&#x7cfb;&#x7edf;">
<node CREATED="1466227369063" ID="ID_56744509" MODIFIED="1466228627189">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#36890;&#36807;&#19968;&#24207;&#21015;&#30340;&#34892;(row)&#19982;&#21015;(column)&#30340;&#32452;&#21512;
    </p>
    <p>
      &#26469;&#21019;&#24314;&#39029;&#38754;&#24067;&#23616;&#12290;&#21487;&#20197;&#29702;&#35299;&#20026;&#25972;&#20010;&#39029;&#38754;&#23601;
    </p>
    <p>
      &#26159;&#19968;&#20010;&#34920;&#26684;&#12290;
    </p>
  </body>
</html>
</richcontent>
<node CREATED="1466227634659" ID="ID_1999577370" MODIFIED="1466227768389" TEXT="&#x884c;(row)&#x5fc5;&#x987b;&#x5305;&#x542b;&#x5728;.container(&#x56fa;&#x5b9a;&#x5bbd;&#x5bbd;)&#x6216;.container-fluid(100%&#x5bbd;&#x5ea6;)&#x4e2d;"/>
<node CREATED="1466227782404" ID="ID_67599493" MODIFIED="1466228557236">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#36890;&#36807;&#34892;(row)&#22312;&#27700;&#24179;&#26041;&#21521;&#21019;&#24314;&#19968;&#32452;&quot;&#21015;&quot;(column),&#21482;&#26377;
    </p>
    <p>
      &quot;&#21015;(column)&#21487;&#20197;&#20316;&#20026;&#34892;(row)&quot;&#30340;&#30452;&#25509;&#23376;&#20803;&#32032;
    </p>
  </body>
</html></richcontent>
<node CREATED="1466229278995" ID="ID_298099334" MODIFIED="1466231861363" TEXT="&#x4e00;&#x884c;(row)&#x6700;&#x591a;12&#x5217;(column), &#x652f;&#x6301;&#x5d4c;&#x5957;">
<node CREATED="1466229616757" ID="ID_276353474" MODIFIED="1466229676167" TEXT="&#x6839;&#x636e;&#x663e;&#x793a;&#x5c4f;&#x5927;&#x5c0f;&#x9009;&#x62e9;&#x9002;&#x5408;&#x7684;&#x7c7b;&#x9009;&#x62e9;&#x5668;">
<node CREATED="1466229472906" ID="ID_1001208455" MODIFIED="1466229613144">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      .col-xs-&#160;&#160;&#160;#&#36229;&#23567;&#23631;&#24149; &#25163;&#26426;
    </p>
    <p>
      .col-sm-&#160;&#160;#&#23567;&#23631;&#24149; &#24179;&#26495;
    </p>
    <p>
      .col-md-&#160;&#160;#&#20013;&#31561;&#23631;&#24149; &#26700;&#38754;&#26174;&#31034;&#22120;
    </p>
    <p>
      .col-lg-&#160;&#160;&#160;#&#22823;&#23631;&#24149; &#22823;&#26700;&#38754;&#26174;&#31034;&#22120;
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1466231200313" ID="ID_1544995208" MODIFIED="1466231271918" TEXT="&#x5217;(column)&#x504f;&#x79fb;&#xff0c;&#x8bbe;&#x7f6e;&#x504f;&#x79fb;&#x591a;&#x5c11;&#x5217;">
<node CREATED="1466231273938" ID="ID_1550115237" MODIFIED="1466231345943" TEXT="&lt;div class=&quot;col-md-4 col-md-offset-2&quot;&gt;4&#x5217;&#x5143;&#x7d20;&lt;/div&gt;"/>
</node>
</node>
</node>
<node CREATED="1466228654187" ID="ID_1489864829" MODIFIED="1466238600291">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;!DOCTYPE html&gt;
    </p>
    <p>
      &lt;html&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&lt;head&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;meta charset=&quot;utf-8&quot; /&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;title&gt;&#23398;&#20064;bootstrap&lt;/title&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;link rel=&quot;stylesheet&quot; href=&quot;http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css&quot;&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&lt;/head&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&lt;body&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;container-fluid&quot;&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;row&quot;&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;col-md-2'&gt;2&#21015;&#30340;&#20803;&#32032;&lt;/div&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;col-md-4&quot;&gt;4&#21015;&#30340;&#20803;&#32032;&lt;/div&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;col-md-6&quot;&gt;6&#21015;&#30340;&#20803;&#32032;&lt;/div&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/div&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/div&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&lt;/body&gt;
    </p>
    <p>
      &lt;/html&gt;
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
</node>
<node CREATED="1466236867526" ID="ID_196186829" MODIFIED="1466236943285" TEXT="label&#x6807;&#x7b7e;">
<node CREATED="1466236945051" ID="ID_549360686" MODIFIED="1466237019735" TEXT="&#x4e00;&#x5b9a;&#x8981;&#x6dfb;&#x52a0;label&#x6807;&#x7b7e;"/>
<node CREATED="1466237021868" ID="ID_546849486" MODIFIED="1466237557878" TEXT="label&#x8bbe;&#x7f6e;,&#x8fd9;&#x662f;bootstrap&#x89c4;&#x8303;.sr-only&#x7c7b;&#x5c06;&#x5176;&#x9690;&#x85cf;">
<node CREATED="1466237188595" ID="ID_1607272" MODIFIED="1466237492366">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &lt;form&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&lt;div class=&quot;form-group&quot;&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;lable for=&quot;exampleInputEmail&quot;&gt;Email address&lt;/lable&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;input type=&quot;email&quot; class=&quot;form-control&quot; id=&quot;exampleInputEmail&quot; placeholder=&quot;Email&quot;&gt;
    </p>
    <p>
      &#160;&#160;&#160;&#160;&lt;/div&gt;
    </p>
    <p>
      &lt;/form&gt;
    </p>
  </body>
</html>
</richcontent>
<node CREATED="1466237775820" ID="ID_968075015" MODIFIED="1466238305069" TEXT="placeholder&#x5c5e;&#x6027;&#x4f5c;&#x7528;&#x662f;&#x5b9a;&#x4e49;&#x8f93;&#x5165;&#x6846;&#x7684;&#x9ed8;&#x8ba4;&#x63d0;&#x793a;"/>
<node CREATED="1466238310262" ID="ID_1571839447" MODIFIED="1466238360916" TEXT="lable&#x6807;&#x7b7e;&#x4e2d;&#x7684;for&#x503c;&#x548c;input&#x6807;&#x7b7e;&#x4e2d;&#x7684;id&#x503c;&#x4e00;&#x4e00;&#x5bf9;&#x5e94;"/>
</node>
</node>
</node>
</node>
</node>
</map>
