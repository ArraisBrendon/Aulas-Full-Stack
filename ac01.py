from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    # Define uma mensagem padrão caso não sejam fornecidas notas na URL
    resultado = 'Entre as notas na URL'

    # Obtém as notas da URL, caso tenham sido fornecidas
    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    # Verifica se as notas foram fornecidas e calcula a média
    if primeira and segunda:
        primeira = float(primeira)
        segunda = float(segunda)
        media = (primeira + segunda) / 2

        # Verifica se a média é suficiente para aprovação, recuperação ou reprovação
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

        # Acrescenta a mensagem da média no resultado final
        resultado += f' (média {media:.1f})'

    # Retorna o resultado final
    return resultado

if __name__ == '__main__':
    app.run(debug=True)