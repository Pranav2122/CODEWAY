p=[]
print("Enter one of the choice")
print("1.To add  the task into the todolist")
print("2.To remove  the task from the todolist")
print("3.To display the task into the todolist")
print("4.To exit from the application")
a=int(input())
while(a!=4):
    a=int(input("re enter your option: "))
    if a==1:
        b=input("Enter the task\t")
        p.append(b)
        print("The data is succesfully stored")
    elif a==2:
        c=input("Enter the task to be deleted")
        if c in p:
              p.remove(c)
              print("The task is succesfully removed")
        else:
             print("The task is not present")
    elif a==3:
         print("The items in the todolist are")
         if (len(p)>0):
             for i in range(len(p)):
                  print(p[i])
         else:
           print("They are no items in todolist")
    elif a==4:
         print("exit from the todolist")
         breakpoint
    else:
         print("Invalid option")

