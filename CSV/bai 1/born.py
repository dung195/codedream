import csv
import random

# Một số danh sách mẫu để random tên và lớp
ho = ['Nguyen', 'Tran', 'Le', 'Pham', 'Hoang', 'Do', 'Bui']
ten_dem = ['Van', 'Thi', 'Minh', 'Thu', 'Quang', 'Hong', 'Huu']
ten = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
lop = ['12A1', '12A2', '12A3', '11B1', '11B2']

# Hàm tạo 1 tên sinh viên ngẫu nhiên
def tao_ho_ten():
    return f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"

# Hàm tạo 1 danh sách sinh viên
def tao_danh_sach_sv(so_luong):
    ds = [['HoTen', 'Tuoi', 'Lop']]  # dòng tiêu đề
    for _ in range(so_luong):
        ho_ten = tao_ho_ten()
        tuoi = random.randint(16, 20)  # Tuổi từ 16–20
        lop_hoc = random.choice(lop)
        ds.append([ho_ten, tuoi, lop_hoc])
    return ds

# Tạo nhiều file testcase
so_file = 5  # Ví dụ: tạo 5 file
for i in range(1, so_file + 1):
    ten_file = f"sinhvien_testcase_{i}.csv"
    danh_sach = tao_danh_sach_sv(random.randint(3, 10))  # Mỗi file random 3-10 sinh viên
    with open(ten_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(danh_sach)
    print(f"Đã tạo {ten_file} với {len(danh_sach) - 1} sinh viên.")
