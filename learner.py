# #string thing
# c = (input("You're name:"))
# print ("You're name:", c)

# a = "new"
# print (len(a))

# b="code"
# print (len(b))

# d =c+" "+(a+" "+b)

# print ("New code: ",d)
# print (len(d))

# print (d[4:])

# #string functions

# a = "i am a bowler"

# print (a.endswith("age"))
# print (a.capitalize())
# print (a.replace("bowler","batsman"))
# print (a.find("am"))
# print (a.count("a"))

# #loop and nested loop

# a = int (input("Enter a: "))
# b = int (input("Enter b: "))
# c = int (input("Enter c: "))

# if (a>b):
#     if(a>c):
#         print("a is greatest")
#     elif(a<c):
#         print ("c is greatest")
# elif(a<b):
#     if(b>c):
#         print("b is greatest")
#     elif(b<c):
#         print ("c is greatest")


# temperatures = [72, 85, 60, 90, 78]
# for x in temperatures :
#     if x > 80 :
#         print("Hot Day")
#     else:
#         print("Nice Day")


scores = [55, 82, 40, 95, 78]
passing_scores = []
for x in scores :
    if x >=60:
        passing_scores.append(x)
print(passing_scores)