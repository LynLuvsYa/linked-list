class LN:
    def __init__(self,d,p):
        self.data = d
        self.pointer = p

def initialise():
    for x in range(5):
        LL.append(LN("", x + 1))
    LL.append(LN("",-1))
def printy():
    for x in range(len(LL)):
        print(LL[x].data, "|", LL[x].pointer)
def findprev():
    for x in range(len(LL)):
        if LL[x].pointer == -1:
            return x
    return -2
def adddata(data):
    LL[startpointer].data = data
    prevpointer = findprev()
    if prevpointer != -2:
        LL[prevpointer].pointer = 
#main declarations

LL = []

    

#main prog
global startpointer
startpointer = 0
LL[startpointer].data = input("input first bit of data: ")
LL[startpointer].pointer = newspot()
data = input("input data to add: ")
adddata(data)
