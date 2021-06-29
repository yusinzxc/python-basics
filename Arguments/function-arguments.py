#ARBITRARY ARGUMENTS
def helloMe(*name):
    for i in name:
        print("Hello,",i)

helloMe("Yujin","Jiyoon","Haseul")

#KEYWORDS ARGUMENTS
def myBias(firstname,lastname):
    print("Her name is: ",firstname,lastname)

myBias(lastname="Ahn",firstname="Yujin")

#KEYWORDS ARBITRARY ARGUMENTS
def kpopMembers(*name,groupName):
    print(groupName,"Members: ")
    for i in name:
        print(groupName,":",i)
        #Loona: Heejin

kpopMembers("Heejin","Haseul",groupName="Loona")

#ARBITRARY KEYWORDS ARGUMENTS
def profileMembers(**member):
    print("Name:",member["name"],"\n","Color:",member["color"])

profileMembers(name="Jeon Heejin",color="Pink")


def addAllNum(*number):
    sum = 0
    for i in number:
        sum += i
    return sum

print(addAllNum(1,2,3,4,5,6,7,8,9,10))
