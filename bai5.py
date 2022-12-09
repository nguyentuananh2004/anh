import random as r
def bai5():
    x=r.choices(range(-1000,1001),k=1000)
    print('danh sách: ',x)
    nguon=input("Nhap ten tap tin: ")
    f=open(nguon,"w")
    a=[]
    for i in range(10):
        a.append(i)
    for i in range(100):
        for j in range(10):
            a[j]=str(x[i*10+j])
        f.write(','.join(a)+"\n")
    f.close()
    with open(nguon,"r+") as f:
        tep=f.read()
        tep=tep.replace(",", "  ")
        print(tep)
bai5()