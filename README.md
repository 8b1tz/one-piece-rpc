# Luffy and Sanji - RPC Example

Este é um exemplo de implementação simples de **RPC** usando **XML-RPC**, onde **Luffy** (cliente) faz um pedido de comida para **Sanji** (servidor) através do **Den Den Mushi** (rede/internet). O projeto é organizado em pastas para facilitar a manutenção e entendimento.

## Como Funciona

- **Sanji** (servidor) está disponível para receber pedidos de comida e preparar o que for solicitado.
- **Luffy** (cliente) faz o pedido de comida utilizando o **Den Den Mushi** (internet), e Sanji responde com a confirmação de que a comida está pronta.

## Instruções para Execução

### 1. Executar o Servidor (Sanji)
No diretório `/server`, execute o seguinte comando para iniciar o servidor:

```bash
python sanji.py
```

O servidor estará pronto para receber pedidos na porta 8000.

### 2. Executar o Cliente (Luffy)
No diretório /client, execute o seguinte comando para fazer um pedido de comida:

```bash
python luffy.py
```

O cliente enviará o pedido de comida para o servidor, e você verá a resposta de Sanji no console.

## Dependências
Este projeto não requer bibliotecas externas, pois utiliza a biblioteca xmlrpc que já vem incluída no Python. Certifique-se de ter o Python 3.x instalado.