# -*- coding: utf-8 -*- 
from __future__ import print_function
import socket
from contextlib import closing
import MySQLdb

def get_sleepy_user():
  #connect to DB
  conn = MySQLdb.connect(
    user='root',
    passwd='light',
    host='localhost',
    db='AH'
  )
  c = conn.cursor()

  #get peer_id
  c.execute('select * from user where flag = 1')
  for row in c.fetchall():
      peer_id = row[2]

  #commit and close connection
  conn.commit()

  c.close()
  conn.close()

  return peer_id

def flag_sleepy_user(peer_id):
  #connect to DB
  conn = MySQLdb.connect(
    user='root',
    passwd='light',
    host='localhost',
    db='AH'
  )
  c = conn.cursor()

  #get peer_id
  c.execute("update user set flag = 1 where peer_id = %s", [peer_id])

  #commit and close connection
  conn.commit()

  c.close()
  conn.close()

def unflag_sleepy_user(peer_id):
  #connect to DB
  conn = MySQLdb.connect(
    user='root',
    passwd='light',
    host='localhost',
    db='AH'
  )
  c = conn.cursor()

  #get peer_id
  c.execute("update user set flag = 0 where peer_id = %s", [peer_id])

  #commit and close connection
  conn.commit()

  c.close()
  conn.close()

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

        #split received message
        msg = msg.split(',')

        #start_talking(msg[0]:1, msg[1]:peer_id)
        if(int(msg[0])==1):
          #flag sleepy user
          flag_sleepy_user(msg[1])

          #send back other's peer_id
          peer_id = get_sleepy_user()
          conn.send(peer_id)

        #end_talking  
        elif(int(msg[0])==2):
          #unflag sleepy user
          unflag_sleepy_user(msg[1])

if __name__ == '__main__':
  while True:
    main()

