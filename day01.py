print("Hi my name is M.Tafseer ")
print("This is my dayone of daily uploads on github")

#Dictionaries

biodata={
    "name": "M.tafseer",
    "age" : 21,
    "Father name": "Azhar ",
    "learning" : "Coding",

}
print(biodata)
print(biodata["name"])

#dictionaries are unordered and mutable (changeable) and dont allow duplicate keys

#nested dictionaries
data= {
    "name" : "Tafseer",
    "subjects" : {
        "chem" : 54,
        "phy" : 58,
        "bio" : 59,
    }
    
    
}
print(data["subjects"]["bio"])
print(data.keys())

print(tuple(data.keys()))


new_info={"city": "karachi", "time":5,}
data.update(new_info)
print(data)


#Sets 
file={"ahmad","ali","zain","asim"}
file.add("mian")
file.add("qasim")
# print(file)
file.remove("ali")
print(file)
# file.clear()
# print(file)
print(file.pop())
