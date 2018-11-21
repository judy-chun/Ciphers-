
decoded = ""
for char in encoded:
    unicode = ord(char)
    unicode = unicode - key
    newcode = chr(unicode)
    decoded = decoded + newcode
    
# YOUR CODE HERE
# raise NotImplementedError()