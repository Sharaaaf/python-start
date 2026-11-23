# n = int(input("Give me input: "))

# n =1
# while n<=10:
#     print(n*n)
#     n += 1
#     x = [n]

# print(x)

# for el in range(101):
#     print(el)

# for el in range(100,0,-1):
#     print(el)

# n = int(input("Give: "))
# for val in range (1,11):
#     print(n*val)

# n = int(input("Enter: "))
# i = 1
# sum = 0
# while i <= n:
#     sum +=i
#     i+=1 
    
# print (sum)

# n = int (input("Give me : "))
# i = 1
# Result = 1
# for val in range (n):
#     Result *= i
#     i+=1
# print(Result)     

employees = {
    (101,"Alice",50000),
    (102,"Bob",65000),
    (103,"Charlie",45000)
}

a = int(input("Provide Employee Id : "))
found = False

for employee in employees :
    employee_id = employee[0]

    if employee_id == a :
        print("FOUND!!")
        print("Name is ",employee[1])
        print("ID is ",employee[0])
        print("Salary is ",employee[2])

        found = True
        break

if found == False:
    print("NOT FOUND")