import re

def LongestWord(sen):
  words = (re.sub(r"[^a-z A-Z0-9_]+", '', sen)).split(' ')

  longest =""

  for word in words:
    if len(word) > len(longest):
      longest = word

  return longest


print(LongestWord(input()))
