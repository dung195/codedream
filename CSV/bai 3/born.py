import csv
import random

# Danh sách mẫu cho họ tên
ho = ['Nguyen', 'Tran', 'Le', 'Pham', 'Hoang', 'Do', 'Bui']
ten_dem = ['Van', 'Thi', 'Minh', 'Thu', 'Quang', 'Hong', 'Huu']
ten = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Hàm tạo tên sinh viên ngẫu nhiên
def tao_ho_ten():
    return f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"

# Hàm tạo danh sách điểm sinh viên
def tao_danh_sach_diem(so_luong):
    ds = [['HoTen', 'Toan', 'Ly', 'Hoa']]  # dòng tiêu đề
    for _ in range(so_luong):
        ho_ten = tao_ho_ten()
        toan = random.randint(0, 10)
        ly = random.randint(0, 10)
        hoa = random.randint(0, 10)
        ds.append([ho_ten, toan, ly, hoa])
    return ds

# Tạo nhiều file testcase
so_file = 5  # 5 file test
for i in range(1, so_file + 1):
    ten_file = f"diem_testcase_{i}.csv"
    danh_sach = tao_danh_sach_diem(random.randint(3, 8))  # mỗi file 3-8 sinh viên
    with open(ten_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(danh_sach)
    print(f"Đã tạo {ten_file} với {len(danh_sach) - 1} sinh viên.")
