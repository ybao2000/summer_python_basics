#Given a set of words, find the shortest word. If there are mutiples, find the first one ordered by the letters.
# Test case:
#  	{'aaaa', 'bbb', 'cc', 'ca'} => 'ca'
def shortest_word(words):
# first, initalize the result (mayber with empty string)
# second, loop through the words, and 
# if result is empty, assign the result with the word
# otherwise, compare the result with the word:
#     compare with length, if word is shorter, just replace the result with word
#                          else if word is longer, do nothing
#                          else (same length), directly compare with result and word
#                                if <, then repalce,  otherwise, do nothing
# finally after the loop, the result is the answer
  result = ''
  for word in words:
    if not result:
      result = word
    else:
      if len(word) < len(result):
        result = word
      elif len(word) == len(result):
        if word < result:
          result = word
  return result

words = {'aaaa', 'bbb', 'cc', 'ca'}
print(shortest_word(words))
