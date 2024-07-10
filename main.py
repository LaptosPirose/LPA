import numpy as np
from time import time


def main():
    #     zeros = np.zeros(10, dtype='uint8')
    #     print(zeros)
    #     ones = np.ones(10, dtype='uint8')
    #     print(ones)

    array_simple = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f'This is a one dimension array with pyhton numpy {array_simple}')

    print('You cans also see the performance difference between Python List and Python Numpy Arrays\
           using  time to calculate the how fast the array is.')

    print("Let's create a list with 1000 items from 0 to 1000")
    list_start = time()
    list_example = list(range(1000))
    list_end = time()
    list_time = list_end - list_start
    print(list_example)

    print("Now let's create an array with 1000 items from 0 to 1000 using Python Numpy")
    numpy_start = time()
    numpy_example = np.arange(1000)
    numpy_end = time()
    numpy_time = numpy_end - numpy_start
    print(numpy_example)

    print(f'Time using list from 0 to 1000 is :{list_time}')
    print(f'Time using array from 0 to 1000 is :{numpy_time}')

if __name__ == '__main__':
    main()
