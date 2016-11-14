# Find 3 most common letters in a string

rick = "Gotta make you understand"
roll = """
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""

# Iterate over string
for letter in roll:
    print(letter)


count = {}
#
for letter in roll:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1


# 
from collections import Counter
print (Counter(roll).most_common(3))

