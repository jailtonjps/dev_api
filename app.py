from flask import Flask, jsonify,request,json

app = Flask(__name__)

desenvolvedores = [
    {'id':'0',
     'nome':'Jailton',
     'habilidade': ['Python', 'Flask']
    },
    {'id':'1',
        'nome':'Miguel',
     'habilidade':['Python', 'Django']
    },
    {'id':'2',
     'nome': 'Michelle',
     'habilidade':['HTML','CSS']
    }
]
# devolve um desenvolvedor pelo ID, tbem altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return  jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluido'})

# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor
@app.route('/dev/',methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','mensagem':'Registro inserido'})


if __name__ == '__main__':
    app.run(debug=True)