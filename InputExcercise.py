name = input("Input your name: ")
while len(name) >20 :
    name = input("Input your name: ")
gender = input("Input your gender: ")
while gender.lower() not in ["male", "female"]:
    gender = input("Input your gender again? (Male , Female): ")
age = int(input("Input your age: "))
while int(age) < 17 or int(age) > 45 :
    age = int(input("Input your age again: "))

print("--- Student information ---")
print("Name:" +name)
print("Gender:" +gender)
print("Age:" +str(age))

