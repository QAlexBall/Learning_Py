import os
import fnmatch # 用于文件名称的匹配
import gzip
import bz2
import re


def gen_find(file_pattern, top):
    """
    Find all filenames in a directory tree 
    that match a shell wildcard pattern
    """
    for path, dir_list, file_list in os.walk(top):
        for name in fnmatch.filter(file_list, file_pattern):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing file object.
    The file is closed immediately when proceeding to the next iteration.
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filenmae, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    Chain a sequence of iterators together into a single Sequnce
    """
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    """
    pattern = re.compile(pattern)
    for line in lines:
        if pattern.search(line):
            yield line


lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)