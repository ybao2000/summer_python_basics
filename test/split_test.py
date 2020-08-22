# conversion between string and list

text = "   She sells  seashells   by the seashore"

# mylist = ["She", "sells", "seashells", "by", "the", "seashore"]
mylist =[]  # initialize 
word = ""   # this is the temporary working string
for c in text:
  if c != ' ':  # if not space, then concatenate the word
    word += c
  else:       # if space, that means we have put the word into the list
    if word:  # this means, we don't put empty word into the list
      mylist.append(word)
      word=""   # this is to reset the word
if word:   # this is outside the loop, also need to check if word is empty, if not, then need to append it into the list
  mylist.append(word)

print(mylist)
print()

# this is split the text into words, which are separated by white space
mylist2 = text.split()   
print(mylist2)