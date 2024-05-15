def cipher (n: int, s:str, k:int):

    original_alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
                    ]
    
    k = k%len(original_alph)
    
    new_alph = original_alph[k:] + original_alph[:k]
    
    cipher_s = ''



    for letters in s:
        if letters.isupper():
            cipher_s += new_alph[original_alph.index(letters.lower())].upper()
        else:
            if letters not in original_alph:
                cipher_s += letters
            else:
                cipher_s += new_alph[original_alph.index(letters)]
    print(cipher_s)
    

cipher(int(input()), input(), int(input()))