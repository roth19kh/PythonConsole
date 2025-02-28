myList = ["Kon Khmer" ,"Kon Khmer" , "Min del Klach" , "Ey tang os"]

myList.insert(1, "HEHEHEHeE")
myList.append("-;")
myList.pop(0)
myList.remove("Ey tang os")
for display in myList:
    print(display)

newList = myList.copy()
newList.append(":-")
for displayNew in newList:
    print(displayNew)

newOneList = myList + newList
for displayNew in newOneList:
    print(displayNew)

count = myList.count("Kon Khmer")
print(count)

index = myList.index("Kon Khmer")
print(index)
myList.reverse()
print(myList)

myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)