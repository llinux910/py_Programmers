#import animal_mysql
import PRODUCT_CD_mysql
#import online_sale_mysql


#sudo systemctl start mariadb.service


db = PRODUCT_CD_mysql._mariadb("mysql","mysql","localhost",3306,"mysql")

db.connect()

db.createTable("ONLINE_SALE","ONLINE_SALE_ID	INTEGER	FALSE USER_ID	INTEGER	FALSE PRODUCT_ID	INTEGER	FALSE SALES_AMOUNT	INTEGER	FALSE SALES_DATE	DATE	FALSE")
db.insertTable("ONLINE_SALE","1	1	3	2	2022-02-25 2	1	4	1	2022-03-01 4	2	4	2	2022-03-12 3	1	3	3	2022-03-31 5	3	5	1	2022-04-03 6	2	4	1	2022-04-06 2	1	4	2	2022-05-11",4)

#db.createTable("ICECREAM_INFO","FLAVOR	VARCHAR(N)	FALSE INGREDIENT_TYPE	VARCHAR(N)	FALSE")
#db.insertTable("ICECREAM_INFO","chocolate	sugar_based vanilla	sugar_based mint_chocolate	sugar_based caramel	sugar_based white_chocolate	sugar_based peach	fruit_based watermelon	fruit_based mango	fruit_based strawberry	fruit_based melon	fruit_based orange	fruit_based pineapple	fruit_based",1)

db.dropTable("ONLINE_SALE")
#db.dropTable("ICECREAM_INFO")

db.close()