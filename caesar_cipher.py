def caesarCipher(s, k):
    '''
    ASCII values for lowercase characters range from ord('a') to ord('z')
    ASCII values for lowercase characters range from ord('A') to ord('Z') 
    '''

    encrypted_s = ""
    k = k if k < 26 else k % 26
    for letter in s:
        if (ord(letter) >= ord('a') and ord(letter) <= ord('z')):
            encrypted_s += chr(ord(letter) + k) if ord(letter) + k <= ord('z') else chr(ord('a') + ord(letter) + k - ord('z') - 1)
        elif (ord(letter) >= ord('A') and ord(letter) <= ord('Z')):
            encrypted_s += chr(ord(letter) + k) if ord(letter) + k <= ord('Z') else chr(ord('A') + ord(letter) + k - ord('Z') - 1)
        else:
            encrypted_s += letter

    return encrypted_s
    
print(caesarCipher("www.abc.xy",87))