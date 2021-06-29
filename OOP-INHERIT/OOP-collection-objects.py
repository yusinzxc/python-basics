class MyBias:
    def __init__(self,name,colors):
        self.name = name
        self.colors = colors
    def introduce(self):
        print("Hi i'm " + self.name)


members = ["Heejin","Hyunjin","Haseul","Yeojin","Vivi","Kim Lip","Jinsoul","Choerry","Yves","Chuu","Go Won","Olivia Hye"]
colors = ["Pink","Yellow","Green","Orange","Pastel Rose","Red","Blue","Purple","Burgundy","Peach","Eden Green","Silver"]
listofMembers = [] #m
listofColors = [] # m

for i in range(12):
    # m = MyBias("Heejin","Pink")
    m = MyBias(members[i],colors[i])

    # append to listofMembers
    listofMembers.append(m)

for i in listofMembers:
    #listofMembers[0].introduce()
    i.introduce()

    print("Color \n","-",i.colors,"\n")
