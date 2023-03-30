with open('filename.txt', 'a+') as f:
    f.write('This is a new line.\n')
    f.seek(0)  # Move the file pointer to the beginning of the file
    content = f.read()
    print(content)