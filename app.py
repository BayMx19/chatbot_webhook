from flask import Flask, request, jsonify # type: ignore
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory # type: ignore

app = Flask(__name__)

# Buat objek stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillment_text = "Maaf, saya tidak mengerti."

    if req.get("queryResult"):
        query_result = req.get("queryResult")
        user_input = query_result.get("queryText")
        
        # Melakukan stemming pada input pengguna
        stemmed_input = stemmer.stem(user_input.lower())
        
        # Tanggapan berdasarkan kata dasar dari input pengguna
        if 'toko' in stemmed_input or 'alamat' in stemmed_input or 'lokasi' in stemmed_input or 'tempat' in stemmed_input:
            fulfillment_text = "Toko berada di Jalan Pulo Wonokromo No.304, Wonokromo, Kota Surabaya, Jawa Timur 60241, Indonesia dan sayangnya umkm hafidz pigura belum memiliki cabang toko ditempat lainnya."
        elif 'harga' in stemmed_input or 'cost' in stemmed_input or 'biaya' in stemmed_input or 'tarif' in stemmed_input:
            fulfillment_text = "Harga pigura dimulai dari 15.000 dan harga pigura custom menyesuaikan dengan ukuran yang anda inginkan"
        elif 'pengiriman' in stemmed_input or 'pengantaran' in stemmed_input or 'penyaluran' in stemmed_input or 'pendistribusian' in stemmed_input or 'mengantar' in stemmed_input or 'penyerahan' in stemmed_input or 'kirim' in stemmed_input:
            fulfillment_text = "Pengiriman produk umkm hafidz pigura bisa melalui ojek online baik grab, gojek, atau yang lainnya, hafidz pigura bisa mengirim ke luar kota menggunakan layanan jasa ekspedisi yang ada."
        elif 'ukuran' in stemmed_input or 'besar' in stemmed_input or 'besaran' in stemmed_input or 'dimensi' in stemmed_input:
            fulfillment_text = "Saat ini kami memiliki ketersedian ukuran pigura a4, a3n, dan kami menyediakan jasa custom ukuran dan bentuk pigura sesuai kebutahan anda"
        elif 'pagi' in stemmed_input or 'halo' in stemmed_input or 'hai' in stemmed_input or 'assalamualaikum' in stemmed_input:
            fulfillment_text = "Hai! dengan Hafidz Pigura disini. Ada yang bisa dibantu?"

    response = {
        "fulfillmentText": fulfillment_text
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
