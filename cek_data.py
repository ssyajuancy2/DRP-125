import pandas as pd

# Input dan pembacaan data
df = pd.read_csv("dfTransjakarta.csv", sep=",")

print(df.shape)  # (37900, 22)
print(df.head())

# Cek kesehatan data (kosong, duplikat, tipe data)
print("\nMissing Values:")
print(df.isna().sum())

df.info()

# Cek duplikat
print("\nJumlah data duplikat:", df.duplicated().sum())

# Cek konsistensi penulisan
print("\nJenis Bank:")
print(df["payCardBank"].value_counts())

print("\nJenis Kelamin:")
print(df["payCardSex"].value_counts())

print("\nArah Perjalanan:")
print(df["direction"].value_counts())

print("\nKoridor:")
print(df["corridorID"].value_counts())

# Cek kolom numerik
print("\nStatistik Deskriptif:")
kolom_numerik = [
    "payCardBirthDate",
    "direction",
    "tapInStopsLat",
    "tapInStopsLon",
    "stopStartSeq",
    "tapOutStopsLat",
    "tapOutStopsLon",
    "stopEndSeq",
    "payAmount"
]

print(df[kolom_numerik].describe())

# Cek spasi berlebih pada kolom teks
print("\nJumlah Data Unik Setelah Strip:")

kolom_teks = [
    "payCardBank",
    "payCardName",
    "payCardSex",
    "corridorName",
    "tapInStopsName",
    "tapOutStopsName"
]

for kolom in kolom_teks:
    print(kolom, df[kolom].str.strip().nunique())

# Hapus spasi berlebih
for kolom in df.select_dtypes(include="object").columns:
    df[kolom] = df[kolom].str.strip()

# Cek nilai minimum, median, dan maksimum
print("\nNilai Minimum, Median, Maksimum:")
print(df.describe().T[["min", "50%", "max"]])

# Cek keunikan Transaction ID
print("\nApakah jumlah TransID sama dengan total baris?")
print(df["transID"].nunique() == len(df))

# Cek TransID yang sama
print("\nData dengan TransID yang sama:")
print(df[df.duplicated("transID", keep=False)])

# Cek jumlah kartu pelanggan unik
print("\nJumlah kartu pelanggan unik:")
print(df["payCardID"].nunique())

# Cek nilai pembayaran
print("\nJumlah transaksi dengan pembayaran 0:")
print((df["payAmount"] == 0).sum())

# Cek nilai pembayaran negatif
print("\nJumlah pembayaran negatif:")
print((df["payAmount"] < 0).sum())

# Cek nilai arah perjalanan
print("\nNilai direction yang tersedia:")
print(df["direction"].unique())

# Cek data yang memiliki informasi halte tujuan kosong
print("\nJumlah data halte tujuan kosong:")
print(df["tapOutStopsName"].isna().sum())

# Hapus data duplikat
df = df.drop_duplicates()

print("\nUkuran data setelah cleansing:")
print(df.shape)
