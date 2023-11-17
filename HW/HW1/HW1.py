import os

global money 
global record 

money = 0
record = []

def initialize():
    global money 
    global record 
    print("Welcome to PyMoney ! How much money do you have?")
    try:
        money = int(input())
    except ValueError:
        print("Only integer is valid in initialization\n")
        initialize()
    record.clear()
    print("Description          Amount\n")
    print("==================== ======\n")
    record.append(("Initail Money", money))
    print("Initail Money        %d\n" %money)

def view():
    global money 
    global record 
    print("Description          Amount\n")
    print("==================== ======\n")
    for item in record:
        print( "%15s%12s\n" %(item[0], item[1]))
    print("==================== ======\n")
    localMoney = 0
    for item in record:
        localMoney = localMoney + int(item[1])
    money = localMoney
    print("tot:%d\n" %money)


def Add():
    global money 
    global record 
    while True:
        add = input("How much you add ( ex lunch 10, exit to end )\n")
        add = add.split(" ")
        # print("add:",add)
        if len(add)==1:
            if(add[0] == "exit"):
                break
            continue
        elif len(add)==2:
            item = add[0]
            moneyAdd = add[1]
            try:
                int(moneyAdd[:])
            except ValueError:
                print("2nd Input should be integer")
                Add()
                
            # try:
            #     int(item[:])
            # except ValueError:
            #     print("1st Input should be integer")
            #     Add()
            # try:
            #     moneyAdd = add.split(" ",1)[1]
            #     try:
            #         int(moneyAdd[:])
            #     except ValueError:
            #         print("2nd Input should be integer")
            #         Add()
            # except IndexError:
            #     print("Input should like ex apple 100")
            #     Add()
            record.append((item,moneyAdd))
            if(moneyAdd[0] != "-"):
                money = money + int(moneyAdd[:])
            if(moneyAdd[0] == "-"):
                money = money - int(moneyAdd[1:])
        else:
            continue
        # item = add.split(" ",1)[0]
        # if(add=="exit"):
        #     break
        # else:
        #     item = add.split(" ",1)[0]
        #     try:
        #         moneyAdd = add.split(" ",1)[1]
        #         try:
        #             int(moneyAdd[:])
        #         except ValueError:
        #             print("2nd Input should be integer")
        #             Add()
        #     except IndexError:
        #         print("Input should like ex apple 100")
        #         Add()
        #     record.append((item,moneyAdd))
        #     if(moneyAdd[0] != "-"):
        #         money = money + int(moneyAdd[:])
        #     if(moneyAdd[0] == "-"):
        #         money = money - int(moneyAdd[1:])
# def delete(record):

            # add = add.split(" ",1)[1]

            # if(type(add.split(" ",1)[0]) != str):
            #     print("1st input should be string")
            #     Add()
            # if(type(int(add.split(" ",1)[1])) != int):
            #     print("2st input should be integer")
            #     Add()
            # try:
            # try:
            #     "a" + int(add.split(" ",1)[0])
            #     item = add.split(" ",1)[0]
            # except TypeError:
            #     print("1st Input should be string")
            #     Add()
            # item = add.split(" ",1)[0]
def delete():
    global record 
    print("choose the number you want to delete, ex 1,2,3")
    idx = int(input())
    del record[idx]
    return        
# def save(money,record):


def save(name):
    global money 
    global record 
    file = open("./" + name + ".txt","w")
    for item in record:
        file.writelines("%s            %s\n" %(item[0], item[1]))
    file.writelines("Tot:%s\n" %(money))
    file.close()
    return

def read(name):
    global money 
    global record 
    record.clear()
    file = open("./" + name + ".txt","r")
    fileList = []
    fileList = file.readlines()
    print(fileList)
    print("\n")
    for i in range(len(fileList)-1):
        if(i == 0):
            a = fileList[i].split()[0]
            b = fileList[i].split()[1]
            c = fileList[i].split()[2]
            record.append((a + " " + b,c))
        else:
            a = fileList[i].split()[0]
            b = fileList[i].split()[1]
            record.append((a,b))
    # file.write("Tot:%s\n" %(money))
    file.close()
    return


while True:
    action = input("what do you want?( (a) initialize, (b) add, (c) view, (d) delete, (e) save, (f) read (g) exit, ex:a,b...)")
    print("action:",action)
    if(action == "a"):
        initialize()
        # initialize(money, record)
    elif(action == "b"):
        Add()
        # add(money, record)
    elif(action == "c"):
        view()
        # view(money,record)
    elif(action == "d"):
        delete()
        # delete(record)
    elif(action == "e"):
        name = input("Enter fileName : ")
        save(name)
        # save(money,record)
    elif(action == "f"):
        name = input("Enter fileName : ")
        read(name)
    elif(action == "g"):
        break
view()