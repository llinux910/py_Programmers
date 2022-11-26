    # Get Cursor

    # cur.execute(drop_s)
    # cur.fetchall()

# Module Imports
import mariadb
import sys



class _mariadb:
    def __init__(self,user,password,host,port,database):
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._database = database
        self._conn = None
        self._cur = None

    def connect(self):
        if self._conn==None:
            try:
                self._conn = mariadb.connect(
                user=self._user,
                password=self._password,
                host=self._host,
                port=self._port,
                database=self._database
            )
            except mariadb.Error as e:
                print("x")
                print("Error connecting to MariaDB Platform: {e}")
                sys.exit(1)
            
            self._cur = self._conn.cursor()
            self._conn.autocommit = True

    def close(self):
        try:
            self._cur.close()
            self._conn.close()
        except mariadb.Error as e:
            print("Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
            

    def sendQuery(self,string):
        try:
            self._cur.execute(string)
        except mariadb.Error as e:
            print("Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        
        

    def createTable(self,tableName,stringInfo,Prikey=None):
        string = ""
        value_list=c = stringInfo.split(' ')


        string+="CREATE TABLE "
        string+=tableName
        string+="("
        for v in value_list:
            f = v.split('	')
            for vv in f:
                if vv == "VARCHAR(N)":
                    string+="VARCHAR(255) "
                elif vv == "FALSE":
                    string+="NOT NULL"
                elif vv == "TRUE":
                    string+=''
                elif vv == "INTEGER":
                    string += "INT "
                else:
                    string+=vv+" "
            string+=','




        if Prikey == None:
            if string[len(string)-1] == ",":
                string = string[:-1:]
        else:
            string+="PRIMARY KEY ("+Prikey+")"

        string+=");"

        self.sendQuery(string)

    def dropTable(self,tableName):
        self.sendQuery("drop table "+tableName+";")

    def getClenString(self,originString,problemNumber):

        #originString = "A354597	Cat	2014-05-02 12:16:00	Normal	Ariel	Spayed Female A362707	Dog	2016-01-27 12:27:00	Sick	Girly Girl	Spayed Female A370507	Cat	2014-10-27 14:43:00	Normal	Emily	Spayed Female A414513	Dog	2016-06-07 09:17:00	Normal	Rocky	Neutered Male"
        spltList=originString.split("\t")
        addList = []
        addString = ""
        cnt = 0

        for x in spltList:
            if cnt==problemNumber:
                tmp = x.split(" ")
                if(len(tmp)>2):
                    addString+=tmp[0]+" "+tmp[1]
                    addList.append(addString)
                    addString=tmp[2]+","
                else:
                    addString+=x
                    addList.append(addString)
                cnt = 1
                continue
            addString+=x+","
            cnt+=1
        return addList

    def insertTable(self,TableName,StringInfo,problemNumber):

        dataList = self.getClenString(StringInfo,problemNumber)


        for x in dataList:
            s = "INSERT INTO "+TableName+" VAlUES ("
            t = x.split(",")
            for y in t:
                if y == "NULL":
                    s+=y+","
                else:     
                    s+="'"+y+"'"+","    
            s = s[:-1:]
            s+=");"
            self.sendQuery(s)
        



        

