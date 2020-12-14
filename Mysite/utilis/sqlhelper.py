import pymysql



def get_list(sql, args):
    conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    ret = cursor.fetchall()
    cursor.close()
    conn.close()
    return ret


def get_one(sql, args):
    conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    ret = cursor.fetchone()
    cursor.close()
    conn.close()
    return ret


def modify(sql, args):
    conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()




class SqlHelper:
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = pymysql.Connection(host="localhost", port=3306, user="root", password="lixuan", database="test")
        self.cursor = self.conn.cursor(cursor = pymysql.cursors.DictCursor)
    
    def get_list(self, sql, args):
        self.cursor.execute(sql, args)
        ret = self.cursor.fetchall()
        return ret
    
    def get_one(self, sql, args):
        self.cursor.execute(sql, args)
        ret = self.cursor.fetchone()
        return ret
    
    def modify(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def create(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def multiple_modify(self, sql, args):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()