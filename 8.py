# 5 去除列表中的重复元素

# 用集合

# list(set(l))

# 用字典

# l1 = ['b','c','d','b','c','a','a']

# l2 = {}.fromkeys(l1).keys()

# print l2

# 用字典并保持顺序

# l1 = ['b','c','d','b','c','a','a']

# l2 = list(set(l1))

# l2.sort(key=l1.index)

# print l2

# 列表推导式

# l1 = ['b','c','d','b','c','a','a']

# l2 = []

# [l2.append(i) for i in l1 if not i in l2]

# sorted排序并且用列表推导式.

# l = [‘b’,’c’,’d’,’b’,’c’,’a’,’a’]
# [single.append(i) for i in sorted(l) if i not in single]
# print single

# 6 链表成对调换

# 1->2->3->4转换成2->1->4->3.

# class ListNode:

#     def __init__(self, x):

#         self.val = x

#         self.next = None


# class Solution:

#     # @param a ListNode

#     # @return a ListNode

#     def swapPairs(self, head):

#         if head != None and head.next != None:

#             next = head.next

#             head.next = self.swapPairs(next.next)

#             next.next = head

#             return next

#         return head

# 7 创建字典的方法

# 1 直接创建

# dict = {'name':'earth', 'port':'80'}

# 2 工厂方法

# items=[('name','earth'),('port','80')]

# dict2=dict(items)

# dict1=dict((['name','earth'],['port','80']))

# 3 fromkeys()方法

# dict1={}.fromkeys(('x','y'),-1)

# dict={'x':-1,'y':-1}

# dict2={}.fromkeys(('x','y'))

# dict2={'x':None, 'y':None}

# 8 合并两个有序列表

# 知乎远程面试要求编程

# 尾递归

# def _recursion_merge_sort2(l1, l2, tmp):

#     if len(l1) == 0 or len(l2) == 0:

#         tmp.extend(l1)

#         tmp.extend(l2)

#         return tmp

#     else:

#         if l1[0] < l2[0]:

#             tmp.append(l1[0])

#             del l1[0]

#         else:

#             tmp.append(l2[0])

#             del l2[0]

#         return _recursion_merge_sort2(l1, l2, tmp)


# def recursion_merge_sort2(l1, l2):

#     return _recursion_merge_sort2(l1, l2, [])

# 循环算法

# 思路：

# 定义一个新的空列表

# 比较两个列表的首个元素

# 小的就插入到新列表里

# 把已经插入新列表的元素从旧列表删除

# 直到两个旧列表有一个为空

# 再把旧列表加到新列表后面

# def loop_merge_sort(l1, l2):

#     tmp = []

#     while len(l1) > 0 and len(l2) > 0:

#         if l1[0] < l2[0]:

#             tmp.append(l1[0])

#             d