import time

from remove_forged import is_forged

if __name__ == '__main__':
    num_tests = 1000000
    start = time.time()
    for _ in range(num_tests):
        ret = is_forged('482CA04A7D89')
    elapsed = time.time() - start
    print('total time: {} sec'.format(elapsed))
    print('avg time: {} sec'.format(elapsed / num_tests))
