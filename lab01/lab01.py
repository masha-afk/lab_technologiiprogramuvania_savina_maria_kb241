## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}
# already sorted list
list = [
  {"name":"Bob", "surname": "Smith", "phone":"0631234567", "group":"CB-241"},
  {"name":"Emma", "surname": "Roberts", "phone":"0631234567", "group":"CB-241"}, 
  {"name":"Jon", "surname": "Joster", "phone":"0631234567", "group":"CB-241"}, 
  {"name":"Zak", "surname": "Parker", "phone":"0631234567", "group":"CB-241"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student is " + elem["name"] + ' ' +  elem["surname"] + ",  Phone is " + elem["phone"] + ",  Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    surname = input("Please enter student surname: ")
    phone = input("Please enter student phone: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "surname": surname, "group": group, "phone": phone}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Student not found")
        return

    new_name = input("Please enter student new name: ")
    new_surname = input("Please enter student new surname: ")
    new_phone = input("Please enter student new phone: ")
    new_group = input("Please enter student new group: ")

    del list[updatePosition]
    updatedItem = {"name": new_name,"surname": new_surname, "phone": new_phone, "group": new_group}

    insertPosition = 0
    for item in list:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, updatedItem)
    print("Student data updated successfully")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

main()