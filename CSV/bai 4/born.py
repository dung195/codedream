import csv
import random

# Danh sách mẫu cho họ tên
ho = ['Nguyen', 'Tran', 'Le', 'Pham', 'Hoang', 'Do', 'Bui']
ten_dem = ['Van', 'Thi', 'Minh', 'Thu', 'Quang', 'Hong', 'Huu']
ten = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def tao_ho_ten():
    return f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"

def tao_danh_sach_diem(so_luong):
    ds = [['HoTen', 'Toan', 'Ly', 'Hoa']]
    for _ in range(so_luong):
        ho_ten = tao_ho_ten()

        # 50% sinh viên sẽ có điểm khá cao
        if random.random() < 0.5:
            toan = random.randint(7, 10)
            ly = random.randint(7, 10)
            hoa = random.randint(7, 10)
        else:
            toan = random.randint(4, 8)
            ly = random.randint(4, 8)
            hoa = random.randint(4, 8)

        ds.append([ho_ten, toan, ly, hoa])
    return ds

# Tạo 5 file testcase
so_file = 5
for i in range(1, so_file + 1):
    ten_file = f"diem_baitap4_testcase_{i}.csv"
    danh_sach = tao_danh_sach_diem(random.randint(5, 10))  # mỗi file 5-10 sinh viên
    with open(ten_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(danh_sach)
    print(f"Đã tạo {ten_file} với {len(danh_sach) - 1} sinh viên.")
