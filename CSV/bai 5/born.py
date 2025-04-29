import csv
import random

# Các danh sách mẫu để random
ho = ['Nguyen', 'Tran', 'Le', 'Pham', 'Hoang', 'Do', 'Bui', 'Dang']
ten_dem = ['Van', 'Thi', 'Minh', 'Hong', 'Quang', 'Bao', 'Thu']
ten = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K']

ky_nang_lap_trinh = ['Lập trình Python', 'Lập trình C++', 'Lập trình Web', 'Lập trình di động']
ky_nang_khac = ['Thiết kế đồ họa', 'Phân tích dữ liệu', 'Marketing', 'Quản trị hệ thống', 'Hỗ trợ kỹ thuật']

def tao_ho_ten():
    return f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"

def tao_ky_nang():
    # 50% cơ hội chọn kỹ năng lập trình
    if random.random() < 0.5:
        return random.choice(ky_nang_lap_trinh)
    else:
        return random.choice(ky_nang_khac)

def tao_danh_sach_ung_vien(so_luong):
    ds = [['Ten', 'Tuoi', 'KinhNghiem', 'KyNang']]
    for _ in range(so_luong):
        ten = tao_ho_ten()
        tuoi = random.randint(20, 35)
        kinh_nghiem = random.randint(0, 7)  # 0-7 năm kinh nghiệm
        ky_nang = tao_ky_nang()
        ds.append([ten, tuoi, kinh_nghiem, ky_nang])
    return ds

# Tạo 5 file testcase
for i in range(1, 6):
    ten_file = f"hosoxinviec_testcase_{i}.csv"
    danh_sach = tao_danh_sach_ung_vien(random.randint(7, 12))  # mỗi file 7-12 ứng viên
    with open(ten_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(danh_sach)
    print(f"Đã tạo {ten_file} với {len(danh_sach)-1} ứng viên.")
