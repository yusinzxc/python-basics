userFirstNum = int(input("Enter firstnumber: "))
userSecondNum = int(input("Enter lastname: "))

add = lambda x,y:x+y
minus = lambda x,y:x+y
multiply = lambda x,y:x*y
calculator = lambda x,y,op : op(x,y)
print(calculator(userFirstNum,userSecondNum,userOperator))
