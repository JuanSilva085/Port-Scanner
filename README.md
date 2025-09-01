# Port Scanner em Python

## Descrição

Este projeto implementa um port scanner simples em Python utilizando a biblioteca padrão socket.
O objetivo é demonstrar conceitos básicos de redes e segurança da informação, permitindo identificar se determinadas portas em um host estão abertas ou fechadas.


## Funcionalidades

Escaneamento de portas TCP específicas.

Retorno indica se a porta está aberta ou fechada.

Configuração simples, sem dependências externas.



## Detalhes técnicos – Import socket

Neste projeto, foi usado a biblioteca padrão socket, que fornece acesso ao sistema de sockets BSD para comunicação via TCP/IP. Os principais componentes empregados incluem:

socket.socket(socket.AF_INET, socket.SOCK_STREAM): cria um socket do tipo cliente TCP (IPv4).

settimeout(1): evita bloqueios prolongados ao tentar conexão com portas fechadas.

connect((ip, port)): tenta estabelecer uma conexão.

close(): encerra e libera os recursos do socket.

## Referência / Documentação

Módulo socket (Python): Fornece acesso à interface de soquete BSD. https://docs.python.org/3/library/socket.html