string = "gztxxxxxggggggggggggsssssssbbbbbeeeeeeehhhmmmmmmmitttttttlllllhkppppp"
changed_status = False 
array_of_changes = []
count = 0
array_of_big_groups = []
final_count = 0

#create an index list of all characters where a change is happening 
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        array_of_changes.append(i)

print(array_of_changes)
print(string.index('i'))

#establish which two adjacent indexes have a difference of less than 2 (meaning that there are less than 2 adjacent characters occurring subsequently)
for i in range(len(array_of_changes)-1):
    if array_of_changes[i+1] - array_of_changes[i] < 2:
        #slice the string up to the index where the change happens
        x = string.index(string[array_of_changes[i+1]])
        #add the sliced string into a new list: array_of_big_groups 
        array_of_big_groups.append(string[count: x])
        #record the previous index where the slice was made for the next slice
        count = x

print(array_of_big_groups)
#add the last part of the string which might not be included in the previous array 
final_item = 1 + array_of_changes[len(array_of_changes)-1]
array_of_big_groups.append(string[count: final_item])

print(array_of_big_groups)
#Clean Up Collection 
#establish if all the items in the big group have more than 2 adjacent characters and eliminate those that are not
for i in range(len(array_of_big_groups)):
    tracker_score = 0
    if len(array_of_big_groups[i]) < 2:
        pass
    else: 
        #create a unique set of all the characters in each item at each index 
        x = set()
        #check if all the items left have a recurrence of two or more adjacent characters 
        for j in range(len(array_of_big_groups[i])):
            for char in array_of_big_groups[i]:
                x.add(char)
        
        #Create a list of the set items so that we can iterate through it to do further checks 
        y = list(x)

        #create an array with a count for the occurrence of each set character in the array_of_big_groups item at index[i]
       
        array_of_set_character_scores = []
       
        for a in range(len(y)):
            character_count_1 = 0
            for j in range(len(array_of_big_groups[i])):
                if array_of_big_groups[i][j] == y[a]:
                    character_count_1 += 1
                
            array_of_set_character_scores.append(character_count_1)
            character_count_1 = 0 

        #this will help us keep score of the number of times that each unique character occurs in each substring created 
        

        #Qualifying statements: If the length of the array_of_set_character_scores > 2: then at least 2 items in the list must have a value greater than 2
        #Qualifying Statements: if the length of the array_of_set_character_scores =< 2: then both items must have a value greater than 2 
        #Keeping score of the newly added scores might help 
        array_length = len(array_of_set_character_scores)

        #if the tracker score is higher than 1, then all qualifying statements are true 
        if array_length > 2:
            #keep score of the number of times that an array list has a value of more than 1 add 1, and subtract 1 when the item is less than 1 in value
            tracker_counter = 0
            for c in range(array_length):
                if array_of_set_character_scores[c] <= 1:
                    tracker_counter -= 1
                else: 
                    tracker_counter += 1
                tracker_score = tracker_counter
        else: 
            for c in range(array_length):
                if y[c] == 1:
                    tracker_score = 0
        
        if tracker_score == 0: 
            final_count = 0
    #if the tracker score does not exist, then there is no recurrence of the character in the item, thereby the score will be zero, otherwise, the final score will be factored in. 








        
        

    
