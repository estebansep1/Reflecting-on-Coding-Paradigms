class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = 'repaired'

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other):
        other.condition = 'trashed'




pod = Podracer(max_speed=3, condition="perfect", price=1000)
pod.repair()
print(pod.condition)

new_pod = AnakinsPod(max_speed=2, condition="trashed", price=800)
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod(max_speed=5, condition="perfect", price=1200)
third_pod.flame_jet(new_pod)
print(new_pod.condition)



# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
"""
Definitely some inhertience since anakin and sebula's pod all inherit from Podracer. 
Also Enscapulation as attributes and methods within each class hide internal details.
"""

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
"""
With OOP and this solution I think this was the correct way to do it because any other way probably would have been to repetitive

"""
# How in particular did Object Oriented Programming assist in the solving of this problem?
"""
It helped me organize and reuse bits of the code
"""