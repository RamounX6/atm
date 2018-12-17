#                                   ====================================
#                                   =         Documentation            =
#                                   ====================================
#
#                                         //////////////////////
#                                         //    Method Guide  //
#                                         //////////////////////
#
#   login_check()                   -----> Check if ID and PIN Exist (Return 0 or 1 )
#   balance_check()                 -----> Check balance (Return balance)
#   add_balance(balance)            -----> Add Balance
#   id_check()                      -----> Check if ID Exist (Return 0 or 1)
#   insert_user(balance)            -----> Insert user ID / PIN / Balance


import MySQLdb

# =======================================[  Connect TO DataBase ]=======================================================
# MYSQL INFO
host_name = "127.0.0.1"
user_name = "user"
password = "123456"
db_name = "info"

# Open DataBase connection
db = MySQLdb.connect(host_name, user_name, password, db_name)

# prepare a cursor object using cursor() method
cursor = db.cursor()


class DBOperation:
    # __init__ build in function
    def __init__(self, card1d, pin=0):
        self.id = card1d    # user ID
        self.pin = pin  # user PIN

# ============================================[  Login Check Method  ]==================================================
    # Function To Check ID
    def login_check(self):
        # Count ID in DB
        sql = "SELECT COUNT(1) FROM est WHERE ID = %s and PIN = %s" % (self.id, self.pin)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data"
        # Change tuple To int
        check = int(results[0][0])
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return check

# ============================================[  Balance Check Method  ]================================================
    # Function To Check ID
    def balance_check(self):
        # Count ID in DB
        sql = "SELECT balance FROM est WHERE ID = %s" % self.id
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Ferch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data"
        # Change tuple To int
        balance = int(results[0][0])
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return balance

# ============================================[ Update Method ]=========================================================
    # Function To Update User
    def add_balance(self, balance):
        # Insert New User
        sql = "UPDATE est  SET balance = %s WHERE ID = %s " %(balance, self.id)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

# ============================================[ ID Check Method ]=======================================================
    # Function To Check ID
    def id_check(self):
        # Count ID in DB
        sql = "SELECT COUNT(1) FROM est WHERE ID = %s" % self.id
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print "Error : Cant Fetch Data"
        # Change tuple To int
        check = int(results[0][0])
        # Check = 0 if ID is not Exist // Check = 1 if ID is Exist
        return check

# ============================================[ Insert Method ]=========================================================
    # Function To Insert User
    def insert_user(self, balance):
        # Insert New User
        sql = "INSERT INTO est (ID, PIN ,balance ) VALUES (%s, %s, %s)" %(self.id, self.pin, balance)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()


# ======================================================================================================================
# Disconnect from server
db.close()
