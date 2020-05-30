# 26 Python的is

# is是对比地址,==是对比值

# 27 read,readline和readlines

# read 读取整个文件
# readline 读取下一行,使用生成器方法
# readlines 读取整个文件到一个迭代器以供我们遍历
# 28 Python2和3的区别

# 推荐：Python 2.7.x 与 Python 3.x 的主要差异

# 29 super init

# super() lets you avoid referring to the base class explicitly, which can be nice. But the main advantage comes with multiple inheritance, where all sorts of fun stuff can happen. See the standard docs on super if you haven’t already.

# Note that the syntax changed in Python 3.0: you can just say super().__init__() instead of super(ChildB, self).__init__() which IMO is quite a bit nicer.

# http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

# Python2.7中的super方法浅见

# 30 range and xrange

# 都在循环时使用，xrange内存性能更好。
# for i in range(0, 20):
# for i in xrange(0, 20):
# What is the difference between range and xrange functions in Python 2.X?
# range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.
# xrange is a sequence object that evaluates lazily.

# http://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x

# 操作系统

# 1 select,poll和epoll

# 其实所有的I/O都是轮询的方法,只不过实现的层面不同罢了.

# 这个问题可能有点深入了,但相信能回答出这个问题是对I/O多路复用有很好的了解了.其中tornado使用的就是epoll的.

# selec,poll和epoll区别总结

# 基本上select有3个缺点:

# 连接数受限
# 查找配对速度慢
# 数据由内核拷贝到用户态
# poll改善了第一个缺点

# epoll改了三个缺点.

# 关于epoll的: http://www.cnblogs.com/my_life/articles/3968782.html

# 2 调度算法

# 先来先服务(FCFS, First Come First Serve)
# 短作业优先(SJF, Shortest Job First)
# 最高优先权调度(Priority Scheduling)
# 时间片轮转(RR, Round Robin)
# 多级反馈队列调度(multilevel feedback queue scheduling)
# 常见的调度算法总结:http://www.jianshu.com/p/6edf8174c1eb

# 实时调度算法:

# 最早截至时间优先 EDF
# 最低松弛度优先 LLF
# 3 死锁

# 原因:

# 竞争资源
# 程序推进顺序不当
# 必要条件:

# 互斥条件
# 请求和保持条件
# 不剥夺条件
# 环路等待条件
# 处理死锁基本方法:

# 预防死锁(摒弃除1以外的条件)
# 避免死锁(银行家算法)
# 检测死锁(资源分配图)
# 解除死锁
# 剥夺资源
# 撤销进程
# 死锁概念处理策略详细介绍:https://wizardforcel.gitbooks.io/wangdaokaoyan-os/content/10.html

# 4 程序编译与链接

# 推荐: http://www.ruanyifeng.com/blog/2014/11/compiler.html

# Bulid过程可以分解为4个步骤:预处理(Prepressing), 编译(Compilation)、汇编(Assembly)、链接(Linking)

# 以c语言为例:

# 1 预处理

# 预编译过程主要处理那些源文件中的以“#”开始的预编译指令，主要处理规则有：

# 将所有的“#define”删除，并展开所用的宏定义
# 处理所有条件预编译指令，比如“#if”、“#ifdef”、 “#elif”、“#endif”
# 处理“#include”预编译指令，将被包含的文件插入到该编译指令的位置，注：此过程是递归进行的
# 删除所有注释
# 添加行号和文件名标识，以便于编译时编译器产生调试用的行号信息以及用于编译时产生编译错误或警告时可显示行号
# 保留所有的#pragma编译器指令。
# 2 编译

# 编译过程就是把预处理完的文件进行一系列的词法分析、语法分析、语义分析及优化后生成相应的汇编代码文件。这个过程是整个程序构建的核心部分。

# 3 汇编

# 汇编器是将汇编代码转化成机器可以执行的指令，每一条汇编语句几乎都是一条机器指令。经过编译、链接、汇编输出的文件成为目标文件(Object File)

# 4 链接

# 链接的主要内容就是把各个模块之间相互引用的部分处理好，使各个模块可以正确的拼接。
# 链接的主要过程包块 地址和空间的分配（Address and Storage Allocation）、符号决议(Symbol Resolution)和重定位(Relocation)等步骤。

# 5 静态链接和动态链接

# 静态链接方法：静态链接的时候，载入代码就会把程序会用到的动态代码或动态代码的地址确定下来
# 静态库的链接可以使用静态链接，动态链接库也可以使用这种方法链接导入库

# 动态链接方法：使用这种方式的程序并不在一开始就完成动态链接，而是直到真正调用动态库代码时，载入程序才计算(被调用的那部分)动态代码的逻辑地址，然后等到某个时候，程序又需要调用另外某块动态代码时，载入程序又去计算这部分代码的逻辑地址，所以，这种方式使程序初始化时间较短，但运行期间的性能比不上静态链接的程序

# 6 虚拟内存技术

# 虚拟存储器是指具有请求调入功能和置换功能,能从逻辑上对内存容量加以扩充的一种存储系统.

# 7 分页和分段

# 分页: 用户程序的地址空间被划分成若干固定大小的区域，称为“页”，相应地，内存空间分成若干个物理块，页和块的大小相等。可将用户程序的任一页放在内存的任一块中，实现了离散分配。

# 分段: 将用户程序地址空间分成若干个大小不等的段，每段可以定义一组相对完整的逻辑信息。存储分配时，以段为单位，段与段在内存中可以不相邻接，也实现了离散分配。

