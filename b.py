class person(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname,self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

obj1 = student("Shivika ", "Agarwal", 2020)

obj1.print_name()
print(obj1.year)

    