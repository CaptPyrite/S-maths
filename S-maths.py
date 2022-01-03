def addition(number1,number2):
  x = []
  for i in range(number1):
    x.append("I")
    
  for i in range(number2):
    x.append("I")
  
  return x
  del x[:]
  
def subtraction(number1,number2):
  x = []
  
  for i in range(number1):
    x.append("I")
    
  for i in range(number2):
    del x[i]
    
  return x 
  del x[:]

def multiply(number1,number2):
  x = []
  for i in range(number2):
    for i in range(number1):
      x.append("I")
      
  return x
  del x[:]

def divide(number1,number2):
  x = []
  o = []
  for i in range(0,11):
    x.append(len(multiply(i,number2))==number1)
  try:
    o.extend("I"*int(x.index(True)))
    
    return o
    del x[:]
    del o[:]
    
  except:
    return 0
  
print(len(addition(2,2))) #2+2; O/P: 4
print(len(subtraction(6,2))) #6-2; O/P: 4
print(len(multiply(2,2))) #2*2; O/P: 4
print(len(divide(8,2))) #8/2; O/P: 4
