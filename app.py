# --- Arquivo: app.py ---

import random
from flask import Flask, render_template, request, jsonify

# 1. Configuração do Flask
app = Flask(__name__)

# 2. Rota Principal (para carregar a página HTML)
@app.route('/')
def index():
    # O Flask procura automaticamente o 'index.html' na pasta 'templates'
    return render_template('index.html')

# 3. Rota da API (para onde o JavaScript vai enviar a jogada)
@app.route('/jogar', methods=['POST'])
def jogar():
    # ---------------------------------------------------
    # A LÓGICA DO SEU JOGO ACONTECE AQUI
    # ---------------------------------------------------
    
    # 3a. Pegar a jogada do jogador que veio do JavaScript
    # O 'request.json' é o "pedido" que o garçom (JS) trouxe
    dados_jogador = request.json
    jogador = int(dados_jogador['escolha']) # Pega o valor 0, 1 ou 2

    # 3b. Definir os itens e sortear a jogada do PC
    itens = ("Pedra", "Papel", "Tesoura")
    computador = random.randint(0, 2)

    # 3c. Determinar o vencedor (corrigi a lógica 'elif' que estava aninhada)
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
    # Usamos 'jsonify' para enviar a resposta de volta ao Frontend
    return jsonify({
        'jogador_jogou': itens[jogador],
        'computador_jogou': itens[computador],
        'resultado_final': resultado
    })
    # ---------------------------------------------------
    # FIM DA LÓGICA DO JOGO
    # ---------------------------------------------------

# 5. Linha para rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)