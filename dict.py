
#? WHAT IS A DICTIONARY 
# a dictionary stores pairs of information, a key and value 
# Think of it as a real dictionary, you look up a word (the key) and find its definition (the value)

#* EXAMPLE: CONTACT LIST
phone_book = {"mom" : "082 123 4567", 
              "Dad" : "082 765 4321", "Best Friend" : "083 555 1122"} 
print(phone_book) # PRINTS OUT THE ENTIRE PHONE BOOK 
print(phone_book["mom"]) # PRINTS OUT MOMS PHONE NUMBER

#* ADDING A NEW ENTRY 
phone_book["sister"] = "082 779 3542"
print(phone_book)

#* CHANGING A NEW ENTRY 
phone_book['dad'] = '082 124 1365'

#* REMOVING AN ENTRY 
del phone_book["Best Friend"]
print(phone_book)

#* LOOPING THROUGH A DICTIONARY 
for name, number in phone_book.items():
    print(name, ":", number)
