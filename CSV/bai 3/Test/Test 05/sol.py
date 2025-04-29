import csv

def tinh_dtb_va_ghi_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            reader = csv.DictReader(f_in)
            sinh_vien_dtb = []

            for row in reader:
                ho_ten = row['HoTen']
                toan = float(row['Toan'])
                ly = float(row['Ly'])
                hoa = float(row['Hoa'])
                dtb = round((toan + ly + hoa) / 3, 1)
                sinh_vien_dtb.append({'HoTen': ho_ten, 'DTB': dtb})

        # Ghi ra file output
        with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
            fieldnames = ['HoTen', 'DTB']
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)

            writer.writeheader()
            for sv in sinh_vien_dtb:
                writer.writerow(sv)

        print(f"Đã ghi điểm trung bình ra file '{output_file}' thành công!")

    except FileNotFoundError:
        print(f"Không tìm thấy file: {input_file}")
    except KeyError:
        print(f"File {input_file} không đúng định dạng cột (HoTen, Toan, Ly, Hoa).")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng:
input_file = 'diem_testcase_5.csv'  # Hoặc 'diem_testcase_1.csv'
output_file = 'output.csv'
tinh_dtb_va_ghi_file(input_file, output_file)
