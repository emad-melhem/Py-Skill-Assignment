        # 1
text = "Python programming is powerful and versatile."
#       01234567          18
            
        # 2  
print(text[7:18]) # slicing from index 0 to 18 except index 18 with step =1.
""" OR
text_to_find = "programming"
index = text.find(text_to_find) # return 7
if index > -1:
    print(text[index:index + len(text_to_find)])
else:
    print("Can't find the word in text")
"""
        
split_text = text.split(" ") # split the text to list of words without space
print("-".join(split_text)) # join the list with '-'
'''or
print(text.replace(" ", "-"))
'''

        # 3
numbers = list(range(10, 101, 10)) # creat list numbers 10-100 with step 10
squares = [i ** 2 for i in numbers] # the shortcut method to creat new list with square.
""" OR
squares = []
for number in numbers:
    squares.append(number ** 2)
"""
print(squares)