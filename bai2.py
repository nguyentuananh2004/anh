def bai2():
    x=input("Nhap ten tap tin(nguồn):")
    with open(x,"r") as f:
        doc=f.read()
        print(doc)
bai2()