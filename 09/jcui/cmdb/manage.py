#encoding:utf-8


from users import viers

if __name__ == '__main__':
    viers.app.run(host='0.0.0.0', port=9000, debug=True)


'''
create table assets (
id int primary key auto_increment,
sn varchar(128) default '' unique key comment 'sn编码',
ip varchar(128) default '' comment 'ip地址',
hostname varchar(64) default '' comment '主机名',
os varchar(32) default '' comment '操作系统',
cpu int not null comment 'cpu核数',
ram int not null comment '内存(G)',
disk int not null comment '硬盘大小(G)',
idc_id int comment '机房的ID',
admin varchar(32) default '' comment '使用者',
business varchar(32) default '' comment '业务',
purchase_date datetime comment '采购日期',
warranty int not null comment '保修时间(年)',
vendor varchar(64) default '' comment '供应商',
model varchar(64) default '' comment '型号',
status int default 0
) engine=INNODB default charset=utf8;
'''