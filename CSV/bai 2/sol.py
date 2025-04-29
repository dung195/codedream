import csv
import sys
sys.stdout=open("diem.out","w",encoding='utf-8')
def tinh_diem_trung_binh(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ho_ten = row['HoTen']
                toan = float(row['Toan'])
                ly = float(row['Ly'])
                hoa = float(row['Hoa'])
                dtb = (toan + ly + hoa) / 3
                print(f"{ho_ten} - ĐTB: {dtb:.1f}")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {ten_file}")
    except KeyError:
        print(f"File {ten_file} không đúng định dạng cột (HoTen, Toan, Ly, Hoa).")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
# Ví dụ sử dụng
ten_file = 'diem_testcase_1.csv'  # Hoặc thay bằng 'diem_testcase_1.csv', v.v. để test
tinh_diem_trung_binh(ten_file)
