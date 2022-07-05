# Blockchain

### Necessário
- Docker
- Python 3.8+
- MongoDB Compass

Para instalar o ambiente para rodar as aplicações Blockchain e BlockchainClient, instale os pacotes necessários usando o comando do pip.

```bash
pip install -r requirements.txt
```

Depois iremos subir o container da blockchain.

```bash
docker compose up -d
```

O banco está hospedado na nuvem, para ter acesso vá no MongoDB Compass e insira a mongo_uri disponivel no arquivo *extras.txt* que está no email.

Depois você pode rodar a aplicação da _Blockchain primeiro_.
- Nota 1: Você precisa executar com as variáveis de ambiente.
- Nota 2: Recomendo usar o vscode, para executar use a aba de debug do vscode para as envs serem carregadas.

Com a aplicação rodando, acesse a url:

```
http://localhost:8000/docs
```

Para conseguir minerar e fazer as operações bancárias, você precisa criar uma conta. É possivel criar via swagger ou via mensageria.

Depois, para fazer uma transação é precisa ter o número da conta que você vai enviar os tokens e a conta de onde vai sair eles.

As filas criadas no RabbitMQ podem ser visualizadas pela url:

```
http://localhost:15672/#/
```
- User: user
- Password: password

## Filas

- _EVENTS_: Recebe os dados das transações que ficaram salvas no cache e encaminha mensagem para iniciar o POW nos clientes.

- _ELECTIONS_: Recebe a mensagem com quem ganhou o POW, envia mensagem para os outros clientes pararem o seu POW. Envia as informações do novo bloco para o ganhador, solicita aos outros clientes a validação da cadeia de blocos. Por fim, envia as recompensas para as contas.

- _BLOCKS_: Recebe a mensagem para registrar um novo bloco.

- _REGISTER_: Registra o novo cliente ativo.

- _TRANSACTIONS_: Envia transações. *Nota: Informações ficam salvas em cache por um determinado tempo e depois encaminhadas para a fila de ELECTIONS*.

- _ACCOUNT_BALANCE_: Fila que recebe as transações e valida os dados dela.

- _ACCOUNT_REGISTER_: Cria uma nova conta.

- _TOKENS_: Minera os tokens e envia para a conta indicada.

- _VALIDATE_: Encaminha mensagens para os clientes com os blocos para eles validarem a cadeia de blocos.

Os payloads para enviar nas filas estão no arquivo [eventos.txt](eventos.txt)