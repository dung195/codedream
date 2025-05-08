import pandas as pd
import random

# Danh sách tên để kết hợp ngẫu nhiên
ho = ["Nguyễn", "Trần", "Lê", "Phạm", "Đỗ", "Hoàng", "Vũ"]
ten_dem = ["Văn", "Thị", "Minh", "Hữu", "Ngọc", "Thùy", "Gia"]
ten = ["An", "Bình", "Chi", "Dũng", "Hà", "Khoa", "Linh", "Nam", "Oanh", "Phúc"]

# Danh sách lớp
lop_list = [f"{k}{c}{n}" for k in range(6,13) for c in ['A','B','C'] for n in range(1,4)]

def tao_ho_ten():
    return f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"

def sinh_file_test(so_hoc_sinh, ten_file):
    data = {
        'Họ tên': [tao_ho_ten() for _ in range(so_hoc_sinh)],
        'Tuổi': [random.randint(12, 18) for _ in range(so_hoc_sinh)],
        'Lớp': [random.choice(lop_list) for _ in range(so_hoc_sinh)]
    }
    df = pd.DataFrame(data)
    df.to_excel(ten_file, index=False)
    print(f"✅ Đã tạo file: {ten_file}")

# Sinh 5 bộ test
for i in range(1, 6):
    sinh_file_test(so_hoc_sinh=random.randint(5, 20), ten_file=f"students_test_{i}.xlsx")
