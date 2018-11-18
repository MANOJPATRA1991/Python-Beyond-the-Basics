def count_words(doc):
  normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
  frequencies = {}
  for word in normalised_doc.split():
    frequencies[word] = frequencies.get(word, 0) + 1
  return frequencies

def combine_counts(d1, d2):
  d = d1.copy()
  for word, count in d2.items():
    d[word] = d.get(word, 0) + count
  return d
