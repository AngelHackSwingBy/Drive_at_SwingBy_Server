from __future__ import print_function
import socket
from contextlib import closing

def main():
  host = '59.106.219.4'
  port = 44344
  bufsize = 4096

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  with closing(sock):
    sock.connect((host, port))
    sock.send(b'1,hogehoge')
    print(sock.recv(bufsize))
  return

if __name__ == '__main__':
  main()