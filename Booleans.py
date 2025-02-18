a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


'''One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class 
with a __len__ function that returns 0 or False:'''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))