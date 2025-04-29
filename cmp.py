def are_files_identical(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            b1 = f1.read(4096)  # đọc theo block 4KB
            b2 = f2.read(4096)
            if b1 != b2:
                return False
            if not b1:  # đọc hết file
                return True

file1 = 'xxx.xlsx'
file2 = 'bbb.xlsx'

if are_files_identical(file1, file2):
    print("Hai file giống hệt nhau.".encode('utf-8').decode('utf-8'))
else:
    print("Hai file KHÁC nhau.".encode('utf-8').decode('utf-8'))
