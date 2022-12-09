# Mở file để đọc dữ liệu
fo = open("anh", "r+")

# Đọc một chuỗi trong file
str = fo.read(20)

# In ra chuỗi được đọc
print("Chuỗi được đọc là: ", str)

# Đóng file lại
fo.close()





