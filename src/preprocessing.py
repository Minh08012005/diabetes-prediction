import pandas as pd
import numpy as np

def load_data(path="../data/raw/diabetes.csv"):
	return pd.read_csv(path)

def clean_data(df):
	"""
	    Hàm này thực hiện:
	    1. Biến các số 0 vô lý thành NaN (Not a Number) để máy hiểu là dữ liệu thiếu.
	    2. Điền vào chỗ thiếu đó bằng giá trị Median (Trung vị).
	"""

# Danh sách các cột không thể bằng 0
# (Lưu ý: Pregnancies được phép bằng 0 vì có thể chưa mang thai bao giờ)

	cols_bad_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

	# BƯỚC 1: Thay số 0 bằng NaN (Rỗng)
	# Giống như việc đánh dấu vào sổ: "Chỗ này đang thiếu nhé"
	df[cols_bad_zeros] = df[cols_bad_zeros].replace(0, np.nan)

	# Kiểm tra xem thiếu bao nhiêu (In ra để báo cáo cô giáo)
	print("Số lượng dữ liệu bị thiếu (NaN) sau khi thay thế số 0:")
	print(df[cols_bad_zeros].isnull().sum())
	print("-" * 30)

	# BƯỚC 2: Điền dữ liệu thiếu bằng MEDIAN
	# Tại sao dùng Median? Vì biểu đồ Box Plot cho thấy dữ liệu có nhiều Outliers (Nhiễu).
	for col in cols_bad_zeros:
		median_val = df[col].median()  # Tìm con số đứng giữa
		df[col] = df[col].fillna(median_val)  # Lấp chỗ trống
		print(f"-> Đã điền cột {col} bằng giá trị Median: {median_val}")

	return df


# Chạy thử nghiệm
if __name__ == "__main__":
	# Đường dẫn file (sửa lại cho đúng máy bạn)
	file_path = "../data/raw/diabetes.csv"
	try:
		df = load_data(file_path)
		print("--- TRƯỚC KHI XỬ LÝ ---")
		print(df.head())  # Xem 5 dòng đầu

		df_clean = clean_data(df)

		print("\n--- SAU KHI XỬ LÝ (SẠCH SẼ) ---")
		print(df_clean.head())

		# Kiểm tra lại xem còn số 0 ở cột Insulin không?
		print("\nKiểm tra lại min của Insulin:", df_clean['Insulin'].min())

	except FileNotFoundError:
		print("Lỗi: Không tìm thấy file dữ liệu. Kiểm tra lại đường dẫn!")
