import pandas as pd
import random

# Tạo tên ngẫu nhiên
ho = ["Nguyễn", "Trần", "Lê", "Phạm", "Đỗ", "Hoàng", "Vũ"]
ten_dem = ["Văn", "Thị", "Minh", "Ngọc", "Hữu", "Gia"]
ten = ["An", "Bình", "Chi", "Dũng", "Hà", "Khoa", "Linh", "Nam", "Oanh", "Phúc"]

def tao_ho_ten():
    return f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"

def diem_ngau_nhien():
    return round(random.uniform(0, 10), 1)

def sinh_file_diem(so_hoc_sinh, ten_file):
    data = {
        'Họ tên': [tao_ho_ten() for _ in range(so_hoc_sinh)],
        'Toán': [diem_ngau_nhien() for _ in range(so_hoc_sinh)],
        'Văn': [diem_ngau_nhien() for _ in range(so_hoc_sinh)],
        'Anh': [diem_ngau_nhien() for _ in range(so_hoc_sinh)]
    }
    df = pd.DataFrame(data)
    df.to_excel(ten_file, index=False)
    print(f"✅ Đã tạo file: {ten_file}")

# Sinh 5 file test
for i in range(1, 6):
    sinh_file_diem(so_hoc_sinh=random.randint(5, 15), ten_file=f"grades_test_{i}.xlsx")
