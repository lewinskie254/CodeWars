string = "ccccoodeffffiiighhhhhhhhhhttttttts"
string2 = []
count = 0
new_string = set()

output = ""

for i in range(len(string)- 1):
    if string[i] == string[i+1]:
        string2.append(string[i])

new_string.update(string2)
character_list = list(new_string)


for h in range(len(character_list) - 1):
    for i in range(len(character_list) - 1): 
        if "a" <= character_list[i] <= "z" or "A" <= character_list[i] <="Z":
            if character_list[i] > character_list[i+1]:
                temp = character_list[i]
                character_list[i] = character_list[i+1]
                character_list[i+1] = temp 

for i in range(len(character_list)):
    output += '"'
    output += character_list[i]
    for j in range(len(string2)):
        if string2[j] == character_list[i]:
            output += string2[j]
    output += '"'
    output += ","

for i in range(len(output)):
    pass


print("String_2_Array: ", string2)
print("Initial Character List", character_list)
print("New String: ", new_string)
print("Updated Character List", character_list)
print("Output: ", output)