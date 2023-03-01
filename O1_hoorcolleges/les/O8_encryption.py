import O8_matrix


def encrypt(message, encryption_matrix):
    """
      Transform the given message into a sequence of codes.
      - The message is transformed into a sequence of integer
        numbers using the Unicode representation of its characters.
      - The resulting sequence is obtained by multiplying
        the sequence of Unicodes by the given encryption matrix.
      - The length of the given message must be a multiple
        of the dimension of the encryption matrix.
    """
    pass



def decrypt(coded_sequence, decryption_matrix):

    """
      Transform the given coded sequence into a message.
      - The coded sequence is multiplied with the given
        decryption matrix (which must be the reverse of
        the matrix used at encryption time).
      - The resulting sequence of Unicodes is
        transformed into a string.
      - The length of the given coded sequence must be a multiple
        of the dimension of the decryption matrix.
    """

    pass




def encrypt_chunk(chunk,encryption_matrix):

    """
        encrypt a chunk of the sequence/message
    """

    codes = [None for k in range(len(chunk))]

    for index in range(len(codes)):

        codes[index] = ord(chunk[index])            # letters vervangen door de unicode waarde

    return O8_matrix.multiply(encryption_matrix,codes)


def decrypt_chunk(chunk,decryption_matrix):

    '''

    '''

    decoded_chunk = O8_matrix.multiply(decryption_matrix,chunk)
    print(decoded_chunk)

    message = ''

    for code in decoded_chunk:
        message = message + chr(code)

    return message


encryption_matrix = \
    [[-3, -3, -4], \
     [ 0,  1,  1], \
     [ 4,  3,  4]]

decryption_matrix = \
    [[ 1,  0,  1], \
     [ 4,  4,  3], \
     [-4, -3, -3]]

# encrypted_message = \
#     encrypt("Secret message to 1st bach engineering!", encryption_matrix)
# print("Encrypted message: ", encrypted_message)
#
# decrypted_message = decrypt(encrypted_message, decryption_matrix)
# print("Decrypted message: ", decrypted_message)


print(encrypt_chunk("abc",encryption_matrix))

coded_chunk = encrypt_chunk("abc",encryption_matrix)
print(decrypt_chunk(coded_chunk,decryption_matrix))