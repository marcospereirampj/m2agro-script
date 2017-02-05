# -*- coding: utf-8 -*-

import psycopg2

conn = psycopg2.connect("dbname=m2agro_db user=marcospereira")
cur = conn.cursor()

cur.execute("create table matrix_m2agro ()")

for i in range(100):
  cur.execute("alter table matrix_m2agro add column col%s varchar(1)" % str(i+1))

for i in range(100):
  cur.execute("insert into matrix_m2agro (col%s, col%s) values ('X','X')" % (str(i+1),str(100-i)))

cur.execute("select * from matrix_m2agro")
rows = cur.fetchall()

for row in rows:
    print(" ".join(map(lambda x: x if x else " ",row)))

conn.commit()
cur.close()
conn.close()
