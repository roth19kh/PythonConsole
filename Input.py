name = input("Enter Student Name: ")
while len(name) >20:
    name = input("Please Enter Your Name again(Max_char is 20): ")
    gender = input("Enter Your gender(Male, Female): ")
while gender.lower() not in ["male", "female"]:
    if gender!="male" and gender !="female":
        gender = input("Gender in Valid Please enter again(Male, Female): ")
age=input("Enter Your Age: ")
while int(age)<17 or int(age)>45:
    age = input("Please Enter Your age again(Age Between 17 and 45): ")

print("--Student Profile--")
print("Name:" +name)
print("Gender:"+gender)
print("Age:"+str(age))