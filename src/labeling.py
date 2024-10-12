import pandas as pd
import os

# Load the dataset
script_dir = os.path.dirname(__file__)  # Mendapatkan lokasi file .py
file_path = os.path.join(script_dir, 'sampled_comments.csv')
clean_df = pd.read_csv(file_path)

# Cek apakah kolom 'label' sudah ada, jika belum tambahkan kolom tersebut
if 'label' not in clean_df.columns:
    clean_df['label'] = None  # Menambahkan kolom 'label' dengan nilai default None

# Fungsi untuk meminta input pengguna
def label_komentar():
    while True:
        try:
            label = int(input("(1=positif, 2=netral, 3=negatif, 0=berhenti): "))
            if label == 1:
                return 'positif'
            elif label == 2:
                return 'netral'
            elif label == 3:
                return 'negatif'
            elif label == 0:
                return 'berhenti'
            else:
                print("Input tidak valid. Masukkan angka 1, 2, 3, atau 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka 1, 2, 3, atau 0.")

# Menambahkan label berdasarkan input pengguna hanya untuk data yang belum memiliki label
def label_comments(df, file_path):
    for i, row in df.iterrows():
        if pd.isnull(row['label']):  # Hanya memproses komentar yang belum memiliki label
            print(f"\nKomentar: {row['textOriginal']}")
            label = label_komentar()
            if label == 'berhenti':
                break
            df.at[i, 'label'] = label
            print(f"Label '{label}' tersimpan untuk komentar: {row['textOriginal']}")
            
            # Update file CSV secara langsung
            df.to_csv(file_path, index=False)
            print("File CSV diperbarui dengan label baru.")
    return df

# Melabeli komentar dan memperbarui CSV secara langsung
clean_df = label_comments(clean_df, file_path)

print("Program berhenti. Data yang sudah dilabeli tersimpan dalam sampled_comments.csv.")
