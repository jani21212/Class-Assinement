class student:
    def developer(self):
        print('IS a programmer')
class ali(student):
    def developer(self):
        print('is a python developer')
class ahmad(student):
    def developer(self):
        print('is a java developer')
def dev(student):
    dev(ali())
    dev(ahmad())

class ali:
    def developer(self):
        print('ali is a deveoper')

class ahmad:
    def developer(self):
        print('ahmad is a developer')

class qadeer:
    def developer(self):
        print('qadeer is a developer')

a = ali()
b = ahmad()
c = qadeer()

print(a.developer(), b.developer() ,c.developer())