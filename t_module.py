import json

from model.c2 import C2
from model.permission import Permission
from model.dao import DAO

t = "ciao a te"
n = 3
print("START")
c2 = C2(t, n)
c2.printText()

p = Permission("ID_7", None, "ALL", "Management", True, False)
print(p)
print(json.dumps(p.toJSON()))

print("\n\n now create a DAO\n")

d = DAO("ID_1", "DAOTest", "to test", "hierarchicalBOH")
d.add_permission(p)
print(d)
print("..... now, the JSON")
print(json.dumps(d.toJSON()))

d = {"x": 7, "y": "ciao0"}
print(d)

for x in d:
    print(x)
print("...and ...")
for x in d.values():
    print(x)
print("END")