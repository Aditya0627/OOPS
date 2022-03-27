class Team:
    promotion = 'A' #class variable
    demograde = 'B'
    def __init__(self, name, age, tno,gd): #it is a contructor
        self.name = name
        self.age = age
        self.tno = tno
        self.gd = gd
    def promote(self):
        self.gd = Team.promotion #class variable calling
    def demote(self):
        self.gd = Team.demograde
    @classmethod
    def change_grade(cls,grd):   #class method is a way to change the value of the class variable!
        Team.promotion = grd
    @classmethod
    def details(cls,d_str):     #using class method as an alternative constructor
        name,age,tno,gd = d_str.split('-')
        return cls(name,age,tno,gd)

cpt = Team("Virat", 33, 18,'A')
wk = Team("Rishabh",25, 17,'B')

#using classmethod
print(cpt.gd)
Team.change_grade('Z')  #this will change the value of class variable
cpt.promote()
print(cpt.gd)


#using class method as alternative constructor
print(cpt.name)
vcpt = Team.details('Rohit-35-45-A')
print(vcpt.name)
print(wk.name)