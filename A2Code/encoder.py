
encoded = ""
for c in message:
    val = ord(c)
    val = val + key
    new = chr(val)
    encoded = encoded + new 
    
    
# YOUR CODE HERE
# raise NotImplementedError()