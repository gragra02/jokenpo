# --- Arquivo: app.py ---
# --- VERSÃO HÍBRIDA (TESTE LOCAL + VERCEL) ---

import random
# Importa as funções extras para o teste local
from flask import Flask, request, jsonify, send_from_directory 

app = Flask(__name__)

# # --- Bloco 1 (PARA TESTE LOCAL) ---
# # Esta rota serve o index.html na página principal
# @app.route('/')
# def index():
#     return send_from_directory('.', 'index.html')


# --- Bloco 2 (PARA O VERCEL E TESTE LOCAL) ---
# Esta é a sua API, a "cozinha" do jogo
@app.route('/jogar', methods=['POST'])
def jogar():
    
    # Tenta pegar a jogada do jogador
    try:
        dados_jogador = request.json
        jogador = int(dados_jogador['escolha'])
    except Exception as e:
        return jsonify({'erro': f'Dados inválidos: {e}'}), 400

    # Definir os itens e sortear a jogada do PC
    itens = ("Pedra", "Papel", "Tesoura")
    computador = random.randint(0, 2)

    # Determinar o vencedor
    resultado = ""
    if computador == jogador:
        resultado = "Empate!"
    elif (computador == 0 and jogador == 2) or \
         (computador == 1 and jogador == 0) or \
         (computador == 2 and jogador == 1):
        resultado = "Computador Venceu!"
    else:
        resultado = "Você Venceu!"
    
    # Devolver a resposta para o JavaScript
    return jsonify({
        'jogador_jogou': itens[jogador],
        'computador_jogou': itens[computador],
        'resultado_final': resultado
    })


# # --- Bloco 3 (PARA TESTE LOCAL) ---
# # Esta linha "liga" o servidor no seu PC
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)