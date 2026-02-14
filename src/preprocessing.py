import pandas as pd
import os


def load_data(filepath):
	"""
	Hàm đọc dữ liệu từ file CSV
	"""
	if not os.path.exists(filepath):
		print(f"❌ Lỗi: Không tìm thấy file tại {filepath}")
		return None

	# Đọc file bằng Pandas
	df = pd.read_csv(filepath)
	print(f"✅ Đã load thành công! Kích thước dữ liệu: {df.shape}")
	print("5 dòng đầu tiên:")
	print(df.head())
	return df


if __name__ == "__main__":
	# Đường dẫn tương đối từ thư mục src ra thư mục data
	# Lưu ý: Cần đảm bảo bạn đã copy file diabetes.csv vào folder data/raw
	path = "../data/raw/diabetes.csv"
	load_data(path)