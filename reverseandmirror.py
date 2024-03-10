string_1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
string_2 = "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate"

def reverse_and_mirror(string_1, string_2): 
    
    reverse_string_1 =""
    mirrored_string = ""
    concat_string= ""
    reverse_string_2 = ""
    mirrored_string_2 = ""

    for i in range(len(string_1)-1, -1, -1):
        if "A" <= string_1[i] <= "Z":
            x = ord(string_1[i]) - ord('A') + ord('a')
        elif "a" <= string_1[i] <= "z":
            x = ord(string_1[i]) - ord('a') + ord('A')
        else: 
            x = ord(string_1[i])
        
        reverse_string_1 += chr(x)

    for i in range(len(reverse_string_1)-1, -1, -1):
        mirrored_string += reverse_string_1[i]

    for i in range(len(string_2)): 
        if "A" <= string_2[i] <= "Z":
            x = ord(string_2[i]) - ord('A') + ord('a')
        elif "a" <= string_2[i] <= "z":
            x = ord(string_2[i]) - ord('a') + ord('A')
        else: 
            x = ord(string_2[i])
        
        reverse_string_2 += chr(x)

    for i in range(len(reverse_string_2)-1, -1, -1):
        mirrored_string_2 += reverse_string_2[i]

    concat_string += mirrored_string_2 + "@@@" + reverse_string_1 + mirrored_string

    return concat_string

def main(): 
    print(reverse_and_mirror(string_1, string_2))

if __name__ == "__main__":
    main()