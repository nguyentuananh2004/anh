def bai3():
    x=input("Nhap ten tap tin (nguon):")
    chuoikitu=input("Nhập vào chuỗi muốn thêm :")
    with open(x,"a") as f:
        f.write(chuoikitu)

bai3()