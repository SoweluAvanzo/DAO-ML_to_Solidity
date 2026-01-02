
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


class K:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


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
o_2f_1 = {"a": 7, "b": False}
o_2f_2 = {"c": "ciao", "b": True}
o_l_1 = {"id": "Point1", "coord": [0, 2, 3]}
o_l_2 = {"id": "Point1", "coord": [8, 2, -3]}
onl1 = {"loc": ["Via", "Sostegno", [65, "bis"]]}  # Object Nested list
onl2 = {"loc": ["Via", "Sostegno", ["65", "bis"]]}  # Object Nested list
onl3 = {"loc": ["Via", "Sostegno", ["65", {}]]}  # Object Nested list
ono1 = {"name": "lonevetad", "stats": {  # Object Nested Object
    "int": 8, "des": 5, "for": 7, "cos": 2}, "liv": 30}
ono2 = {"name": "lonevetad", "stats": {
    "int": 9, "des": 4, "for": 8, "cos": 2}, "liv": 31}
#
a = A()
a2 = A_same()
oa = {"ob": a}
oa2 = {"ob": a2}
a1 = A("altra a")

k1 = K(a="ciao", b="mamma", c=7)
k2 = K(a="ciao", b="mondo", c=8)
k3 = K(a="ciao", b=9, d=True)

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
    T(ints2, [-3, 4, 5, 6, 8], False),  # 35
    T(o_2f_1, {**o_2f_1}, True),
    T(o_2f_1, o_2f_2, False),
    T(o_2f_1, {**o_2f_2, "b": [98]}, False),
    T(o_l_1, {**o_l_1}, True),
    T(o_l_1, o_l_2, False),  # 40
    T(onl1, onl2, False),
    T(onl3, onl2, False),
    T(ono1, comp.deep_copy(ono1), True),
    T(ono1, ono2, False),
    T(a, a, True),  # 45
    T(a, a2, False),
    T(a2, a, False),
    T(a2, a2, True),
    T(oa, {"ob": a}, True),
    T(oa, oa2, False),  # 50
    T(a, a1, False),
    T(a1, a, False),
    T(a, B(), False),
    T(a, B(b="a"), False),
    T(B(), B(), True),  # 55

    # in the end
    T(k1, k1, True),
    T(k1, K(a="ciao", b="mamma", c=7), True),
    T(k1, k2, False),
    T(k1, k3, False),
    T(k3, k2, False),

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
