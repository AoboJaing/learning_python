def counter(num):
    print('Run to the ' + str(num) + ' yield')


def f():
    print('start!')
    yield counter(1)
    yield counter(2)
    yield counter(3)
    print('Done!')