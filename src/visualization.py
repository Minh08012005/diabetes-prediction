import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  # Dành cho phần Boardcasting.
import os

# Cau hinh giao dien
sns.set_theme(style="whitegrid")


def load_data():
	# Đường dẫn tương đối từ thư mục src ra thư mục data
	path = "../data/raw/diabetes.csv"
	if not os.path.exists(path):
		# fall back to absolute path if relative path doesn't work
		path = "data/raw/diabetes.csv"
	return pd.read_csv(path)


df = load_data()


# Vẽ biểu đồ phân phối của cột "Glucose"
def analyze_1_distribution(df):
	# Hàm vẽ Histogram và Density Plot để soi phân phối dữ liệu
	# 1. Tạo một cái khung tranh to (chiều ngang 14 inch, dọc 6 inch)

	plt.figure(figsize=(14, 6))

	# --- HÌNH BÊN TRÁI: GLUCOSE ---
	# Chia khung tranh làm 1 hàng, 2 cột, và vẽ vào vị trí số 1
	plt.subplot(1, 2, 1)

	# Lệnh vẽ chính: Histogram kết hợp KDE
	sns.histplot(data=df, x='Glucose', kde=True, bins=30, color='blue')

	plt.title('Phân phối đường huyết (Glucose) - Gần giống hình chuông')
	plt.xlabel('Chỉ số Glucose')
	plt.ylabel('Số lượng bệnh nhân')

	# --- HÌNH BÊN PHẢI: AGE (TUỔI) ---
	# Vẽ vào vị trí số 2
	plt.subplot(1, 2, 2)

	sns.histplot(data=df, x='Age', kde=True, bins=30, color='green')

	plt.title('Phân phối Tuổi (Age) - Bị lệch phải (Skewed)')
	plt.xlabel('Tuổi')
	plt.ylabel('Số lượng bệnh nhân')

	# Hiển thị tất cả lên màn hình.
	plt.tight_layout()
	plt.show()


if __name__ == "__main__":
	analyze_1_distribution(df)
