#tipe data list
data_list =[10,11,12,13,1.4,"ifa",False]
i=0
while i <5:
    print(data_list[i]) #perulangan
    i+=1
data_list[3]="kayla" #update
print(data_list)
data_list.remove(11) #menghapus
print(data_list)
data_list.insert(3,20) #menambahkan
print(data_list)

#tipe data tuple
data_tuple =(100,200,300,400,500)
print(data_tuple, type(data_tuple))
for i in data_tuple:
    print(i)

#tipe data set
data_set ={"ifa","dini","naya",1,2,3}
i=0
while i<2:
    print(data_set)#perulangan
    i+=1
data_set.discard(2)
print(data_set) #menghapus
data_set.add(50) #menambahkan
print(data_set)

#tipe data dictionary
data_dictionary ={
"nama":"ifa",
"sekolah":"smk",
"univ":"unsulbar"}
i=0
while i<2:
    print(data_dictionary) #perulangan
    i+=2
data_dictionary["nama"]="dini" #update
print(data_dictionary)
data_dictionary["alamat"]="sekolah"
print(data_dictionary)
del data_dictionary["univ"] #menghapus
print(data_dictionary)