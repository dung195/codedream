from openpyxl import Workbook
import random

# Danh sách sản phẩm, danh mục và giá
ten_san_pham_list = ["Laptop", "Điện thoại", "Máy tính bảng", "Tai nghe", "Chuột", "Bàn phím", "Loa", "Máy in", "Tivi", "Camera"]
danh_muc_list = ["Điện tử", "Phụ kiện", "Mỹ phẩm", "Thực phẩm", "Nhà cửa"]
gia_min, gia_max = 1000000, 50000000  # Giá sản phẩm

def sinh_file_products(ten_file, so_san_pham):
    wb = Workbook()
    ws = wb.active
    ws.title = "Danh sách sản phẩm"

    # Ghi tiêu đề
    ws.append(["Tên sản phẩm", "Danh mục", "Giá"])

    for _ in range(so_san_pham):
        ten_san_pham = random.choice(ten_san_pham_list)
        danh_muc = random.choice(danh_muc_list)
        gia = random.randint(gia_min, gia_max)
        ws.append([ten_san_pham, danh_muc, gia])

    wb.save(ten_file)
    print(f"✅ Đã tạo file: {ten_file}")

# Sinh 5 test
for i in range(1, 6):
    ten_file = f"products_test_{i}.xlsx"
    so_san_pham = random.randint(8, 20)
    sinh_file_products(ten_file, so_san_pham)
