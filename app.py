from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Nome do usuário é obrigatório'}), 400
    user = {
        'id': len(users) + 1,
        'name': data['name']
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_to_delete = next((user for user in users if user['id'] == user_id), None)
    if not user_to_delete:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    users.remove(user_to_delete)
    return jsonify({'message': 'Usuário deletado com sucesso'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

