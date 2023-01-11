# name = input("Enter the input: ")

# for i in name:
#     print(i,"*",sep=" ")
# sum = 0;
# for i in range(1,11):
#     sum = sum+i
# print(sum)




for i in range(1,51):
    if i%3==0 and i%5==0:
        print("OppoVivo")
    elif i%5==0:
        print("Vivo")
    elif i%3==0:
        print("Oppo")
    else:
        print(i)
