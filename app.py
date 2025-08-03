from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Halo! Aplikasi ini siap menerima webhook dari n8n.'

# ENDPOINT BARU UNTUK WEBHOOK
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Ambil data JSON yang dikirim oleh n8n
    data = request.json

    # Cetak data yang diterima ke log untuk verifikasi
    print("=========================")
    print("Webhook diterima dari n8n!")
    print(f"Data: {data}")
    print("=========================")

    # Kirim balasan kembali ke n8n
    return jsonify({"status": "sukses", "data_diterima": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)