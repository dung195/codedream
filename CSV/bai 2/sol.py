import csv
import sys

def tinh_diem_trung_binh(ten_file, output_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f, open(output_file, 'w', encoding='utf-8') as out:
            sys.stdout = out  # Redirect output to the file
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
    finally:
        sys.stdout = sys.__stdout__  # Reset stdout to default

# Loop through test case files
for i in range(1, 6):
    input_file = f'diem_testcase_{i}.csv'
    output_file = f'0{i}.out'
    tinh_diem_trung_binh(input_file, output_file)
