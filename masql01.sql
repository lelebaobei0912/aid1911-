CREATE USER 'vip'@'%' IDENTIFIED BY '123';

grant all privileges on stu.cls to 'vip'@'%' identified by '123';


grant all privileges on stu.cls to 'vip'@'%' identified by '123' with grant option ;
移除权限
revoke delete on stu.cls from 'vip'@'%';
删除用户
drop user 'vip'@'%';

"""

"""
