

import pymysql


def main():
    name = input("name:")
    class_id = input("class_id:")

    conn = pymysql.connect(host="localhost", port=3306, user="root", password="lixuan", database="test")
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    # 自己拼接sql语句，会引起SQL注入
    # uuu' or 1=1 -- 
    # sql = "select * from student where sname='%s' and class_id='%s'" % (name, class_id)
    sql = "select * from student where sname=%s and class_id=%s"

    # 让execute来自动拼接是更好的选择
    row = cursor.execute(sql, [name, class_id])
    # sql = "select * from student where sname=%(u)s and class_id=%(v)s"
    # cursor.execute(sql, {"u": name, "v": class_id})

    ret = cursor.fetchone()
    cursor.close()
    conn.close()
    print(ret)
    print(row)
    if ret:
        print("成功")
    else:
        print("失败")
    

if __name__ == "__main__":
    main()