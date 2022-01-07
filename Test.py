# class Fruits:
#     pass

# banana = Fruits()

# banana.color = 'yellow'
# banana.value = 30

# import pickle
# # filehandler = open(b"Fruits.obj","wb")
# # pickle.dump(banana,filehandler)
# file = open("Fruits.obj",'rb')
# object_file = pickle.load(file)
# print(object_file)

a = 12345
final = 0

while a>0:
    b = a%10
    c = a//10
    final = final*10 + b
    a = c
# print(final)


# b = []
# for i in (len(a)-1,-1,-1):
#     b.append(i)
# print(b)
x = [[2,3,5,6], [0,9,8,7]]
z = []
for i in x:
    for j in y:
        i,j = j,i
        z.append([i,j])

print(z)