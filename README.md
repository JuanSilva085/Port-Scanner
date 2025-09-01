# Port Scanner em Python

## Descrição

Este projeto implementa um port scanner simples em Python utilizando a biblioteca padrão socket.
O objetivo é demonstrar conceitos básicos de redes e segurança da informação, permitindo identificar se determinadas portas em um host estão abertas ou fechadas. Também foi adicionado o registro de logse alertas para portas críticas(alertas.log). 


## Funcionalidades

Escaneamento de portas TCP específicas.

Retorno indica se a porta está aberta ou fechada.

Alertas para portas críticas (alertas.log).

<img width="293" height="203" alt="img-scanner" src="https://github.com/user-attachments/assets/aa5ad733-10d6-425f-822f-9d5cf740df7c" />


## Detalhes técnicos – Import socket

Neste projeto, foi usado a biblioteca padrão socket, que fornece acesso ao sistema de sockets BSD para comunicação via TCP/IP. Os principais componentes empregados incluem:

socket.socket(socket.AF_INET, socket.SOCK_STREAM): cria um socket do tipo cliente TCP (IPv4).

settimeout(1): evita bloqueios prolongados ao tentar conexão com portas fechadas.

connect((ip, port)): tenta estabelecer uma conexão.

close(): encerra e libera os recursos do socket.

## Arquivo log

Os registros incluem a data e hora.

Portas críticas abertas geram alertas no alertas.log.


## Referência / Documentação

Módulo socket (Python): Fornece acesso à interface de soquete BSD. 

socket: https://docs.python.org/3/library/socket.html
datetime: https://docs.python.org/3/library/datetime.html