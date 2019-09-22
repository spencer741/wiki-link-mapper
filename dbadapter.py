#todo: abstract meesy connection code per func.



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

        for database in databaseList:
            print(database)

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()

def buildTables(root):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)
    try:

        # Create a cursor object
        cursorInstance = connectionInstance.cursor()  
        #this should be pymysql pyformat to prevent injection...
        sqlStatement = "use WikipediaUrls;create table computer (UrlId int(50) not null auto_increment primary key,FullUrl varchar(50),SelfKey int(50));" 

        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute(sqlStatement)
    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()

def deletetable(table_name):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)
    try:
        # Create a cursor object
        cursorInstance = connectionInstance.cursor()  

        sqlStatement = "DROP TABLE %s;"

        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute(sqlStatement, (table_name))
    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()

def getURL(rootTopic, Key):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)
    try:
        # Create a cursor object
        cursorInstance = connectionInstance.cursor()  

        sqlStatement = "SELECT FullUrl FROM %s WHERE UrlId = %s;"

        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute(sqlStatement, (rootTopic, key))

        myresult = cursorInstance.fetchall()

        return myresult
    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()
        
    
#get primary key where Full URL equals x

def update(rootTopic, url, selfkey):
    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
    charset=charSet,cursorclass=cusrorType)
    try:

        # Create a cursor object
        cursorInstance = connectionInstance.cursor()  

        sqlStatement = "INSERT INTO %s (FullUrl, SelfKey) VALUES (%s, %s);"

        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute(sqlStatement, (rootTopic, url, selfkey))

        sqlStatement = "SELECT UrlId FROM %s WHERE FullUrl = %s;"

        # Execute the create database SQL statment through the cursor instance
        cursorInstance.execute(sqlStatement, (rootTopic, url))

        myresult = cursorInstance.fetchall()

        return myresult

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connectionInstance.close()
        
