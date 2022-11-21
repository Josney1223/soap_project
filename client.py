import zeep

hello_client = zeep.Client('http://localhost:8000/?wsdl')
print(hello_client.service.fazer_pedido("Leonardo", "Combinado 2"))
print(hello_client.service.fazer_pedido("Lorenza", "Barca para 2"))
print(hello_client.service.fazer_pedido("Pedro", "Coca"))
print(hello_client.service.ver_pedidos())
print(hello_client.service.atualiza_pedido(1, "Cancelado"))
print(hello_client.service.atualiza_pedido(5, "Realizado"))
print(hello_client.service.ver_pedidos())