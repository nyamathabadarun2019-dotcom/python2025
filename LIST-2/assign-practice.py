city=["hyd","ban","goa"]  #list
name=("shiva","nani", 99)  #tuple
details={"age":88,"pin":888,"add":67}  #dic
mixed_set={"shiva",23,5.9,True}   #set

"""LIST"""
# a=[city,"bpl"]#list inside list true
# print(a)
# b=[city,("sokullapalem")]#list inside tuple true
# print(b)
# c=[{"wajji":56,"s":9}]#list inside dic true
# print(c)
# d=[details,{"shiva"} ]#list inside set true
# print(type(d[0]))

"""TUPLES"""
# a=(city,["shiva"])#tuple inside list true
# print(a)
# b=(name,("shiva"))#tuple inside tuple true
# print(b)
# c=(details,{"amar":"F"})#tuple inside dict true
# print(c)
# d=(mixed_set,{"amar",24})#tuple inside set true
# print(d)

"""DICT(kEy)"""
# a={city:"shiva","[shiva]":4}#dic(key) inside list false
# print(a)
# b={name:"shiva",("shiva"):23}#dic(key) inside tuple true
# print(b)
# c={details:"nani",{"shiva":34}:"name"}#dic(key) inside dic false
# print(c)
# d={mixed_set:"nani",{"shiva"}:34}#dic(key) inside set true
# print(d)

"""DICT(value)"""
# d={"nani":{"shiva"},"shiva":{34}}  #dict(value) inside set is true
# print(d)
# a={"place":city,"nani":["shiva"]}  #dict(value) inside list is true
# print(a)
# b={"Name":name,"place":("bankok")}  #dic(value) inside tuple is true
# print(b)
# c={"college":details,"Person":{"shive":"goa"}}  #dic(value) inside set is true
# print(c)

"""SET"""
# a={city,["shiva"]}#set inside tuple is false
# print(a)
# b={name,("shiva")}#set inside tuple is true
# print(b)
# c={details,{"shiva":"nani"}}#set inside dic false
# print(c)
# d={"a",{"shiva","nani"}}
# print(d)

# citys=("san","nar")
# villages=[{"players","sandeeep"}]
# print(villages)


# letter=["a","b","c"]
# join="-".join(letter)
# print(join)

# result="-".join(["a","b","c"])
# print(result)



# food_items={"rice":500,"oil":200,"salt":100}
# gifts={"watches":500,"cups":300}
# choice=input("enter your choice")
# items=choice.split(',')
# print(items[1])



# food_items={"rice":500,"oil":200,"salt":100}
# food_items={"rice":500,"oil":200,"salt":100}


# my_list=[1,2,3,4,5]
# print(my_list[1:3])