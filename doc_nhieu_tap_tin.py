from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc: str, ten_taptin: str, objs: list[SinhVien]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print(e)
        print('Xay ra loi trong qua trinh ghi file')

def doc_sinhvien(thumuc: str, ten_taptin: str) -> list[SinhVien]:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def in_list_sinhvien(content: list[SinhVien]):
    for item in content:
        print(item)

def main():
    path = 'C:\\Anh'
    filename = 'sinhvien4.dat'
    sv1 = [SinhVien('Van Nhi', 2005, 10.0),
           SinhVien('Tuan Anh',2004, 11.0),
           SinhVien('Tuan Dat',2004, 12.0)]
    ghi_sinhvien(path, filename, sv1)
    in_list_sinhvien(noidung)
    noidung = doc_sinhvien(path, filename)
    print(noidung)
    print('ket thuc chuong trinh')


if __name__ == '__main__':
    main()