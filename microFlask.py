from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo (em produção, usaríamos um banco de dados)
produtos = [
    {"id": 1, "nome": "Produto A", "preco": 100.0},
    {"id": 2, "nome": "Produto B", "preco": 200.0}
]

# Rota para listar todos os produtos
@app.route('/produtos', methods=['GET'])
def obter_produtos():
    return jsonify(produtos)

# Rota para obter um produto específico
@app.route('/produtos/', methods=['GET'])
def obter_produto(produto_id):
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)


