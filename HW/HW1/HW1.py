print("Welcome to PyMoney ! How much money do you have?")
global money = int(input())
print("Initial Money is", money)
global record = []
continueOrNot = input("If you want to add or take money, key Y, N to exist \n")

def initialize():
    print("Welcome to PyMoney ! How much money do you have?")
    money = int(input())
    print("Initial Money is", money)
    record = []    
    return

def delete():
    return

def view():
    print("Description          Amount\n")
    print("==================== ======\n")
    for i in record:
        print( "%s                  %d\n", i[0], i[1])
    print("==================== ======\n")
    print("%d\n",money)


def add():
    add = input("How much you add ( ex lunch 10 )\n")
    item = add.split(" ",1)[0]
    add = add.split(" ",1)[1]
    record.append((item,add))
    if(add[0] != "-"):
        # add = input("How much you add ( ex lunch 10 )\n")
        # item = add.split(" ",1)[0]
        # itemPrice = int(add.split(" ",1)[1])
        money = money + int(add[:])
    if(add[0] == "-"):
        # take = input("How much you take ( ex lunch -10 or lunch 10 )\n")
        # item = take.split(" ",1)[0]
        # take = take.split(" ",1)[1]
        money = money - int(add[1:])
        # if(take[0] == "-"):
        #     take = take.split("-",1)[1]
        #     money = money - int(take)
        # else:
        #     money = money - int(take)
        # item = take.split(" ",1)[0]
        # itemPrice = int(take.split(" ",1)[1])
def save():
    return


while (continueOrNot == "Y"):
    # initialize()
    # a = input("add or take ? key Y or N\n")
    # add = input("How much you add ( ex lunch 10 )\n")
    # item = add.split(" ",1)[0]
    # add = add.split(" ",1)[1]
    # record = []
    # record.append((item,add))
    action = input("what do you want?(initialize, add, view, delete, save)")
    if(action == "initialize"):
        initialize()
    elif(action == "add"):
        add()
    elif(action == "view"):
        view()
    elif(action == "delete"):
        delete()
    elif(action == "save"):
        save()
    # print("Current Money is", money)
    # print("Record is", record)
    continueOrNot = input("If you want to continue to add or take money, key Y\n")
