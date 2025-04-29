import csv

def loc_ung_vien_tiem_nang(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            reader = csv.DictReader(f_in)
            danh_sach_ung_vien = []

            for row in reader:
                ho_ten = row['Ten']
                tuoi = int(row['Tuoi'])
                kinh_nghiem = int(row['KinhNghiem'])
                ky_nang = row['KyNang']

                # Kiểm tra điều kiện
                if kinh_nghiem >= 2 and 'lập trình' in ky_nang.lower():
                    danh_sach_ung_vien.append({
                        'Ten': ho_ten,
                        'Tuoi': tuoi,
                        'KinhNghiem': kinh_nghiem,
                        'KyNang': ky_nang
                    })

        # Ghi danh sách ứng viên tiềm năng ra file
        with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
            fieldnames = ['Ten', 'Tuoi', 'KinhNghiem', 'KyNang']
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)

            writer.writeheader()
            for ung_vien in danh_sach_ung_vien:
                writer.writerow(ung_vien)

        print(f"Đã lọc và ghi {len(danh_sach_ung_vien)} ứng viên tiềm năng vào file '{output_file}'.")

    except FileNotFoundError:
        print(f"Không tìm thấy file: {input_file}")
    except KeyError:
        print(f"File {input_file} không đúng định dạng cột (Ten, Tuoi, KinhNghiem, KyNang).")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng:
input_file = 'hosoxinviec_testcase_5.csv'
output_file = 'ungvien_tiemnang.csv'
loc_ung_vien_tiem_nang(input_file, output_file)
