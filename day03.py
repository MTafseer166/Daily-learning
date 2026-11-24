python_students = {
"Ali","Ahmad","Sara","Hina"
}
java_students = {"Sara","Hina","Bilal","Zain"}

print(python_students.intersection(java_students))

print(python_students.union(java_students))

print(python_students.difference(java_students))

print(python_students.symmetric_difference(java_students))

word = "programming"
count = {}
for letter in word:
    count[letter]=count.get(letter,0)+1
    print(count)