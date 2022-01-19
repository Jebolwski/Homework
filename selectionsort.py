#selection sort

# dizi = [2,5,3,-32,534,2,5,43,-4]
# print(dizi)
# for i in range(len(dizi)):
#     for j in range(len(dizi)):
#         index = dizi[i]
#         if index<dizi[j]:
#             temp=dizi[i]
#             dizi[i]=dizi[j]
#             dizi[j]=temp
#         print(dizi)


# for i in range(len(dizi)):
#     for j in range(len(dizi)):
#         min=dizi[0]
#         if min>dizi[j]:
#             temp=dizi[j]
#             dizi[j]=dizi[i]
#             dizi[i]=dizi[j]
# print(dizi)

# string = "RasimÖzhan"
# dizi= []
# tersdizi = []
# for i in string:
#     dizi.append(i)

# for i in range(len(dizi)):
#     a=dizi.pop()
#     tersdizi.append(a)
# print(tersdizi)

# array = [1,2,3,4,5,6,7,8,9,10,11,12]

# for i in range(4,len(array)-1):
#     array[i]=array[i+1]
#     array[4]=24
# print(array)


# array = []

# array.append(1)
# print(array)
# array.append(2)
# print(array)
# array.append(3)
# print(array)
# array.append(4)
# print(array)
# array.append(5)
# print(array)
# array.pop()
# print(array)
# array.pop()
# print(array)
# array.pop()
# print(array)
# array.pop()
# print(array)

def faktor(b):
    if b==0 or b==1:
        return 1
    else:
        return b*faktor(b-1)
a=int(input("Kaçın faktöriyeli:"))
res=faktor(a)
print(res)



