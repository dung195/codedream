from openpyxl import Workbook
import random

# Danh sách tên khách hàng mẫu
khach_hang_list = ["Nguyễn Văn A", "Trần Thị B", "Lê Minh C", "Phạm Thị D", "Đỗ Trung E", 
                   "Vũ Hải N", "Ngô Minh H", "Phan Thanh P", "Bùi Thị T", "Đinh Văn M"]

def sinh_file_orders(ten_file, so_don_hang):
    wb = Workbook()
    ws = wb.active
    ws.title = "Danh sách đơn hàng"

    # Ghi tiêu đề
    ws.append(["Mã đơn", "Khách hàng", "Số tiền", "Trạng thái"])

    for _ in range(so_don_hang):
        ma_don = f"DH{random.randint(1000, 9999)}"
        khach_hang = random.choice(khach_hang_list)
        so_tien = random.randint(0, 10000000)  # Số tiền từ 0 đến 10 triệu
        trang_thai = "Đang xử lý" if so_tien > 0 else "Hủy"
        ws.append([ma_don, khach_hang, so_tien, trang_thai])

    wb.save(ten_file)
    print(f"✅ Đã tạo file: {ten_file}")

# Sinh 5 test
for i in range(1, 6):
    ten_file = f"orders_test_{i}.xlsx"
    so_don_hang = random.randint(8, 20)
    sinh_file_orders(ten_file, so_don_hang)
