to_do_list = ["Breakfast", "Walking","Exercise"]

#1.adding task with append()
to_do_list.append("Taking rest")

#2.add task with input()
inp=input("Insert in the list: ")
to_do_list.append(inp)

#3.show number of tasks
length=len(to_do_list)
print("the number  of  tasks  in  the to-do  list is "+str(length))
print(to_do_list)

#4.remove the first task
del to_do_list[0]
print("First element of the list is deleted")
print("Now the list is: "+str(to_do_list))

#5.Remove a specific task
num_delete_task=input("Enter the serial no of task you want o remove: ")
num_delete_task=int(num_delete_task)
del to_do_list[num_delete_task]
print("Now the list is: "+str(to_do_list))

#6+7.show message if he/she has less than 4 tasks and more or equal than 6 items
length=len(to_do_list)
#print(length)
if (length<4):
    print("You have time  to  do more")
elif length>6 or length==6:
       print("You have no room  to  do more  tasks")


