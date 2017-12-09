
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
import config
import random as rand

class SQLClient:
    def __init__(self):
        #connection info
        self.usr = config.mysql['user']
        self.pwd = config.mysql['password']
        self.hst = config.mysql['host']
        self.dab = 'mdulin2_DB'

    def test(self):
        """
        A function to test the SQL code in
        """
        self.display_table("O")
        self.add_user(1,"Van N.",3605080789)
        self.add_ownership(1,4)
        self.users_without_plants()
        self.users_with_most_plants()

    def display_table(self, table_start):
        """
        Displays the table
        Args:
            table_start: The table to be displayed; there are five possible options...
            O-PlantOwnership
            W-WaterEvent
            U-Users
            L-Location
            T-PlantType
        """

        # create a connection
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        if(table_start == 'O'):
            table = "PlantOwnership"
        elif(table_start == 'W'):
            table = "WaterEvent"
        elif(table_start == 'U'):
            table = "Users"
        elif(table_start == "L"):
            table = "Location"
        elif(table_start == "T"):
            table = "PlantType"
        elif(table_start == "P"):
            table = 'Plant'
        else:
            assert(False)

        statement = 'SELECT * FROM %s' % (table) # %s is the placeholder, table is the variable
        #might want to turn this into a prepared statement?
        rs.execute(statement)

        for pull in rs:
            print pull #displays in element in the database pull
        rs.close()
        con.close()

    def add_plant(self,plantType,building,area,plantName):
        """
        Adds a plant to the database with an auto increment key
        Args:
            plantType: the breed of plant
            building: the building in which the plant is located
            area: the place where the plant is at inside of the building
            plantName: the name of the plant being added
        """
        statement = """
        SELECT *
        FROM PlantType
        WHERE name = "%s";""" %(plantType)
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        thirst = input("What is the thirst level of the plant?\n")
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        #makes sure the plantType exists. If not, it adds it.
        if(self.check(statement)== True):

            statement = """
            INSERT INTO PlantType(name,thirst)
            VALUES("%s",%s);""" % (plantType,thirst)
            rs.execute(statement)

        #gets the locationID
        statement = """
        SELECT locationID
        FROM Location
        WHERE building = "%s" AND area = "%s";""" %(building,area)
        self.add_location(building,area)
        rs.execute(statement)
        parse_location = ""
        for (val) in rs:
            text = '{}'.format(val)
            for char in text:
                if(char.isdigit()):
                    parse_location += char
            print parse_location

        #gets the plantType ID
        statement = """
        SELECT ID
        FROM PlantType
        WHERE name = "%s" AND thirst = %s;""" %(plantType,thirst)
        rs.execute(statement)
        parse_type = ""
        for (val) in rs:
            text = '{}'.format(val)
            for char in text:
                if(char.isdigit()):
                    parse_type += char
            print parse_type

        statement = """
        INSERT INTO Plant(locationID,plantName,plantType)
        VALUES(%s,"%s","%s");""" % (parse_location,plantName,parse_type)
        rs.execute(statement)
        con.commit()
        rs.close()
        con.close()

    def add_ownership(self,userID,plantID):
        """

        """
        # create a connection
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        #checks to see if the plant type is already in the database
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        statement = """
        SELECT *
        FROM Plant
        WHERE plantID = %s;""" %(plantID)
        if(self.check(statement)== True):
            print("plant not in database")
            return
        #checks to make sure the user is in the database
        statement = """
        SELECT *
        FROM Users
        WHERE userID = %s;""" %(userID)
        if(self.check(statement)== True):
            print "user not in database"
            return
        #checks to make sure that the plant is in the database
        statement = """
        SELECT * FROM PlantOwnership
        WHERE userID = %s AND plantID = %s """ %(userID,plantID)
        if(self.check(statement) == False):
            print "The relationship already exists!"
            return
        #inserts the plant
        statement = """
        INSERT INTO PlantOwnership(userID,plantID) VALUES(%s,%s) """ %(userID,plantID)
        rs.execute(statement)
        con.commit()
        rs.close()
        con.close()

    def add_water_event(self,userID,plantID):
        """

        """
        # create a connection
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        #checks to see if the plant type is already in the database
        rs = con.cursor(cursor_class=MySQLCursorPrepared)

        #checks to see if a plant is in the database
        statement = """
        SELECT *
        FROM Plant
        WHERE plantID = %s;""" %(plantID)
        if(self.check(statement)== True):
            print("plant not in database")
            return

        statement = """
        SELECT *
        FROM Users
        WHERE userID = %s;""" %(userID)
        if(self.check(statement)== True):
            print "user not in database"
            return


        statement = """
        INSERT INTO WaterEvent(userID,plantID) VALUES("%s",%s) """ %(userID,plantID)
        rs.execute(statement)
        con.commit()
        rs.close()
        con.close()

    def add_plant_type(self,name,thirst):

        # create a connection
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        #checks to see if the plant type is already in the database
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        statement = """
        SELECT *
        FROM PlantType T
        WHERE T.name = "%s"
        and T.thirst = %s; """ %(name,thirst)
        rs.execute(statement)
        if(self.check(statement)== False):
            return

        statement = """
        INSERT INTO PlantType(name,thirst) VALUES("%s",%s) """ %(name,thirst)
        rs.execute(statement)
        con.commit()
        rs.close()
        con.close()

    def check(self,query):
        """
        Checks to see if a set of values is already in the database
        Args:
            query: The query that is being tested
        Returns:
            True if the value is not in table, false otherwise
        """
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        #checks to see if the plant type is already in the database
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        rs.execute(query)
        text = None
        for (val) in rs:
            text = '{}'.format(val)

        if(text == None):
            return True
        else:
            return False

    def add_location(self,building,area):
        """
        Adds a location to the database
        Args:
            building: the building where the plant is located
            area: the part of the building that the plant is stored at.
        """

        statement = """
        SELECT *
        FROM Location L
        WHERE L.building = "%s"
        and L.area = "%s"; """ %(building,area)
        if(self.check(statement) == False):
            return

        # create a connection
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        #checks to see if the plant type is already in the database
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        statement = """
        INSERT INTO Location(building,area) VALUES("%s",%s) """ %(building,area)
        rs.execute(statement)
        con.commit()
        rs.close()
        con.close()

    def add_user(self,userID,name,phone_number,role = "User"):
        """
        Adds a single user to the database
        Args:
            userID(optional): the unique ID of the userID
            name: the Name of the user being inserted
            phone_number: the phone number of the user
            role(optional): the role of the user
        """
        if(self.make_check("userID",userID,"Users",0) == False):
            print("The user is already in the database")
            return
        # create a connection
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)

        rs = con.cursor(cursor_class=MySQLCursorPrepared)

        statement = 'INSERT INTO Users VALUES(%s,"%s","%s","%s");' % (userID,name,phone_number,role)
        rs.execute(statement)
        con.commit()
        rs.close()
        con.close()

    def make_check(self,name,value,table,value_or_string):

        """
        Checks to see if the given value is a key in table already
        Args:
            name: table attribute to Checks
            value: the value being checked
            table: the table being viewed
            value_or_string: 0 if just a value, 1 if a string is needed for it
        Returns:
            True if value is not in the table, false otherwise
        """

        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        if(value_or_string == 0):
            statement = 'SELECT %s FROM %s WHERE %s = %s;' % (name,table,name,value)
        else:
            statement = 'SELECT %s FROM %s WHERE %s = "%s";' % (name,table,name,value)
        print (statement)
        rs.execute(statement)

        text = None
        for (val) in rs:
            text = '{}'.format(val)
        if(text == None):
            return True
        else:
            return False

    def remove(self, table, ID,name):
        """
        Removes an entry from the database
        Args:
            table: the table to delete from
            ID: the id of the value we need to delete
            name: name of the attribute to test on
        """
        statement = """
        DELETE FROM %s
        WHERE %s = %s """ %(table,name,ID)
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        rs.execute(statement)
        con.commit()
        rs.close()
        con.close()

    def parse_val(self, string):
        print string
        for char in string:
            print char

    def remove_plant(self, plantID):
        """
        Removes the plant from the database
        Args:
            plantID: the plant ID
        """
        if(self.check("SELECT * FROM Plant WHERE plantID = %s" % plantID) == False):
            self.remove("Plant",plantID,"plantID")

    def remove_user(self, userID):
        """
        Removes a user from the database
        Args:
            userID: the user to be removed
        """
        if(self.check("SELECT * FROM Users WHERE userID = %s" % userID) == False):
            self.remove("Users",userID, "userID")
            return
        print "The User was not in the database"

    def plants_without_users(self):
        """
        Gets all of the plants without Users
        """
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        statement = """
        SELECT P.plantID
        FROM Plant P LEFT OUTER JOIN PlantOwnership O on P.plantID = O.plantID
        WHERE O.userID IS NULL;
        """

        rs.execute(statement)
        for pull in rs:
            print pull
        rs.close()
        con.close()
    def users_without_plants(self):
        """
        Gets all the users without plants
        """
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        statement = """
        SELECT U.userID
        FROM Users U LEFT OUTER JOIN PlantOwnership O on U.userID = O.userID
        WHERE O.plantID IS NULL; """
        rs.execute(statement)
        for pull in rs:
            print pull
        rs.close()
        con.close()

    def users_with_most_plants(self):
        """
        Gets all the users without plants
        """
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)
        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        statement = """
        SELECT O.userID
        FROM PlantOwnership O
        GROUP BY O.userID
        HAVING COUNT(*) >= ALL(SELECT COUNT(*)
                               FROM PlantOwnership O
                               GROUP BY O.userID)
        """

        print "users with most plants"
        rs.execute(statement)
        for pull in rs:
            print pull
        rs.close()
        con.close()

if __name__ == '__main__':
    pass
