import csv
import sys
sys.stdout=open('sinhvien.out',"w",encoding='utf-8')
def doc_va_in_sinhvien(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:  # Đọc file kiểu text (không phải bytes!)
            reader = csv.DictReader(f)
            for row in reader:
                ho_ten = row['HoTen']
                tuoi = row['Tuoi']
                lop = row['Lop']
                # In trực tiếp bằng f-string
                print(f"Họ tên: {ho_ten} | Tuổi: {tuoi} | Lớp: {lop}")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {ten_file}")
    except KeyError:
        print(f"File {ten_file} không đúng định dạng cột yêu cầu (HoTen, Tuoi, Lop).")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
ten_file = 'sinhvien_testcase_5.csv'  # hoặc file testcase bạn muốn
doc_va_in_sinhvien(ten_file)
