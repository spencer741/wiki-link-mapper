#todo: abstract meesy connection code per func.
#todo: implement db and table checking before manipulation and creation
#todo: implement clean db function.


# import the mysql client for python
import pymysql

#Just hardcoded for now, will implement connection pooler handler if implemented on mass scale

databaseServerIP = "127.0.0.1"  # IP address of the MySQL database server
databaseUserName = "root"       # User name of the database server
databaseUserPassword = "toortoor"   # Password for the database user
newDatabaseName = "WikipediaUrls"  # Name of the database that is to be created
charSet = "utf8mb4"    # Character set
cusrorType = pymysql.cursors.DictCursor


def createdb():
    # Create a connection object
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)

    try:

        # Create a cursor object
        cursorInstance = connectionInstance.cursor()  

        print("\n\n")
        # SQL Statement to create a database
        sqlStatement = "CREATE DATABASE IF NOT EXISTS " + newDatabaseName  

        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute(sqlStatement)
        


        # SQL query string
        sqlQuery = "SHOW DATABASES"

        # Execute the sqlQuery
        cursorInstance.execute(sqlQuery)

        #Fetch all the rows
        databaseList = cursorInstance.fetchall()
        print("\n\n====================")
        for database in databaseList:
            print(database)
        print("=====================\n\n")

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()

def buildTables(root):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,charset=charSet,cursorclass=cusrorType)
    try:

        # Create a cursor object
        cursorInstance = connectionInstance.cursor()  
        #this should be pymysql pyformat to prevent injection...
        sqlStatement = "create table {} (UrlId int not null auto_increment primary key,FullUrl varchar(100),SelfKey int);".format(root) 

        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute("USE WikipediaUrls;")
        cursorInstance.execute(sqlStatement)
    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()



def getURL(rootTopic, key):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)
    try:
        # Create a cursor object
        cursorInstance = connectionInstance.cursor()  
        
        sqlStatement = "SELECT FullUrl FROM {0} WHERE UrlId = {1};".format(rootTopic, key)
        cursorInstance.execute("USE WikipediaUrls;")
        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute(sqlStatement)

        myresult = cursorInstance.fetchone()
        y = dict(myresult)
        return y["FullUrl"]
    except Exception as e:
        print("Exeception occured in getURL:{}".format(e))

    finally:
        connectionInstance.close()
        
    
#get primary key where Full URL equals x

def update(rootTopic, url, selfkey):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)
    try:

        # Create a cursor object
        cursorInstance = connectionInstance.cursor()  
        
        sqlStatement = "INSERT INTO {0} (FullUrl, SelfKey) VALUES ('{1}', {2});".format(rootTopic, url, selfkey)
        #print("This is the sql 1: " + sqlStatement)
        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute("USE WikipediaUrls;")
        cursorInstance.execute(sqlStatement)

        sqlStatement = "SELECT UrlId FROM {0} WHERE FullUrl = '{1}';".format(rootTopic, url)
        #print("This is the sql 2: " + sqlStatement)

        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute("USE WikipediaUrls;")
        cursorInstance.execute(sqlStatement)

        connectionInstance.commit()

        myresult = cursorInstance.fetchone()
        y = dict(myresult)

        #print ("the result: {}".format(y["UrlId"]))
        return y["UrlId"]

    except Exception as e:
        print("Exeception occured in update:{}".format(e))

    finally:
        connectionInstance.close()
        


def deletetable(table_name):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)
    try:
        cursorInstance = connectionInstance.cursor()  
        sqlStatement = "DROP TABLE {};".format(table_name)
        cursorInstance.execute("USE WikipediaUrls;")
        cursorInstance.execute(sqlStatement)
    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()

def isDuplicate(rootTopic, url):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)
    try:
        cursorInstance = connectionInstance.cursor()  
        sqlStatement = "SELECT UrlId from {0} where FullUrl = {1}".format(rootTopic,url)
        cursorInstance.execute("USE WikipediaUrls;")
        cursorInstance.execute(sqlStatement)
        if cursorInstance.fetchone() == None:
            return False
        else:
            return True
    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()
