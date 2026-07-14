# take input of data of students (name sapid cource) from user
# store data in a file
# update cource of student 
# reflect the update in file

with open("filename.txt", "w+") as f :
    name = input("Enter name of student : ")
    f.write(name + " ")
    sap_id = input("Enter sap id of student : ")
    f.write(sap_id + " ")
    cource = input("Enter cource of student : ")
    f.write(cource + "\n") 
    
    f.seek(0)
    data = f.readlines()
    data = [i.split() for i in data]
    
    # updating
    new_cource = input("Enter new cource : ")
    data[0][2] = new_cource  # currently update is reflected only in list, not in file
    
    # making the update to reflect in file also
    # -> we can't directly do f.write(data), as data is a list and file only accepts string
    # -> for this first we have to convert new_cource(list) to file string, so that we can write it in file again
    
    with open("filename.txt", "w") as f :   # we are opening file again in write mode to truncate previous record and write it with new record
        for i in data :
            lines = " ".join(i)  # this line will convert the updated list to file string again
            f.write(lines)       # it will convert each element of list to string seperated by spaces between them
        
    # here, we are not updating just cource from data
    # we are fully truncating previous data or whole file, and filling file with new, updated data
    print(data)
    