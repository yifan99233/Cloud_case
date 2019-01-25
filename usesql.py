import SQL
import pymysql
from decimal import *
class select(object):
    def commun(self):
        sql = 'select * from sample_score'
        v = SQL.Sql().Select(sql)
        for i in v:
            print(i)

            # v = len(i) * '{},'
            # print(str(i))
            # h =v[:len(v)-1].format(str(Decimal(i).quantize(Decimal('0.0'))))
            # print(h)
m = select()
m.commun()
