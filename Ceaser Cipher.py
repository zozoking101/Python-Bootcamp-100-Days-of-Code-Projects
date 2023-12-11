
logo = """                                          

    '''`M                                          
dM'       ` ,6"Yb.  .gP"Ya  ,pP"Ybd  .gP"Ya `7Mb,od8 
MM         8)   MM ,M'   Yb 8I   `" ,M'   Yb  MM' "' 
MM.         ,pm9MM 8M"""""" `YMMMa. 8M""""""  MM     
`Mb.     ,'8M   MM YM.    , L.   I8 YM.    ,  MM     
  `"bmmmd' `Moo9^Yo.`Mbmmd' M9mmmP'  `Mbmmd'.JMML.   
                                                                                                                            
             ,,            ,,                        
  .g8"'"bgd  db          `7MM                        
.dP'     `M                MM                        
dM'       ``7MM `7MMpdMAo. MMpMMMb.  .gP"Ya `7Mb,od8 
MM           MM   MM   `Wb MM    MM ,M'   Yb  MM' "' 
MM.          MM   MM    M8 MM    MM 8M""""""  MM     
`Mb.     ,'  MM   MM   ,AP MM    MM YM.    ,  MM     
  `"bmmmd' .JMML. MMbmmd'.JMML  JMML.`Mbmmd'.JMML.   
                  MM                                 
                .JMML.                               
"""

AppRunning = True
alphabets = 'abcdefghijklmnopqrstuvwxyz'

def is_alphabet(char):
    return char.isalpha()

def encrypt(string, shift_number):
    if shift_number > 25:
        shift_number %= 26

    encrypted = []
    for char in string:
        if is_alphabet(char):
            is_upper = char.isupper()
            char = char.lower()
            index = (alphabets.index(char) + shift_number) % 26
            encrypted_char = alphabets[index]
            encrypted.append(encrypted_char.upper() if is_upper else encrypted_char)
        else:
            encrypted.append(char)

    encrypted_text = ''.join(encrypted)
    print(f'The encoded text is {encrypted_text}')

def decrypt(string, shift_number):
    if shift_number > 25:
        shift_number %= 26

    decrypted = []
    for char in string:
        if is_alphabet(char):
            is_upper = char.isupper()
            char = char.lower()
            index = (alphabets.index(char) - shift_number) % 26
            decrypted_char = alphabets[index]
            decrypted.append(decrypted_char.upper() if is_upper else decrypted_char)
        else:
            decrypted.append(char)

    decrypted_text = ''.join(decrypted)
    print(f'The decoded text is {decrypted_text}')

print(logo)

while AppRunning:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction in ['encode', 'encrypt']:
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        encrypt(string=text, shift_number=shift)
        again = input("Do you want to continue: ").lower()
        if again in ['no', 'q']:
            AppRunning = False

    elif direction in ['decrypt', 'decode']:
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        decrypt(string=text, shift_number=shift)
        again = input("Do you want to continue: ").lower()
        if again in ['no', 'q']:
            AppRunning = False
    else:
        print("Enter a valid direction")
