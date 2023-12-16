def encrypt(plaintext, key):
    ciphertext = ''
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext += plaintext[pointer]
            pointer += key
    return ciphertext
def decrypt(ciphertext, key):
    numRows = (len(ciphertext) + key - 1) // key
    numCols = key
    numShadedBoxes = (numRows * numCols) - len(ciphertext)

    plaintext = [''] * numCols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == numCols) or (col == numCols - 1 and row >= numRows - numShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

