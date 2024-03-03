import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score


df = pd.read_csv("data.csv")

# create x and y
x = df[["kategori_ram","kategori_rom","kategori_layar","kategori_kamera"]] # predictor
y = df["kategori_harga"] # response

X_train, X_valid, Y_train, Y_valid = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)


from sklearn.linear_model import LinearRegression
 
model_LR = LinearRegression()
model_LR.fit(X_train,Y_train)
df = df.sort_values(by='skor_total', ascending=False)

def seleksi(harga):
    if harga == "500.000-1.000.000":
        awal = 500000
        akhir = 1000000
    elif harga == "1.000.000-1.500.000":
        awal = 1000000
        akhir = 1500000
    elif harga == "1.500.000-2.000.000":
        awal = 1500000
        akhir = 2000000
    elif harga == "2.000.000-2.500.000":
        awal = 2000000
        akhir = 2500000
    elif harga == "2.500.000-3.000.000":
        awal = 2500000
        akhir = 3000000
    elif harga == "3.000.000-4.000.000":
        awal = 3000000
        akhir = 4000000
    elif harga == "4.000.000-5.000.000":
        awal = 4000000
        akhir = 5000000
    else:
        awal = 5000000
        akhir = 20000000
    seleksi = df[df["harga"] >= awal]  
    seleksi2 = seleksi[seleksi["harga"] <= akhir]
    foto = []
    nama = []
    harga = []
    rekomendasi = []
    link_hp = []
    for i in seleksi2["Link Foto"]:
        foto.append(i)
    for i in seleksi2["HP"]:
        nama.append(i)
    for i in seleksi2["Harga_rp"]:
        harga.append(i)
    for i in seleksi2["Link_Hp"]:
        link_hp.append(i)
    for i in seleksi2["skor_total"] :
      if i > seleksi.skor_total.quantile(0.75):
        rekomendasi.append("Very Recommended")
      elif i < seleksi.skor_total.quantile(0.25):
        rekomendasi.append("Not Recommended")
      else:
        rekomendasi.append("Recommended")
    
    return foto,nama,harga,rekomendasi,link_hp

def model(kegunaan,penyimpanan,layar,kamera):
    list1=[kegunaan,penyimpanan,layar,kamera]
    hasil= model_LR.predict([list1])
    hasil = int(hasil)
    if hasil == 1:
        harga = "500.000-1.000.000"
    elif hasil == 2:
        harga = "1.000.000-1.500.000"
    elif hasil == 3:
        harga = "1.500.000-2.000.000"
    elif hasil == 4:
        harga = "2.000.000-2.500.000"
    elif hasil == 5:
        harga = "2.500.000-3.000.000"
    elif hasil == 6:
        harga = "3.000.000-4.000.000"
    elif hasil == 7:
        harga = "4.000.000-5.000.000"
    else:
        harga = ">5.000.000"
    return harga
