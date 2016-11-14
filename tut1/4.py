# Reverse all words in a sentence + make first letter a capital letter
sentence = "This is pretty cool sentence"

splitted = sentence.lower().split()
splitted = [word[::-1] for word in splitted]
out = " ".join(splitted).capitalize()
print(out)


out = " ".join([word[::-1] for word in sentence.lower().split()]).capitalize()

print (out)