# 分页与分段的主要区别

# 页是信息的物理单位,分页是为了实现非连续分配,以便解决内存碎片问题,或者说分页是由于系统管理的需要.段是信息的逻辑单位,它含有一组意义相对完整的信息,分段的目的是为了更好地实现共享,满足用户的需要.
# 页的大小固定,由系统确定,将逻辑地址划分为页号和页内地址是由机器硬件实现的.而段的长度却不固定,决定于用户所编写的程序,通常由编译程序在对源程序进行编译时根据信息的性质来划分.
# 分页的作业地址空间是一维的.分段的地址空间是二维的.
# 8 页面置换算法

# 最佳置换算法OPT:不可能实现
# 先进先出FIFO
# 最近最久未使用算法LRU:最近一段时间里最久没有使用过的页面予以置换.
# clock算法
# 9 边沿触发和水平触发

# 边缘触发是指每当状态变化时发生一个 io 事件，条件触发是只要满足条件就发生一个 io 事件

# 数据库

# 1 事务

# 数据库事务(Database Transaction) ，是指作为单个逻辑工作单元执行的一系列操作，要么完全地执行，要么完全地不执行。
# 彻底理解数据库事务: http://www.hollischuang.com/archives/898

# 2 数据库索引

# 推荐: http://tech.meituan.com/mysql-index.html

# MySQL索引背后的数据结构及算法原理

# 聚集索引,非聚集索引,B-Tree,B+Tree,最左前缀原理

# 3 Redis原理

# Redis是什么？

# 是一个完全开源免费的key-value内存数据库
# 通常被认为是一个数据结构服务器，主要是因为其有着丰富的数据结构 strings、map、 list、sets、 sorted sets
# Redis数据库

# ​ 通常局限点来说，Redis也以消息队列的形式存在，作为内嵌的List存在，满足实时的高并发需求。在使用缓存的时候，redis比memcached具有更多的优势，并且支持更多的数据类型，把redis当作一个中间存储系统，用来处理高并发的数据库操作

# 速度快：使用标准C写，所有数据都在内存中完成，读写速度分别达到10万/20万
# 持久化：对数据的更新采用Copy-on-write技术，可以异步地保存到磁盘上，主要有两种策略，一是根据时间，更新次数的快照（save 300 10 ）二是基于语句追加方式(Append-only file，aof)
# 自动操作：对不同数据类型的操作都是自动的，很安全
# 快速的主–从复制，官方提供了一个数据，Slave在21秒即完成了对Amazon网站10G key set的复制。
# Sharding技术： 很容易将数据分布到多个Redis实例中，数据库的扩展是个永恒的话题，在关系型数据库中，主要是以添加硬件、以分区为主要技术形式的纵向扩展解决了很多的应用场景，但随着web2.0、移动互联网、云计算等应用的兴起，这种扩展模式已经不太适合了，所以近年来，像采用主从配置、数据库复制形式的，Sharding这种技术把负载分布到多个特理节点上去的横向扩展方式用处越来越多。
# Redis缺点

# 是数据库容量受到物理内存的限制,不能用作海量数据的高性能读写,因此Redis适合的场景主要局限在较小数据量的高性能操作和运算上。
# Redis较难支持在线扩容，在集群容量达到上限时在线扩容会变得很复杂。为避免这一问题，运维人员在系统上线时必须确保有足够的空间，这对资源造成了很大的浪费。
# 4 乐观锁和悲观锁

# 悲观锁：假定会发生并发冲突，屏蔽一切可能违反数据完整性的操作

# 乐观锁：假设不会发生并发冲突，只在提交操作时检查是否违反数据完整性。

# 乐观锁与悲观锁的具体区别: http://www.cnblogs.com/Bob-FD/p/3352216.html

# 5 MVCC

# ​ 全称是Multi-Version Concurrent Control，即多版本并发控制，在MVCC协议下，每个读操作会看到一个一致性的snapshot，并且可以实现非阻塞的读。MVCC允许数据具有多个版本，这个版本可以是时间戳或者是全局递增的事务ID，在同一个时间点，不同的事务看到的数据是不同的。

# MySQL的innodb引擎是如何实现MVCC的

# innodb会为每一行添加两个字段，分别表示该行创建的版本和删除的版本，填入的是事务的版本号，这个版本号随着事务的创建不断递增。在repeated read的隔离级别（事务的隔离级别请看这篇文章）下，具体各种数据库操作的实现：

# select：满足以下两个条件innodb会返回该行数据：
# 该行的创建版本号小于等于当前版本号，用于保证在select操作之前所有的操作已经执行落地。
# 该行的删除版本号大于当前版本或者为空。删除版本号大于当前版本意味着有一个并发事务将该行删除了。
# insert：将新插入的行的创建版本号设置为当前系统的版本号。
# delete：将要删除的行的删除版本号设置为当前系统的版本号。
# update：不执行原地update，而是转换成insert + delete。将旧行的删除版本号设置为当前版本号，并将新行insert同时设置创建版本号为当前版本号。
# 其中，写操作（insert、delete和update）执行时，需要将系统版本号递增。

# ​ 由于旧数据并不真正的删除，所以必须对这些数据进行清理，innodb会开启一个后台线程执行清理工作，具体的规则是将删除版本号小于当前系统版本的行删除，这个过程叫做purge。

# 通过MVCC很好的实现了事务的隔离性，可以达到repeated read级别，要实现serializable还必须加锁。

# 参考：MVCC浅析