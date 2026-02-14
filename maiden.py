from flask import Flask, jsonify, request, Response

app = Flask(__name__, template_folder="templates")

produse = [
    {"id": 1, "nume": "Laptop", "pret": 3000},
    {"id": 2, "nume": "Telefon", "pret": 1500},
    {"id": 3, "nume": "Vinil", "pret": 200},
    {"id": 4, "nume": "Căști", "pret": 500},
    {"id": 5, "nume": "Boxe", "pret": 800},
    {"id": 6, "nume": "Televizor", "pret": 4000},
    {"id": 7, "nume": "Frigider", "pret": 3500},
    {"id": 8, "nume": "Mașină de spălat", "pret": 2500},
    {"id": 9, "nume": "Cuptor", "pret": 1800},
    {"id": 10, "nume": "Aspirator", "pret": 1200},
    {"id": 11, "nume": "Cafetieră", "pret": 300},
    {"id": 12, "nume": "Mixer", "pret": 400},
    {"id": 13, "nume": "Fier de călcat", "pret": 350},
    {"id": 14, "nume": "Televizor OLED", "pret": 6000},
    {"id": 15, "nume": "Laptop Gaming", "pret": 8000},
    
]

@app.route('/', methods=['GET'])
def home():
    return "bine ai venit la magazinul nostru"

@app.route('/test-diacritice', methods=['GET'])
def test_diacritice():
    return Response("Și ășțî - diacritice OK", content_type="text/plain; charset=utf-8")

@app.route('/produse', methods=['GET'])
def get_produse():
    return jsonify({"date": produse})

@app.route('/produse/<int:produs_id>', methods=['GET'])
def get_produs(produs_id):
    rezultat = [p for p in produse if p["id"] == produs_id]
    if len(rezultat) == 0:
        return jsonify({"error": "Produsul nu a fost găsit"}), 404
    return jsonify(rezultat[0])
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

