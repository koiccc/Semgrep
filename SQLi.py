import sqlite3

# Giả lập kết nối database
conn = sqlite3.connect(':memory:') 
cursor = conn.cursor()

# Tạo bảng và dữ liệu mẫu
cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'admin', 'matkhau123')")
cursor.execute("INSERT INTO users VALUES (2, 'user', '123456')")

def dang_nhap_co_loi(username_input):
    # --- ĐÂY LÀ DÒNG GÂY LỖI ---
    # Việc ghép chuỗi trực tiếp khiến dữ liệu đầu vào biến thành 1 phần của câu lệnh
    query = f"SELECT * FROM users WHERE username = '{username_input}'"
    
    print(f"Câu lệnh SQL thực thi: {query}") # In ra để bạn thấy rõ
    cursor.execute(query)
    return cursor.fetchall()

# Chạy thử
user_input = input("Nhập tên đăng nhập: ")
ket_qua = dang_nhap_co_loi(user_input)
print("Kết quả:", ket_qua)
