import socket
import datetime

# escaneamento
def scan_porta(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(1)
  try:
    sock.connect((ip, port))
    return True
  except:
    return False
  finally:
    sock.close()
#log
def registrar_log(mensage):
  with open("alertas.log", "a") as log:
    log.write(mensage + "\n")

def main():
  target = input("Digite o IP:")
  portas_scan = [21, 22, 23, 25, 53, 80, 443]
  portas_abertas = []

#loop escanear
  print(f"Escaneando... {target}")
  for port in portas_scan:
    if scan_porta(target, port):
      mesage = f"[{datetime.datetime.now()}] A porta {port} está aberta no endereço IP: {target}" #aqui podemos ver data e hora que a porta foi encontrada
      print(mesage)
      
      #guardar na lista
      portas_abertas.append(port)
      #escrever no log
      registrar_log(mesage)

      #verificar se a porta é crítica ou não
      if port in [22, 23]:
        alerta = f"Há uma porta crítica, aberta em {target}"
        print(alerta)
        registrar_log(alerta)
    else:
      print(f"Porta {port}: Está fechada.")

  if not portas_abertas:
   print("Nenhuma porta aberta foi encontrada")
  else:
   print(f"{len(portas_abertas)} portas abertas: {portas_abertas}")

if __name__ == "__main__":
  main()