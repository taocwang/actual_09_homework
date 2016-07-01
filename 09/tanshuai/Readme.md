# 资产管理
1、开发流程
    a. 需求收集
    b. 设计：表的设计；代码的设计
    c. 疯狂coding
    d. 测试
    e. 上线

2、需求收集、设计、表创建
    a. 需求分析
        idcs
            id
            name
            city
            adderss
            status              # 0 正常, 1 删除

        assets
            id                  # ID自增
            sn                  # 资产编号      varchar(128)
            ip                  # IP地址        varchar(128)
            hostname            # 主机名        varchar(64)
            idc_id              # 机房ID        int
            purchase_date       # 采购日期      datetime
            warranty            # 保修时间(年)  int
            vendor              # 供应商        varchar(64)
            model               # 型号        　varchar(64)
            admin               # 使用人        varchar(32)
            business            # 业务          varchar(32)
            cpu                 # 核数(个)      int
            ram                 # 内存(G)       int
            disk                # 磁盘大小(G)   int
            os                  # 操作系统      varchar(32)
            status              # 0 正常,1 删除 int

        # 建库SQL语句
        create table idcs (
          id int primary key auto_increment,
          name varchar(64) default '',
          status int default 0
        )default charset=utf8;

        create table assets (
          id int primary key auto_increment,
          sn varchar(128) default '' unique key comment '资产编号',
          ip varchar(128) default '' comment 'IP地址',
          hostname varchar(64) default '' comment '主机名',
          idc_id int comment '机房ID',
          purchase_date date default '0000-00-00' comment '采购日期',
          warranty int comment '保修时间(年)',
          vendor varchar(64) default '' comment '供应商',
          model varchar(64) default '' comment '型号',
          admin varchar(32) default '' comment '使用人',
          business varchar(32) default '' comment '业务',
          cpu int default 0 comment '核数(个)',
          ram int default 0 comment '内存(G) ',
          disk int default 0 comment '磁盘大小(G)',
          os varchar(32) default '' comment '操作系统',
          status int default 0 comment '0 正常,1 删除 int'
        )default charset=utf8;

    b. 写页面
        一个痛苦的过程



    c. 模版继承
    {% extends "layout.html" %} # 导入模版
    {% block title %}资产管理{% endblock %} # 下面所有都是向模版里填充内容
    {% block nav_asset %}active{% endblock %}
    {% block main %}{% endblock %}
    {% block dialog %}{% endblock %}
    {% block script %}{% endblock %}
    {% block js %}{% endblock %}
















