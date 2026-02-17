import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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


def analyze_3_correlation(df):
	# Hàm vẽ Heatmap để soi mối quan hệ giữa các cột số.
	plt.figure(figsize=(10, 8))

	# 1. Tính toán ma trận tương quan (chỉ tính trên các cột số)
	correlation_matrix = df.corr()

	# 2. Vẽ Heatmap
	# annot=True: Hiện con số cụ thể lên ô
	# fmt=".2f": Lấy 2 chữ số thập phân (ví dụ 0.49)
	# cmap='coolwarm': Dải màu từ Xanh (Lạnh/Âm) sang Đỏ (Nóng/Dương)
	sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)

	plt.title("Ma trận tương quan: Yếu tố nào gây ra tiểu đường?")
	plt.show()


if __name__ == "__main__":
	analyze_3_correlation(df)
