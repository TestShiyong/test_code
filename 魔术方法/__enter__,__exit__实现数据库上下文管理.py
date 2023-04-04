import pymysql


class Db:
    def __init__(self, data_conf):
        self.con = pymysql.connect(**data_conf)
        self.cursor = self.con.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()
        self.cursor.close()


db_conf_data = dict(
    host='rm-uf60nj0t33i3601vx3o.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    password='shi1557225637_',
    database='table_one',
    charset='utf8'
)

sq = "SELECT * FROM `users` WHERE name='shiyong'"
with Db(db_conf_data) as db:
    db.execute(sq)
    print(db.fetchone())
