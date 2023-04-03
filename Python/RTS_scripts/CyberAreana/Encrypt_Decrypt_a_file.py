# encrypts and decrypts a file
def encrypt_file(my_file):
    file = open(my_file, 'r+')
    file_text = file.read()
    new_file_txt = ""
    for i in file_text:
        new_file_txt += chr(ord(i) + 1)
    file.seek(0)
    file.write(new_file_txt)
    file.close()
    
# decrypt_file("my_file")

def decrypt_file(my_file):
    file = open(my_file, 'r+')
    file_text = file.read()
    new_file_txt = ""
    for i in file_text:
        new_file_txt += chr(ord(i) - 1)
    file.seek(0)
    file.write(new_file_txt)
    file.close()

encrypt_file("my_file.txt")
decrypt_file("my_file.txt")
