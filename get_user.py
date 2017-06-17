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

    #get record
    c.execute('select * from user')
    print('===== RECORD =====')
    for row in c.fetchall():
        print('ID:', row[0], 'Flag:', row[1], 'Peer_ID:', row[2])

    #commit and close connection
    conn.commit()

    c.close()
    conn.close()

if __name__ == '__main__':
    main()