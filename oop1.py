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

cpt = Team("Virat", 33, 18,'A')
wk = Team("Rishabh",25, 17,'B')

print('',cpt.age,cpt.name,cpt.tno,cpt.gd,'\n',wk.age,wk.name,wk.tno,wk.gd)
print("Grade of Risabh Pant is upgraded")
wk.promote()
print("Grade of Virat Kohli is degraded")
cpt.demote()
print('',cpt.age,cpt.name,cpt.tno,cpt.gd,'\n',wk.age,wk.name,wk.tno,wk.gd)

