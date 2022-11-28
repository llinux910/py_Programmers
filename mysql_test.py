#import animal_mysql
import PRODUCT_CD_mysql
#import online_sale_mysql



db = PRODUCT_CD_mysql._mariadb("mysql","mysql","localhost",3306,"mysql")

db.connect()

db.createTable("FIRST_HALF","SHIPMENT_ID	INT(N)	FALSE FLAVOR	VARCHAR(N)	FALSE TOTAL_ORDER	INT(N)	FALSE")
db.insertTable("FIRST_HALF","101	chocolate	3200 102	vanilla	2800 103	mint_chocolate	1700 104	caramel	2600 105	white_chocolate	3100 106	peach	2450 107	watermelon	2150 108	mango	2900 109	strawberry	3100 110	melon	3150 111	orange	2900 112	pineapple	2900",2)

db.createTable("ICECREAM_INFO","FLAVOR	VARCHAR(N)	FALSE INGREDIENT_TYPE	VARCHAR(N)	FALSE")
db.insertTable("ICECREAM_INFO","chocolate	sugar_based vanilla	sugar_based mint_chocolate	sugar_based caramel	sugar_based white_chocolate	sugar_based peach	fruit_based watermelon	fruit_based mango	fruit_based strawberry	fruit_based melon	fruit_based orange	fruit_based pineapple	fruit_based",1)

db.dropTable("FIRST_HALF")
db.dropTable("ICECREAM_INFO")

db.close()