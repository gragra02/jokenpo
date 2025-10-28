# --- Arquivo: app.py ---
# --- Versão correta para o VERCEL ---

import random
from flask import Flask, request, jsonify

# 1. Configuração do Flask
app = Flask(__name__)

# 2. Rota da API (NÃO PODE HAVER OUTRA ROTA)
@app.route('/jogar', methods=['POST'])
def jogar():
    
    # 3a. Tenta pegar a jogada do jogador
    try:
        dados_jogador = request.json
        jogador = int(dados_jogador['escolha'])
    except Exception as e:
        # Se falhar, retorna um erro claro
        return jsonify({'erro': f'Dados inválidos: {e}'}), 400

    # 3b. Definir os itens e sortear a jogada do PC
    itens = ("Pedra", "Papel", "Tesoura")
    computador = random.randint(0, 2)

    # 3c. Determinar o vencedor
    resultado = ""
    if computador == jogador:
        resultado = "Empate!"
    elif (computador == 0 and jogador == 2) or \
         (computador == 1 and jogador == 0) or \
         (computador == 2 and jogador == 1):
        resultado = "Computador Venceu!"
    else:
        resultado = "Você Venceu!"
    
    # 4. Devolver a resposta para o JavaScript
    return jsonify({
        'jogador_jogou': itens[jogador],
        'computador_jogou': itens[computador],
        'resultado_final': resultado
    })

# IMPORTANTE: NÃO PODE HAVER 'app.run()' AQUI