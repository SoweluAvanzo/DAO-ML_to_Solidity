from snakes.nets import PetriNet, Place, Transition, Expression, Variable

print("start")

'''
.   . x .   .   .
. --------> . x < 5
(p) .   .   . [t]
. <-------- .   .
.   .x+1.   .   .
'''

n = PetriNet('First net')
n.add_place(Place('p', [0]))
n.add_transition(Transition('t', Expression('x<5')))
n.add_input('p', 't', Variable('x'))
n.add_output('p', 't', Expression('x+1'))

print("end?")
print(n)

substitutions_t_1 = n.transition('t').modes()
print(substitutions_t_1)







print("end :D")
