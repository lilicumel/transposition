from flask import Flask, render_template, request
from transposition_cipher import encrypt, decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    plaintext = request.form['plaintext']
    key = int(request.form['key'])
    encrypted_text = encrypt(plaintext, key)
    return render_template('index.html', plaintext=plaintext, key=key, result=encrypted_text, action='Encryption')

@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    ciphertext = request.form['ciphertext']
    key = int(request.form['key'])
    decrypted_text = decrypt(ciphertext, key)
    return render_template('index.html', ciphertext=ciphertext, key=key, result=decrypted_text, action='Decryption')

if __name__ == '__main__':
    app.run(debug=True)
