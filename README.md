# soap_project

Projeto utilizando o SOAP

# Grupo

Kahao Yu

Leonardo Lopes Lessa da Fonseca

Lorenza Oliva Fracasso

Pedro Pieragnoli Marin

# Roteiro da Ativdade Prática

# Pré-Requisitos

Ter instalado no dispositivo o interpretador Python 3.x.

Saiba mais em https://www.python.org/

# Instalação

Usar o comando abaixo no diretório para intalar as dependências:

```sh
pip install -r dependencies.txt
```

# Recursos

- `hello_client.service.fazer_pedido(nome, pedido)` - efetua um pedido
- hello_client.service.`ver_pedidos()` - imprime os pedidos
- `hello_client.service.atualiza_pedido(pedido, status)` - altera um pedido

# Utilização

- Abrir dois terminais distindos na raiz do projeto
- Para inicializar o servidor use o comando:
 
```sh
  python app.py
```

- Para inicializar o cliente use o comando:

```sh
  python client.py`
```

- Verificar as log's

# Funcionamento

O projeto consiste em um CRUD básico para um sistema de pedidos de um restaurante, ao iniciar a aplicação irá

- Criar uma instância do servidor em `localhost`
- O cliente irá efetuar 4 pedidos, onde os dados serão armazenados em um banco de dados estilo `.xlsx`
- Os pedidos serão impressos no terminal
- Ocorrer dois eventos de atualização, sendo um deles um `cancelamento` e o outro uma `realização`
- Os pedidos serão impressos no terminal
