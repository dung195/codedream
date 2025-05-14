import csv

def doc_va_in_sinhvien(ten_file, output_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f, open(output_file, 'w', encoding='utf-8') as out:
            reader = csv.DictReader(f)
            for row in reader:
                ho_ten = row['HoTen']
                tuoi = row['Tuoi']
                lop = row['Lop']
                # In trực tiếp bằng f-string
                out.write(f"Họ tên: {ho_ten} | Tuổi: {tuoi} | Lớp: {lop}\n")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {ten_file}")
    except KeyError:
        print(f"File {ten_file} không đúng định dạng cột yêu cầu (HoTen, Tuoi, Lop).")
    except Exception as e:  
        print(f"Đã xảy ra lỗi: {e}")

# Chạy cho tất cả các file từ sinhvien_testcase_1.csv -> sinhvien_testcase_5.csv
for i in range(1, 6):
    input_file = f'sinhvien_testcase_{i}.csv'
    output_file = f'sinhvien_testcase_{i:02}.out'
    doc_va_in_sinhvien(input_file, output_file)
