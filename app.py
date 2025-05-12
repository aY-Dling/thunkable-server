from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greeting', methods=['GET'])
def greeting():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # 取 Render 提供的埠口
    app.run(host='0.0.0.0', port=port)
