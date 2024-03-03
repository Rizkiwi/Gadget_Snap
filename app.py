from flask import Flask, redirect, url_for, request, render_template ,send_file, flash, jsonify
from prediksi import model,seleksi

app = Flask(__name__)
app.secret_key = "Rizkiwi"

@app.route("/")
def halaman1():
    return render_template("index.html")

@app.route("/index")
def halaman_1():
    return render_template("index.html")

@app.route("/layanan")
def halaman2():
    return render_template("layanan.html")
    
@app.route("/tentang")
def halaman4():
    return render_template("tentang.html")

@app.route('/rekomendasi', methods=['GET', 'POST'])
def basic():
    status = False
    if request.method == 'POST':
        try:
            kegunaan = int(request.form["kegunaan"]) 
            penyimpanan = int(request.form["penyimpanan"])
            layar = int(request.form['layar'])
            kamera = int(request.form["kamera"])
            harga1 = model(kegunaan,penyimpanan,layar,kamera)
            link,hp,price,rekomen,link_hp = seleksi(harga1)
            status = True
            return render_template("rekomendasi.html", total=harga1, foto=link, nama=hp, harga=price, rekomendasi = rekomen,link_hp=link_hp, status=status)
        except Exception as e:
            error = {"error" : e}
            return render_template("rekomendasi.html", error = error, status=status)


    elif request.method == 'GET':
        return render_template("rekomendasi.html", status=status)
@app.route('/rekomendasi2', methods=['GET', 'POST'])
def rekomend():
    status = False
    if request.method == 'POST':
        try:
            kegunaan2 = int(request.form["kegunaan2"]) 
            penyimpanan2 = int(request.form["penyimpanan2"])
            layar2 = int(request.form['layar2'])
            kamera2 = int(request.form["kamera2"])
            harga2 = model(kegunaan2,penyimpanan2,layar2,kamera2)
            link2,hp2,price2,rekomen2,link_hp2 = seleksi(harga2)
            status = True
            return render_template("rekomendasi.html", total=harga2, foto=link2, nama=hp2, harga=price2, rekomendasi = rekomen2,link_hp=link_hp2, status=status)
        except Exception as e:
            error = {"error" : e}
            return render_template("rekomendasi.html", error = error, status=status)


    elif request.method == 'GET':
        return render_template("rekomendasi.html", status=status)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
