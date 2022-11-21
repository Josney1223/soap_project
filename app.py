import logging

from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from src.database_manager import *

logging.basicConfig(level=logging.DEBUG)
create_database()

class HelloWorldService(ServiceBase):            
    
    @rpc(Unicode, Unicode, _returns=Iterable(Unicode))
    def fazer_pedido(ctx, cliente, pedido):
        yield insert_order(cliente, pedido)
    
    @rpc(_returns=Iterable(Unicode))
    def ver_pedidos(ctx):
        lista: list = read_order()
        count: int = 0

        for i in lista:
            count += 1
            yield "Pedido {}: {}".format(count, i)

    @rpc(Integer, Unicode, _returns=Iterable(Unicode))
    def atualiza_pedido(ctx, index, status): 
        yield update_order(index, status)


application = Application([HelloWorldService],
    tns='spyne.pedidos.crud',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()