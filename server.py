#socket(udp) sensor data view
# -*- coding: utf-8 -*- 

from __future__ import print_function
import socket
from contextlib import closing

def main():
  host = '59.106.219.4'
  port = 44344
  backlog = 10
  bufsize = 4096

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  with closing(sock):
    sock.bind((host, port))
    sock.listen(backlog)
    while True:
      conn, address = sock.accept()
      with closing(conn):
        msg = conn.recv(bufsize)
        print(msg)
        conn.send(msg)
  return

if __name__ == '__main__':
  main()