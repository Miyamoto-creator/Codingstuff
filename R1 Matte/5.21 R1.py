class equalizer():
    @staticmethod
    def f(x):
        return (3 * x) ** 2 + (-4 * x) ** 2

    @staticmethod
    def makePoly(arr):
        def fn(x):
            print("makepoly, fn: ", sum(c * x ** p for p, c in enumerate(arr)))
            return sum(c * x ** p for p, c in enumerate(arr))
        return fn

    @staticmethod
    def dx(fn, x, delta=0.001):
        return (fn(x + delta) - fn(x)) / delta

    @staticmethod
    def solver(fn, value, x=0.5, maxtries=1000, maxerr=0.00001):
        for tries in range(maxtries):
            err = fn(x) - value
            if abs(err) < maxerr:
                return x
            slope = equalizer.dx(fn, x)
            x -= err / slope
        raise ValueError('no solution found')


print(equalizer.solver(equalizer.f, 15 ** 2))  # returns (x =) 5.000000000000496

my_func = equalizer.makePoly([12, 6, 2])
print(equalizer.solver(my_func, 24))
""" def checker(nums, t=None):
     target = 225
     for i, n in nums:
         print(i, n)
         diff = target - n
         while not nums == target:
             t += 0.01
         return t"""
