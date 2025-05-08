from openpyxl import Workbook
import random

# Danh sách dữ liệu mẫu
ten_list = ["Nguyễn Văn A", "Trần Thị B", "Lê Minh C", "Phạm Thị D", "Đỗ Trung E", 
            "Vũ Hải N", "Ngô Minh H", "Phan Thanh P", "Bùi Thị T", "Đinh Văn M"]
chuc_vu_list = ["Nhân viên", "Kế toán", "Kỹ sư", "Trưởng phòng", "Quản lý", "Giám đốc"]

def sinh_file_employees(ten_file, so_nhan_vien):
    wb = Workbook()
    ws = wb.active
    ws.title = "Danh sách"

    # Ghi tiêu đề
    ws.append(["Tên", "Chức vụ", "Lương"])

    for _ in range(so_nhan_vien):
        ten = random.choice(ten_list)
        chuc_vu = random.choice(chuc_vu_list)
        luong = random.randint(7_000_000, 22_000_000)
        ws.append([ten, chuc_vu, luong])

    wb.save(ten_file)
    print(f"✅ Đã tạo file: {ten_file}")

# Sinh 5 test
for i in range(1, 6):
    ten_file = f"employees_test_{i}.xlsx"
    so_nhan_vien = random.randint(8, 20)
    sinh_file_employees(ten_file, so_nhan_vien)
