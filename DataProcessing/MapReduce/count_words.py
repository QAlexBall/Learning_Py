import multiprocessing
import string
from .map_reduce import MapReduce


def file_to_words(filename):
    """ READ a file and return a sequence of (words, occupancies) values. """
    STOP_WORDS = {'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in', 'is', 'it', 'of', 'or', 'py', 'rst',
                  'that', 'the', 'to', 'with'}
    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    print(multiprocessing.current_process().name, 'reading', filename)
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            if line.lstrip().startswith('..'):
                continue
            line = line.trainslate(TR)
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append((word, 1))
        return output


def count_words(item):
    """ Convert the partitioned data for a word to a tuple containing the word and the number of occurances. """
    word, occurances = item
    return word, sum(occurances)


if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('*.csv')

    mapper = MapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    print('\nTOP 20 WORDS BY FREQUENCY\n')
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print('%-*s: %5s' % (longest + 1, word, count))
