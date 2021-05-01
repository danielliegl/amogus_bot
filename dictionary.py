from PyDictionary import PyDictionary
dictionary=PyDictionary()

# improve_wordlist(word_list):
# takes a list of words and adds all synonyms that it can find using the
# PyDictionary package and creates a list with the old words and
# new synonyms
def improve_wordlist(word_list):
  new_list = []
  for word in word_list:
    new_list.append(word)
    if dictionary.synonym(word) is not None:
      for synonym in dictionary.synonym(word):
        new_list.append(synonym.lower())
  return list(dict.fromkeys(new_list))