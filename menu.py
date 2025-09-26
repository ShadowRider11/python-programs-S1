x = 1
while(x == 1):
    print("MENU")
    print("1.find occurance of word")
    print("2.find character frequency")
    print("3.display the factors of given number")
    print("4.exit")
    a=int(input("choose one option from 1 - 4: "))
    if a==1:
        o = input("enter the text: ")
        p = o.split()
        s = set(p)
        for i in s:
            print(i, "=",p.count(i))
    elif a==2:
        o = input("enter the text: ")
        li=[]
        for i in o:
            li.append(i)
            s=set(li)
        for i in s:
            print(i,"=",o.count(i))
    elif a==3:
        o = int(input("enter a number: "))
        i = 1
        for i in range(i, o+1):
            if o % i == 0:
                print(i,"is a factor of : ",o)

    elif a == 4:
        x += 1
    else:
        print("  inavlid input ")
            
    
