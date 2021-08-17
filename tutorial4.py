#string slicing and string methods

str = "wELCOME to The Classes"
str_num= "4654"
str_without_space="theclasses"
print(str)
print(len(str))

print(str[0:7])
print(str[:])
print(str[0:len(str)])
print(str[8:10])
print(str[0:10:2])
print(str[::])
# print(str[0:len(str):1])-> default value
print(str[::-2])

print(str.capitalize())
print(str.count('s'))
print(str.endswith("Classes"))
print(str.find("to"))
print(str_num.isalnum())
print(str_without_space.isalpha())
print(str.lower())
print(str.replace('s','S')) #all the character willl be replaced

