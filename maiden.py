from flask import Flask, jsonify, request, Response, render_template
from data import produse

app = Flask(__name__, template_folder="templates")
app.json.ensure_ascii = False


@app.route('/', methods=['GET'])
def home():
    return "Bine ai venit la magazinul nostru"


@app.route('/test-diacritice', methods=['GET'])
def test_diacritice():
    return Response(
        "Și ășțî - diacritice OK",
        content_type="text/plain; charset=utf-8"
    )


@app.route('/produse', methods=['GET'])
def get_produse():
    return jsonify({"date": produse})


@app.route('/produse/<int:produs_id>', methods=['GET'])
def get_produs(produs_id):
    rezultat = [p for p in produse if p["id"] == produs_id]

    if len(rezultat) == 0:
        return Response(
            "Produsul nu a fost găsit",
            status=404,
            content_type="text/plain; charset=utf-8"
        )

    produs = rezultat[0]
    return render_template("produs.html", produs=produs)


@app.route('/add_produs/', methods=['POST'])
def add_produs():

    nume = request.json['nume']
    pret = request.json['pret']

    for p in produse:
        if p["nume"].lower() == nume.lower():
            return Response(
                "Produsul exista deja",
                status=400,
                content_type="text/plain; charset=utf-8"
            )

    new_id = max(p["id"] for p in produse) + 1

    nou_produs = {
        "id": new_id,
        "nume": nume,
        "pret": pret
    }

    produse.append(nou_produs)

    return jsonify(nou_produs), 201
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)