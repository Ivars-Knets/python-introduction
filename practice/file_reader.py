# removes the need to add .close() at the end, that is easily forgotten
with open('data/dataToRead.txt', 'r') as file:
    file_data = file.read()
    print(file_data)