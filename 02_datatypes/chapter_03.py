#String - Indexing & Slicing
text = "The quick brown fox jumps over the lazy dog"

# Indexing
print(text[0])      # T
print(text[10])     # r
print(text[-1])     # g
print(text[-4])     # d

# Basic slicing [start:stop]
print(text[4:9])    # quick
print(text[10:15])  # brown
print(text[:3])     # The - by defualt begin index string is used for start
print(text[40:])    # dog - by default it pick last index of string used for last

# Slicing with step [start:stop:step]
print(text[::2])    # Teqikbonfxjmsoe h aydg
print(text[4:9:2])  # qik
print(text[::-1])   # god yzal eht revo spmuj xof nworb kciuq ehT

# Negative indices in slices
print(text[-3:])    # dog
print(text[-8:-4])  # lazy
print(text[:-35])   # The quick
print(text[::-1])   # Reverse String

#Encode & Decode
label_text = "python"
encoded = label_text.encode("utf-8")
print(f"Encoded label_text: {encoded}")
decoded = encoded.decode("utf-8")
print(f"Decoded label_text: {decoded}")