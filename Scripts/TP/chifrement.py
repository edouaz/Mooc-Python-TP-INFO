def chifrement(Words : str, offset : int) -> str:
    crypted_words = ''
    for i in Words:
        if i.isalpha():
            crypted_character = ord(i)
            crypted_character += offset
            if crypted_character > 90:
                crypted_character -= 26
            crypted_words += chr(crypted_character)
        else:
            crypted_words += i
    return crypted_words 
print(chifrement("BIEN L'BONJOUR", 7))