
custom_encoded = ""
for current_character in custom_message:
    if current_character in custom_encodings:
        custom_encoded = custom_encoded + custom_encodings[current_character]
    else:
        custom_encoded = custom_encoded + current_character
        
print(custom_encoded)
# YOUR CODE HERE
# raise NotImplementedError()