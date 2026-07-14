to_do = {}
while (True) : 
    print("===================================================")
    print("Enter '1' to add days and tasks in todo list")
    print("Enter '2' to delete days and tasks in todo list")
    print("Enter '3' to view days and tasks in todo list")
    print("Enter '4' to end program")
    print("===================================================")
    n = int(input("Enter your choice : "))
    match(n) : 
        case 1 : 
                day_num = int(input("Enter day number : "))
                to_do[day_num] = []
                while(True) :
                    task_input = input("Enter task for day : ")
                    print("Enter 1 to exit day planner")
                    if task_input == "1" :
                        break
                    else :
                        to_do[day_num].append(task_input)         

        case 2 : 
            if len(list(to_do.keys())) == 0 :
                print("List is already empty")
                break
            delete_choice = input("Enter 'a' to delete whole day and 'b' to delete task for particular day : ")
            if delete_choice == "a" :
                day_delete = int(input("Enter the day which you want to remove : "))
                flag = False
                for i in to_do :
                    if i == day_delete : 
                        flag = True
                        break
                if flag == True :
                    del to_do[day_delete]
                else :
                    print("Item not found in list")
            elif delete_choice == "b" :
                day_delete = int(input("Enter day from which you want to remove task : "))
                day_task = input("Enter task which you want to delete : ")
                flag = False
                for i in to_do :
                    if i == day_delete :
                        flag = True
                        break
                if flag == True :
                    to_do[day_delete].remove(day_task)
        case 3 :
            print(to_do)
            
        case 4 : break