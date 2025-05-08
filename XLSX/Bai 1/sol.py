import pandas as pd

# Đọc file Excel
input_file = 'students_test_5.xlsx'
output_file = 'student.out'

try:
    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(input_file)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Danh sách học sinh:\n")
        f.write("-" * 40 + "\n")

        # Duyệt qua từng dòng và ghi ra file
        for index, row in df.iterrows():
            ho_ten = row['Họ tên']
            tuoi = row['Tuổi']
            lop = row['Lớp']
            line = f"{index + 1}. Họ tên: {ho_ten}, Tuổi: {tuoi}, Lớp: {lop}\n"
            f.write(line)

    print(f"✅ Đã ghi danh sách học sinh vào file '{output_file}'.")

except FileNotFoundError:
    print(f"❌ Không tìm thấy file: {input_file}")
except Exception as e:
    print(f"⚠️ Lỗi xảy ra: {e}")
