# Using the generator pattern (an iterable)
class GeneratorBase():
    '''
    @deprecated
    '''

    def __init__(self, n:int):
        self.n = n
        self.num = 0
        pass

    def __iter__(self):
        return self

    def stop_iteration(self):
        raise StopIteration()

    # Python 3 compatibility
    def __next__(self):
        return self.next()


    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        raise StopIteration()

