# -*- coding: utf-8 -*- 
from __future__ import print_function
import socket
from contextlib import closing
import MySQLdb

def get_sleepy_user(my_peer_id):
  #connect to DB
  conn = MySQLdb.connect(
    user='root',
    passwd='light',
    host='localhost',
    db='AH'
  )
  c = conn.cursor()

  peer_id = ""
  #get peer_id
  c.execute("select * from user where peer_id <> %s", [my_peer_id])
  for row in c.fetchall():
      peer_id = row[2]

  #commit and close connection
  conn.commit()

  c.close()
  conn.close()

  if(peer_id == ""): peer_id = "no_peer"

  return peer_id

def add_sleepy_user(peer_id):
  #connect to DB
  conn = MySQLdb.connect(
    user='root',
    passwd='light',
    host='localhost',
    db='AH'
  )
  c = conn.cursor()

  #get peer_id
  c.execute("insert into user(peer_id) values(%s)", [peer_id])

  #commit and close connection
  conn.commit()

  c.close()
  conn.close()

def del_sleepy_user(peer_id):
  #connect to DB
  conn = MySQLdb.connect(
    user='root',
    passwd='light',
    host='localhost',
    db='AH'
  )
  c = conn.cursor()

  #get peer_id
  c.execute("delete from user where peer_id = %s", [peer_id])

  #commit and close connection
  conn.commit()

  c.close()
  conn.close()

def add_hobby(username, hobby1, hobby2, hobby3):
  #connect to DB
  conn = MySQLdb.connect(
    user='root',
    passwd='light',
    host='localhost',
    db='AH'
  )
  c = conn.cursor()

  #get peer_id
  c.execute("insert into hobby(username, hobby1, hobby2, hobby3) values(%s, %s, %s, %s)", [username], [hobby1], [hobby2], [hobby3])

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

        #add_hobby(msg[0]:0, msg[1]:username, msg[2-4]:hobby)
        if(int(msg[0])==0):
          add_hobby(msg[1], msg[2], msg[3], msg[4])

        #start_talking(msg[0]:1, msg[1]:peer_id)
        elif(int(msg[0])==1):
          #flag sleepy user
          add_sleepy_user(msg[1])

          #send back other's peer_id
          peer_id = get_sleepy_user(msg[1])
          conn.send(peer_id)

        #end_talking  
        elif(int(msg[0])==2):
          #unflag sleepy user
          del_sleepy_user(msg[1])

if __name__ == '__main__':
  while True:
    main()

