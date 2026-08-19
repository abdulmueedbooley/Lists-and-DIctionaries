# what is a list? 
# A list stores multiple items in specific order

#* EXAMPLE: SHOPPING LIST 
shopping_list = ['milk', 'bread', 'eggs', 'apples']
print(shopping_list) # THIS PRINTS OUT THE WHOLE LIST 
print(shopping_list[0]) # THIS PRINTS OUT THE FIRST ITEM 
print(shopping_list[1]) # THIS PRINTS OUT THE 2ND ITEM 

#* CHANGING ITEMS IN A SHOPPING LIST 
shopping_list[1] = "brown bread"
print(shopping_list)

#* ADDING ITEMS 
shopping_list.append("coffee") # Adds the item at the end of the list 
print(shopping_list) 

#* REMOVING ITEMS 
shopping_list.remove('milk')
print(shopping_list)

#* LOOP THROUGH A SHOPPING LIST 
for item in shopping_list:
    print('i need to purchase:', shopping_list)
