
# def get_characters(characters):
characters=input("pl enter characters number and '*','/','+','-':>>  ")
	# return characters
# characters_get=get_characters
characters_list=[]


def become_character_on_the_list( characters):
	characters_components=""
	print(characters)
	for character in characters:
		if character =="-" or character=="+" or character=="*" or character=="/" :

			characters_list.append(characters_components)
			characters_list.append(character)

			characters_components=""
		else:
			characters_components+=character

	# 
	characters_list.append(characters_components) #the last character adds the number
	return characters_list

def multiplication():
	index=characters_list.index("*")
	index_before=index-1
	index_next=index+1
	result=float(characters_list[index_before]) * float(characters_list[index_next])

	index_help=index+2
	characters_list[index_before : index_help]=[result]
	return characters_list

def division():
	index=characters_list.index("/")
	index_before=index-1
	index_next=index+1
	result=float(characters_list[index_before]) / float(characters_list[index_next])

	index_help=index+2
	characters_list[index_before : index_help]=[result]
	return characters_list

def addition():
	index=characters_list.index("+")
	index_before=index-1
	index_next=index+1
	result=float(characters_list[index_before]) + float(characters_list[index_next])

	index_help=index+2
	characters_list[index_before : index_help]=[result]
	return characters_list

def difference():
	index=characters_list.index("-")
	index_before=index-1
	index_next=index+1
	result=float(characters_list[index_before]) - float(characters_list[index_next])

	index_help=index+2
	characters_list[index_before : index_help]=[result]
	return characters_list

def mathematics():
	len_value=len(characters_list)

	for item in range(len_value):
		if "*" in characters_list:
			multiplication()

	for item_two in range(len_value):
		if "/" in characters_list:
			division()

	for item_three in range(len_value):
		if "+" in characters_list:
			addition()

	for item_four in range(len_value):
		if "-" in characters_list:
			difference()

	number=characters_list[0]

	return float(number)
		
# print(get_characters(characters))	
# print(become_character_on_the_list(get_characters()))
print(become_character_on_the_list(characters))
print(mathematics())