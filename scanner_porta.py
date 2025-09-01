import socket

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

def main():
  target = input("Digite o IP:")
  portas_scan = [21, 22, 23, 25, 53, 80, 443]

  print(f"Escaneando... {target}")
  for port in portas_scan:
    if scan_porta(target, port):
      print(f"Porta {port}: Está aberta.")
    else:
      print(f"Porta {port}: Está fechada.")

if __name__ == "__main__":
  main()