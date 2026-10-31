#list which can be called array
info = ['Sharafat',90,"24 Years",58,"Hello bangla"]
print (info)

print (info[0])

info[2] = "25 Years"
print (info)

#list slicing
print (info[1:3]) #1,2 printed
print (info[:3]) #0,1,2 printed
print (info[1:]) #1,2,3,4 printed

info.append(4) #add another element at the end only
print (info)

list=[5,4,52,4,8,2,3,4]
list.sort() #sort in ascending order
print(list)

list.sort(reverse = True) #sort in descending order
print(list)

newlist = [5,4,5,8,8,1,85]

newlist.reverse()
print (newlist) #list re ghurai fele

newlist.insert(3,9) #(position/index,item) evabe diye kichu dhukano jay
print (newlist)

newlist.remove(8) #(item) remove kora jay
print (newlist)

newlist.pop(3) #(index) remove kora jay
print (newlist)