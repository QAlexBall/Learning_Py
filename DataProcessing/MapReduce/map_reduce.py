""" map reduce """
import collections
import itertools
import multiprocessing

class MapReduce(object):


    def __init__(self, map_func, reduce_func, num_workers=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)


    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()


    def __call__(self, inputs, chunksize=1):
        # inputs 是一个需要处理的列表，chunksize表示每次给mapper的量，根据需求调整这个值
        # 第一次pool.map是为了把大任务分组
        map_responses = self.pool.map(
            self.map_func, inputs, chunksize=chunksize)
        # chain把mapper的结果链接为一个可迭代的对象
        partitioned_data = self.partition(itertools.chain(*map_responses))
        # 第二次pool.map是为了聚合结果实现reduce，map方法继续用来实现并行计算
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values
