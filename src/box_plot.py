import matplotlib.pyplot as plt
import pandas as pd
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


def analyze_2_boxplot(df):
	# Hàm vẽ Box Plot để tìm ra outliers
	plt.figure(figsize=(14, 6))

	# --- HÌNH 1: INSULIN ---

	plt.subplot(1, 2, 1)
	sns.boxplot(data=df, x='Insulin', color='orange')
	plt.title('Box Plot: Chỉ số Insulin (Nhiều Outliers)')
	plt.ylabel('Mức Insulin (mu U/ml')

	# --- HÌNH 2: PREGNANCIES (SỐ LẦN MANG THAI) ---.
	plt.subplot(1, 2, 2)


	sns.boxplot(data=df, y='Pregnancies', color='purple')
	plt.title('Box Plot: Số lần mang thai')
	plt.ylabel('Số lần')

	plt.tight_layout()
	plt.show()

if __name__ == "__main__":
	analyze_2_boxplot(df)
