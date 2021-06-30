import time
class Bias:
  def __init__(self,names,reps,colors):
    self.names = names
    self.reps = reps
    self.colors = colors
  
  def introduce(self):
    print("",self.names)
    print("",self.reps)
    print("",self.colors)

listOfMembers = []

while True:
  print()
  name =  input("Name          : ")
  rep =   input("Representative: ")
  color = input("Color         : ")
  bias = Bias(name,rep,color)
  listOfMembers.append(bias)
  
  addMembers = input("you want to add more members? [Y/Any Char] >>> ")
  
  print()
  if addMembers == "Y" or addMembers == "y":pass
  else:break
  
count = 1
for i in listOfMembers:
  print("Member #"+ str(count))
  i.introduce()
  count += 1
  print()