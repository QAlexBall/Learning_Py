import multiprocessing
import string

from .map_reduce import MapReduce

def file_to_words(filename):
    """ READ a file and return a swquence of (words, occurances) values. """

