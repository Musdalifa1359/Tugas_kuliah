pilihan= 0
namelist =["musdalifa","ifa"]
while pilihan <= 9:
    print("_ _ _ _ _ _ _")
    print ("1. mencetak list")
    print ("2. menambahkan nama kedalam list")
    print ("3. menghapus nama dalam list")
    print ("4. mengubah data dalam list")
    print ("5. index barabf yang ingin di tampilkan")
    print ("6. mencai barang yang ingin di cari")
    print ("9. keluar")
    menu_item = int(input("pilih menu: "))
    if menu_item == 1:
        current = 0
        if len(namelist) > 0:
            while current < len(namelist):
                print (current, ".", namelist[current])
                current = current + 1
        else:
            print("list kosong")
            
    elif menu_item == 2 :
            name = input("masukkan nama list: ")
            namelist.append(name)
            print(namelist)
            
    elif menu_item == 3 :
        del_name = input("nama yang ingin di hapus: ")
        if del_name in namelist:
            #namelist.remove(del_name) dapat di gunakan
            item_number = namelist.index(del_name)
            del namelist[item_number]
            print(namelist)

        else:
            print (del_name, "tidak di temukan")
        
    elif menu_item == 4 :
        old_name = input("nama apa yang ingin di ubah")

        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input("nama baru: ")
            namelist[item_number] = new_name
            print(namelist)
        else:
           print (old_name, "tidak di temukan")

    elif menu_item == 5 :
        print(namelist)
        nama_yang_ingin_dicari =input("masukkan nama yang ingin di cari :")
        print(nama_yang_ingin_dicari, "berada pada index", namelist.index(nama_yang_ingin_dicari))

    elif menu_item == 6 :
        nama_yang_ingin_dicari =input("masukkan nama yang ingin di cari :")
        if nama_yang_ingin_dicari in namelist:
            print("nama ini terdapat dalam namelist")
        elif nama_yang_ingin_dicari not in namelist:
            print("nama ini tidak terdapat dalam namelist")