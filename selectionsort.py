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

string = "RasimÖzhan"
dizi= []
tersdizi = []
for i in string:
    dizi.append(i)

for i in range(len(dizi)):
    a=dizi.pop()
    tersdizi.append(a)
print(tersdizi)

