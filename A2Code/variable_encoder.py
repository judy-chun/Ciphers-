
encoded = ""
key = start_key
for c in message:
    val = ord(c)
    val = val + key
    new = chr(val)
    encoded = encoded + new 
    key = key + key_increment 
    
# YOUR CODE HERE
# raise NotImplementedError()