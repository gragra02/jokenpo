# --- Arquivo: app.py ---
# --- Versão correta para o VERCEL ---

import random
from flask import Flask, request, jsonify 

app = Flask(__name__)

# --- Esta é a ÚNICA rota que deve existir ---
@app.route('/jogar', methods=['POST'])
def jogar():
    
    try:
        dados_jogador = request.json
        jogador = int(dados_jogador['escolha'])
    except Exception as e:
        return jsonify({'erro': f'Dados inválidos: {e}'}), 400

    itens = ("Pedra", "Papel", "Tesoura")
    computador = random.randint(0, 2)

    resultado = ""
    if computador == jogador:
        resultado = "Empate!"
    elif (computador == 0 and jogador == 2) or \
         (computador == 1 and jogador == 0) or \
         (computador == 2 and jogador == 1):
        resultado = "Computador Venceu!"
    else:
        resultado = "Você Venceu!"
    
    return jsonify({
        'jogador_jogou': itens[jogador],
        'computador_jogou': itens[computador],
        'resultado_final': resultado
    })

# --- NADA MAIS DEVE VIR DEPOIS DAQUI ---