from flask import Flask, jsonify, request

app = Flask(__name__)

materiais = []
quantidades = []

#Listar materiais
@app.route('/materials', methods=['GET'])
def listar_materiais():
    lista_materiais = []
    for i, material in enumerate(materiais):
        lista_materiais.append({
            "id": i,
            "name": material,
            "qtde": quantidades[i]
        })
    return jsonify(lista_materiais), 200

#Criar
@app.route('/materials', methods=['POST'])
def criar_material():
    material = request.json.get('material')
    if not material:
        return 'Bad request', 400
    nome_material = material.get('name')
    qtde_material = material.get('qtde')
    if not nome_material or not qtde_material:
        return 'Bad request', 400
    materiais.append(nome_material)
    quantidades.append(qtde_material)
    return 'Created', 201

#Buscar por ID
@app.route('/materials/<int:id>', methods=['GET'])
def buscar_material(id):
    if id >= len(materiais):
        return 'Not found', 404
    material = {
        "id": id,
        "name": materiais[id],
        "qtde": quantidades[id]
    }
    return jsonify({"material": material}), 200

#Alterar por ID
@app.route('/materials/<int:id>', methods=['PUT'])
def alterar_material(id):
    if id >= len(materiais):
        return 'Not found', 404
    material = request.json.get('material')
    if not material:
        return 'Bad request', 400
    nome_material = material.get('name')
    qtde_material = material.get('qtde')
    if not nome_material or not qtde_material:
        return 'Bad request', 400
    materiais[id] = nome_material
    quantidades[id] = qtde_material
    return 'OK', 200

#Remover por ID
@app.route('/materials/<int:id>', methods=['DELETE'])
def remover_material(id):
    if id >= len(materiais):
        return 'Not found', 404
    materiais.pop(id)
    quantidades.pop(id)
    lista_materiais = []
    for i, material in enumerate(materiais):
        lista_materiais.append({
            "id": i,
            "name": material,
            "qtde": quantidades[i]
        })
    return jsonify(lista_materiais), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
