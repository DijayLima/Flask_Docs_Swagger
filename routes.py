from flask_restplus import Resource, Namespace, fields
from flask import request
from funcionario_db import FuncionarioDb

api = Namespace('Funcionario',description='Manutenção dados de Funcionario')
#criação de modelo que será validado ao receber post
modelo = api.model('FuncionarioModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'endereco': fields.String
})

@api.route('/')
class FuncionarioController(Resource):
    @api.response(200, "Busca realizada com sucesso") #documentação para tipo de respostas
    def get(self):
        return FuncionarioDb.obter(), 200
    @api.expect(modelo) #espera modelo ao criar nova Funcionario
    def post(self):
        return FuncionarioDb.adicionar(request.json), 201

@api.route('/<id>')#classe que atende requisições /:id
class FuncionarioIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return FuncionarioDb.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('nome','Nome do Funcionario')#parametros customizados
    @api.param('endereco','Endereço do Funcionario')
    def put(self, id:int):
        return FuncionarioDb.alterar(int(id), request.json), 201

    def delete(self, id:int):
        return FuncionarioDb.remover(int(id)), 200