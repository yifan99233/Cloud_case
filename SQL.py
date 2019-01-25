import pymysql
class Sql(object):
    def __init__(self):
        self.db = pymysql.connect(host = "rds11gs3kjhq3aeyr736o.mysql.rds.aliyuncs.com",
                                  user = "cloud_dev",
                                  password = "u4-vsQxQLv_R15Nf",
                                  db = "photo_cloud_dev")
        self.cursor = self.db.cursor()
    def Select(self,sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            m = self.cursor.fetchall()
            kill = []
            for i in m:
                list = []
                [list.append(str(n)) for n in i]
                kill.append(list)
            #n = m[0]
            self.db.close()
        except:
            # 发生错误时回滚
            self.db.rollback()
            print("更新失败")
            self.db.close()
        return kill
    def Update(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()
            print(sql+"SUCCESS")
        except:
            #self.db.rollback()
            self.db.close()
            print('*'*5+sql+"FAIL")
if __name__ == '__main__':
    c = Sql()
