import os
while(True) :
    print("1 to add task")
    print("2 to delete task")
    print("3 to display task")
    print("4 to end program")
    response = int(input("Enter response : "))
    match response :
        case 1 :
            date = input("Enter date : ")
            task = input("Enter task : ")
            with open("ToDo.txt", "a") as f :
                f.write(date + " ")
                f.write(task + "\n")
        
        case 2 :
            with open("ToDo.txt", "r") as f :
                f.seek(0, os.SEEK_END)
                if f.tell() == 0 :
                    print("Empty file")
                else : 
                    f.seek(0)
                    data_delete = f.readlines()
                    data_delete = [i.split() for i in data_delete]               
                    date_check = input("Enter date : ")
                    check = False
                    index = -1
                    for i in range(len(data_delete)) :
                        if data_delete[i][0] == date_check :
                            check = True
                            index = i
                    if check == True :
                        data_delete = list(data_delete)
                        data_delete.pop(index)
                    else :
                        print("No record found")
                        
                    # converting list to file string 
                    with open ("ToDo.txt", "w") as f : 
                        for i in data_delete :
                            f.write(" ".join(i) + '\n')
        
        case 3 :
            with open("ToDo.txt", "r") as f :
                f.seek(0, os.SEEK_END)
                if f.tell() == 0 :
                    print("Empty file")
                else :
                    f.seek(0)
                    data_view = f.readlines()
                    data_view = [i.split() for i in data_view]
                    print(data_view)
        
        case 4 :
            exit(0)