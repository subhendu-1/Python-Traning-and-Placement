import os
print(os.getcwd())
print (os.listdir())

data = os.listdir()

for files in data:
    print(files)


# os.mkdir('HIT')  #creat  the new file from the directory
# os.rmdir('HIT') #remove the file from the directory

# count the file data:::

f =open('text.txt')
data = f.read()
word_lst = data.split()
print(len(word_lst))