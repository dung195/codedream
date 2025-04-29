import csv

def loc_hoc_sinh_gioi(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            reader = csv.DictReader(f_in)
            danh_sach_gioi = []

            for row in reader:
                ho_ten = row['HoTen']
                toan = float(row['Toan'])
                ly = float(row['Ly'])
                hoa = float(row['Hoa'])
                dtb = (toan + ly + hoa) / 3

                if dtb >= 8.0:
                    danh_sach_gioi.append({
                        'HoTen': ho_ten,
                        'Toan': toan,
                        'Ly': ly,
                        'Hoa': hoa,
                        'DTB': round(dtb, 1)
                    })

        # Ghi các bạn học sinh giỏi ra file
        with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
            fieldnames = ['HoTen', 'Toan', 'Ly', 'Hoa', 'DTB']
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)

            writer.writeheader()
            for sv in danh_sach_gioi:
                writer.writerow(sv)

        print(f"Đã lọc và ghi {len(danh_sach_gioi)} học sinh giỏi ra file '{output_file}' thành công!")

    except FileNotFoundError:
        print(f"Không tìm thấy file: {input_file}")
    except KeyError:
        print(f"File {input_file} không đúng định dạng cột (HoTen, Toan, Ly, Hoa).")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng:
input_file = 'diem_baitap4_testcase_5.csv'  # hoặc 'diem.csv' tùy bài
output_file = 'gioi.csv'
loc_hoc_sinh_gioi(input_file, output_file)
