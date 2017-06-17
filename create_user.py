# coding: utf-8

import MySQLdb

def main():
    #connect to DB
    conn = MySQLdb.connect(
        user='root',
        passwd='light',
        host='localhost',
        db='AH'
    )
    c = conn.cursor()

    #add record
    c.execute("insert into user(peer_id) values ('hogehoge')")

    #commit and close connection
    conn.commit()

    c.close()
    conn.close()

if __name__ == '__main__':
    main()