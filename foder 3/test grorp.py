import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np


# Đọc dữ liệu từ file CSV
file_path = r'C:\Visual studio code\foder 3\Website Access Category.csv'

df = pd.read_csv(file_path)

# Chuyển cột 'Date' sang định dạng datetime
df['Date'] = pd.to_datetime(df['Date'])

# Tạo cột 'Day' là số ngày kể từ ngày đầu tiên
df['Day'] = (df['Date'] - df['Date'].min()).dt.days

# Chọn cột dùng để dự đoán: 'Day' và 'TotalAmount'
X = df[['Day']]  # Biến độc lập
y = df['TotalAmount']  # Biến phụ thuộc (tổng doanh thu)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình bằng cách tính toán lỗi trung bình bình phương (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Dự đoán cho các ngày trong tương lai (giả sử 30 ngày)
future_days = np.array(range(df['Day'].max() + 1, df['Day'].max() + 31)).reshape(-1, 1)
future_sales = model.predict(future_days)

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))

# Vẽ dữ liệu thực tế
plt.scatter(df['Day'], df['TotalAmount'], color='blue', label='Thực tế')

# Vẽ đường dự đoán cho dữ liệu thực tế
plt.plot(df['Day'], model.predict(df[['Day']]), color='green', label='Dự đoán hiện tại')

# Vẽ dự đoán cho tương lai
plt.plot(future_days, future_sales, color='red', linestyle='--', label='Dự đoán tương lai')

plt.xlabel('Số ngày kể từ ngày đầu tiên')
plt.ylabel('Tổng doanh thu')
plt.title('Dự đoán tăng trưởng doanh số trong tương lai')
plt.legend()

# Hiển thị biểu đồ
plt.show()
