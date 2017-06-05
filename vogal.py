letra = input('Digite uma letra: ')

def vogal(l):
    if l == 'a' or l == 'A':
        return True
    elif l == 'e' or l == 'E':
        return True
    elif l == 'i' or l == 'I':
        return True
    elif l == 'o' or l == 'O':
        return True
    elif l == 'u' or l == 'U':
        return True
    else:
        return False

print(vogal(letra))        