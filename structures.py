# JEROME C. REYES BSCpE

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z',
            'j', 'e', 'r', 'o', 'm', 'e', 'c', 'r', 'i', 's', 't', 'o', 'b', 'a', 'l', 'r', 'e', 'y', 'e', 's']


from collections import Counter
Alphabet_counts = Counter(Alphabet)
repeat = Alphabet_counts.most_common(5)
print ("Alphabet duplicated")
print(repeat)