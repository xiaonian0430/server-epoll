# 网络编程 -- Epoll

epoll 是对 select、poll 模型的改进，提高了网络编程的性能，广泛应用于大规模并发请求的C/S架构中。

## 一般步骤

- Create an epoll object——创建1个 epoll 对象
- Tell the epoll object to monitor specific events on specific sockets——告诉epoll对象，在指定的socket上监听指定的事件
- Ask the epoll object which sockets may have had the specified event since the last query——询问epoll对象，从上次查询以来，哪些socket发生了哪些指定的事件
- Perform some action on those sockets——在这些socket上执行一些操作
- Tell the epoll object to modify the list of sockets and/or events to monitor——告诉epoll对象，修改socket列表和（或）事件，并监控
- Repeat steps 3 through 5 until finished——重复步骤3-5，直到完成
- Destroy the epoll object——销毁 epoll 对象


## 相关实现

1、python3 基于 python 实现的网络编程




