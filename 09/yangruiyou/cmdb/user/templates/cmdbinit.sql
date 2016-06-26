
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
   `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户编号',
   `username` varchar(50) DEFAULT NULL COMMENT '用户名',
   `password` varchar(50) DEFAULT NULL COMMENT '密码',
   `age` int(11) DEFAULT NULL COMMENT '年龄',
   PRIMARY KEY (`user_id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `accesslog`;

CREATE TABLE `accesslog` (
   `access_id` int(11) NOT NULL AUTO_INCREMENT,
   `ip` varchar(15) DEFAULT NULL COMMENT 'IP地址',
   `url` varchar(255) DEFAULT NULL COMMENT 'url地址',
   `code` varchar(20) DEFAULT NULL COMMENT 'http状态码',
   `cnt` varchar(50) DEFAULT NULL,
   PRIMARY KEY (`access_id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `assets`;
 
CREATE TABLE `assets` (
   `asset_id` int(11) NOT NULL AUTO_INCREMENT,
   `sn` varchar(128)   COMMENT '资产编号',
   `idc_id` int(11) NOT NULL COMMENT '机房ID',
   `ipaddr` varchar(128) NOT NULL COMMENT 'IP地址',
   `hostname` varchar(64) NOT NULL COMMENT '主机名',
   `verdor` varchar(64) DEFAULT NULL COMMENT '供应商',
   `model` varchar(64) NOT NULL COMMENT '型号',
   `admin` varchar(50) DEFAULT NULL COMMENT '使用人',
   `business` varchar(32) DEFAULT NULL COMMENT '业务',
   `cpu` int(11) NOT NULL COMMENT 'CPU核数',
   `ram` int(11) NOT NULL COMMENT '内存(G)',
   `disk` int(11) NOT NULL COMMENT '硬盘大小(G)',
   `os` varchar(50) NOT NULL COMMENT '操作系统',
   `puchase_date` datetime DEFAULT NULL COMMENT '购买时间',
   `warranty_date` datetime DEFAULT NULL COMMENT '保修时间',
   `status` tinyint(4) DEFAULT 0 COMMENT '0正常，1为删除',
   PRIMARY KEY (`asset_id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='资源表';



DROP TABLE IF EXISTS `idcs`;

CREATE TABLE `idcs` (
   `idc_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '机房编号',
   `idc_name` varchar(50) DEFAULT NULL COMMENT '机房名称',
   `idc_phone` varchar(20) COMMENT '机房联系方式'
   `status` tinyint(4) DEFAULT 0 COMMENT '0正常,1为删除',
   PRIMARY KEY (`idc_id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='IDC机房表';








