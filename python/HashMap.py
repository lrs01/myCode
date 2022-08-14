# 哈希表基于Python语言的简单实现
'''
哈希表需要实现的方法：
add(key,value)  增加元素
search(key)  查找元素
travel() 遍历整个哈希表
'''

class HashTable(object):
    """
    哈希表类
    """
    def __init__(self):
        """
        初始化
        """
        self.__key_llist = []
        self.__val_list = []

    def add(self, key, val):
        """
        添加元素
        """
        self.__key_llist.append(key)
        self.__val_list.append(val)

    def get(self, key):
        """
        搜索元素
        """
        return self.__val_list[self.__key_llist.index(key)] if key in self.__key_llist else None

    def travel(self):
        """
        遍历哈希表
        """
        for index in range(0, len(self.__key_llist)):
            print(self.__val_list[index])


if __name__ == "__main__":
    ht = HashTable()
    ht.add('asd', 123)
    ht.add('qwe', 456)
    ht.add('zxc', 789)
    print(ht.get('asd'))
    print(ht.get('wer'))
    ht.travel()


