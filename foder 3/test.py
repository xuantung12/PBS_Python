import csv

with open('file.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

import pandas as pd

def is_valid_date(date_str):
    try:
        pd.to_datetime(date_str)
        return True
    except ValueError:
        return False

def process_csv(file_path):
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(file_path)
    
    # Kiểm tra dữ liệu trống
    if data.isnull().sum().sum() > 0:
        print("Dữ liệu có chứa giá trị trống.")
    else:
        print("Không có giá trị trống trong dữ liệu.")
    
    # Kiểm tra định dạng ngày hợp lệ cho các cột DateOfBirth và RegistrationDate
    data['DateOfBirth_Valid'] = data['DateOfBirth'].apply(is_valid_date)
    data['RegistrationDate_Valid'] = data['RegistrationDate'].apply(is_valid_date)
    
    # Lọc ra các hàng có định dạng ngày không hợp lệ
    invalid_date_entries = data[(~data['DateOfBirth_Valid']) | (~data['RegistrationDate_Valid'])]
    
    if not invalid_date_entries.empty:
        print("Dữ liệu có chứa giá trị lỗi định dạng ngày tháng.")
        print(invalid_date_entries[['CustomerID', 'DateOfBirth', 'RegistrationDate']])
    else:
        print("Tất cả các giá trị ngày tháng đều hợp lệ.")
    
    # Loại bỏ các cột tạm thời
    data.drop(columns=['DateOfBirth_Valid', 'RegistrationDate_Valid'], inplace=True)
    
    return data

# Đường dẫn đến file CSV
file_path = 'sale_data.csv'
# Xử lý file CSV
processed_data = process_csv(file_path)

# Hiển thị vài dòng đầu tiên của dữ liệu đã xử lý
print(processed_data.head())