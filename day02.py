subjects={
    "phy" : 45,
    "chem" : 58,
    "math" : 67,
    "eng" : 68,
}
print(subjects["chem"])
subjects.pop("phy")
print(subjects)
subjects["math"]=65,
print(subjects)

print(subjects.keys())
print(subjects.values())
print(subjects.items())
