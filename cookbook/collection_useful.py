"""
package collection is very useful in python

namedtuple: 声明可以使用名字来访问元素内容的tuple子类。
deque: 双端队列，可以快速从另外一侧追加和推出对象
ChainMap: 类似字典（dict）的容器，将多个映射集合到一个视图里面
Counter: 字典的子类，提供了可供哈希对象计数的功能
OrderedDict: 有序字典， 保存了他们被添加的顺序
defaultdict：字典的子类，提供了一个工厂函数，为字典查询提供一个默认值
UserDict: 封装了字典对象，简化了字典子类化
UserList: 封装了列表对象，简化了列表子类化
UserString: 封装了列表对象，简化了字符串子类化

"""
import collections

collections_elem_list = ['deque', 'defaultdict', 'namedtuple',
                         'UserDict', 'UserList', 'UserString',
                         'Counter', 'OrderedDict', 'ChainMap']
print(collections.__all__)


def ChainMap_example():
    from collections import ChainMap
    baseline = {'music': 'bach', 'art': 'rembrandt'}
    adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    print(list(ChainMap(adjustments, baseline)))


def combine_multi_dict():
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    from collections import ChainMap
    c = ChainMap(a, b)
    print(c)
    print(c['x'], c['y'], c['z'])


def find_most_elem():
    """
    question: 怎样找出一个序列出现最多的元素
    USE: collection Counter
    :return:

    output: [('eyes', 8), ('the', 5), ('look', 4)]
    """
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    from collections import Counter
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)


def defaultdict_example():
    from collections import defaultdict
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(sorted(d.items()))


def OrderedDict_example():
    pass


if __name__ == "__main__":
    # find_most_elem()
    # defaultdict_example()
    combine_multi_dict()
