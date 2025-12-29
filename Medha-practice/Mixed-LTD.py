cities =["Hyd","channi","banglor","puna","mumbai"]
names = ("shiva","amar","arun",True,98.6)
details = {
           "fruits":["apple","banana","grapes"],
           "numbers":[55,58,97,63,79]

}
##list

# a = [cities,"xyz"] # list inside list
# print(a)
# b = [cities,("abcdefgh")]#list inside tuple
# print(b)
# c = [{"pqrst":88,"abhi":98.6}]#list inside dictionary
# print(c)
# d = [cities,{"arun"}] #list inside set
# #print(d)
# print(type(d[1]))


##tuple
# a = (names,[cities])#tuple inside list
# print(a)
# b = (names,(names))#tuple inside tuple
# print(b)
# print(type(b))
# c =(names,{"age":21})  ##tuple outside and dictionary inside
# print(c)                
# print(type(c[1]))
# d = (names,{"arun"}) #tuple outside and set inside
# print(d)


##dictionary
a = {"details":details,"xyz":names}
print(a)


# numbers = [31, 55,86,79, 94,49]
# cities = ("hyd", "channi" , "banglor", "puna", "mumbai")
# payers = {
#           "names":["amar","shiva","arun"],
#           "apple":["numbers","cities","payers"]
# }
# print(payers)



