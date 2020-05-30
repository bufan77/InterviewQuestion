# 5 去除列表中的重复元素

# 用集合

# list(set(l))

# 用字典

# l1 = ['b','c','d','b','c','a','a']

# l2 = {}.fromkeys(l1).keys()

# print l2

# 用字典并保持顺序

# l1 = ['b','c','d','b','c','a','a']

# l2 = list(set(l1))

# l2.sort(key=l1.index)

# print l2

# 列表推导式

# l1 = ['b','c','d','b','c','a','a']

# l2 = []

# [l2.append(i) for i in l1 if not i in l2]

# sorted排序并且用列表推导式.

# l = [‘b’,’c’,’d’,’b’,’c’,’a’,’a’]
# [single.append(i) for i in sorted(l) if i not in single]
# print single

# 6 链表成对调换

# 1->2->3->4转换成2->1->4->3.

# class ListNode:

#     def __init__(self, x):

#         self.val = x

#         self.next = None

 

# class Solution:

#     # @param a ListNode

#     # @return a ListNode

#     def swapPairs(self, head):

#         if head != None and head.next != None:

#             next = head.next

#             head.next = self.swapPairs(next.next)

#             next.next = head

#             return next

#         return head

# 7 创建字典的方法

# 1 直接创建

# dict = {'name':'earth', 'port':'80'}

# 2 工厂方法

# items=[('name','earth'),('port','80')]

# dict2=dict(items)

# dict1=dict((['name','earth'],['port','80']))

# 3 fromkeys()方法

# dict1={}.fromkeys(('x','y'),-1)

# dict={'x':-1,'y':-1}

# dict2={}.fromkeys(('x','y'))

# dict2={'x':None, 'y':None}

# 8 合并两个有序列表

# 知乎远程面试要求编程

# 尾递归

# def _recursion_merge_sort2(l1, l2, tmp):

#     if len(l1) == 0 or len(l2) == 0:

#         tmp.extend(l1)

#         tmp.extend(l2)

#         return tmp

#     else:

#         if l1[0] < l2[0]:

#             tmp.append(l1[0])

#             del l1[0]

#         else:

#             tmp.append(l2[0])

#             del l2[0]

#         return _recursion_merge_sort2(l1, l2, tmp)

 

# def recursion_merge_sort2(l1, l2):

#     return _recursion_merge_sort2(l1, l2, [])

# 循环算法

# 思路：

# 定义一个新的空列表

# 比较两个列表的首个元素

# 小的就插入到新列表里

# 把已经插入新列表的元素从旧列表删除

# 直到两个旧列表有一个为空

# 再把旧列表加到新列表后面

# def loop_merge_sort(l1, l2):

#     tmp = []

#     while len(l1) > 0 and len(l2) > 0:

#         if l1[0] < l2[0]:

#             tmp.append(l1[0])

#             del l1[0]

#         else:

#             tmp.append(l2[0])

#             del l2[0]

#     tmp.extend(l1)

#     tmp.extend(l2)

#     return tmp

# pop弹出

# a = [1,2,3,7]

# b = [3,4,5]

 

# def merge_sortedlist(a,b):

#     c = []

#     while a and b:

#         if a[0] >= b[0]:

#             c.append(b.pop(0))

#         else:

#             c.append(a.pop(0))

#     while a:

#         c.append(a.pop(0))

#     while b:

#         c.append(b.pop(0))

#     return c

# print merge_sortedlist(a,b)

 

# 9 交叉链表求交点

# 其实思想可以按照从尾开始比较两个链表，如果相交，则从尾开始必然一致，只要从尾开始比较，直至不一致的地方即为交叉点，如图所示

 

# # 使用a,b两个list来模拟链表，可以看出交叉点是 7这个节点

# a = [1,2,3,7,9,1,5]

# b = [4,5,7,9,1,5]

 

# for i in range(1,min(len(a),len(b))):

#     if i==1 and (a[-1] != b[-1]):

#         print "No"

#         break

#     else:

#         if a[-i] != b[-i]:

#             print "交叉节点：",a[-i+1]

#             break

#         else:

#             pass

# 另外一种比较正规的方法，构造链表类

# class ListNode:

#     def __init__(self, x):

#         self.val = x

#         self.next = None

# def node(l1, l2):

#     length1, lenth2 = 0, 0

#     # 求两个链表长度

#     while l1.next:

#         l1 = l1.next

#         length1 += 1

#     while l2.next:

#         l2 = l2.next

#         length2 += 1

#     # 长的链表先走

#     if length1 > lenth2:

#         for _ in range(length1 - length2):

#             l1 = l1.next

#     else:

#         for _ in range(length2 - length1):

#             l2 = l2.next

#     while l1 and l2:

#         if l1.next == l2.next:

#             return l1.next

#         else:

#             l1 = l1.next

#             l2 = l2.next

# 修改了一下:

# #coding:utf-8

# class ListNode:

#     def __init__(self, x):

#         self.val = x

#         self.next = None

 

# def node(l1, l2):

#     length1, length2 = 0, 0

#     # 求两个链表长度

#     while l1.next:

#         l1 = l1.next#尾节点

#         length1 += 1

#     while l2.next:

#         l2 = l2.next#尾节点

#         length2 += 1

 

#     #如果相交

#     if l1.next == l2.next:

#         # 长的链表先走

#         if length1 > length2:

#             for _ in range(length1 - length2):

#                 l1 = l1.next

#             return l1#返回交点

#         else:

#             for _ in range(length2 - length1):

#                 l2 = l2.next

#             return l2#返回交点

#     # 如果不相交

#     else:

#         return

# 思路: http://humaoli.blog.163.com/blog/static/13346651820141125102125995/

