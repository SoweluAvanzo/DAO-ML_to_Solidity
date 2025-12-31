
import src.utilities.comparisons as comp


class A:
    def __init__(self, a="a"):
        self.a = a


class A_same:
    def __init__(self, a="a"):
        self.a = a


class B:
    def __init__(self, b="b"):
        self.b = b


class CD:
    def __init__(self, c="c", d=7):
        self.c = c
        self.d = d


class DE:
    def __init__(self, d=7, e=False):
        self.d = d
        self.e = e


class T:
    def __init__(self, value1, value2, should_pass=True):
        self.value1 = value1
        self.value2 = value2
        self.should_pass = should_pass


# TODO, fare liste, sotto-liste, oggetti, oggetti con sotto-oggetti e liste e sottoliste
ints1 = [1, 2, 3]
ints2 = [4, 5, 6]
mixin_vals = [None, 666, True, 5.5, "ciao"]
object1 = {"o": 0}
object2 = {"p": 0}
tests: list[T] = [
    *[
        T(v1, v2, v1 == v2)
        for v1 in mixin_vals
        for v2 in mixin_vals
    ],  # 0-24
    T(6, 7, False),  # 25
    T(3.14159265, 2.718281828, False),
    T("hello", "mom", False),
    T(True, False, False),
    T(ints1, ints1, True),
    T(ints1, ints2, False),  # 30
    T(ints2, ints1, False),
    T([9, ints1, 0], [9, ints1, 0], True),
    T([9, ints1, 0], [9, ints2, 0], False),
    T([9, ints1, 0], [9, ints1, 3], False),
    # 35
    # TODO
]


def join_errors(errors):
    return f"\n\t - {'\n\t - '.join(errors)}"


debug = True
print("START")
index = 0
for t in tests:
    errors = comp.check_differences(t.value1, t.value2)
    if t.should_pass:
        if (errors is not None) and (len(errors) > 0):
            print(
                f"\nUnexpected {len(errors)} errors at test {index}: {join_errors(errors)}")
    elif (errors is None) or (len(errors) <= 0):
        print(f"\n test {index} shoud had errors but have none of them")
    elif debug:
        print(
            f"\nDEBUG # {index} ... just print errors: {join_errors(errors)}")
    index += 1

print("\n end")

# python -m src.tests.pipeline.manual.t_check_differences > t_check_differences_OUT.txt
