#Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)

#Inputs
#- Original list of strings
#- List of strings to be added
#- List of strings to be removed

#Return
#- List shall only contain unique values
#- List shall be ordered as follows
#--- Most character count to least character count
#--- In the event of a tie, reverse alphabetical

def merger(Original,Add,Delete):
	
	for element in Add:#Adding
		if element not in Original:
			Original.append(element)
	for element in Delete:#Deleting
		if element in Original:
			Original.remove(element)

	Original.sort(reverse=True) #Sorting
	return(Original)

Original=['one', 'two', 'three']
Add=['one', 'two', 'five', 'six']
Delete=['two', 'five']

Result= ['three', 'six', 'one']#Cheking

print(merger(Original,Add,Delete))
