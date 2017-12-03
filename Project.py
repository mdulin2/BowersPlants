
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
import config

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

        self.add_water_event(48755,2)
        #self.disply_table("P")
        #self.disply_table("U")
        self.disply_table("W")

    def get_plants(self):
        """
        Gets all of the plants
        Returns:
            A list of all the plant id's
        """

        try:
            con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                          database=self.dab) #connection

            rs = con.cursor(cursor_class=MySQLCursorPrepared) #changing the type of cursor
            query = 'SELECT plantID,locationID FROM Plant;' #the query itself
            rs.execute(query) #executing the query
            # create a result set
            plants_list = []
            text = ""
            #iterating through the database
            for (plantID,locationID) in rs:
                text = '{},{}'.format(plantID,locationID)
                plants_list.append(text[0])

            rs.close() #close the cursor
            con.close() #close the connection
            return plants_list
        except mysql.connector.Error as err:
            print("come on! ")

    def disply_table(self, table_start):
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

    def add_plant(self,plantType,locationID,plantName):
        """
        Adds a plant to the database with an auto increment key
        Args:

        """
        #need to check to see if the PlantType is in here

        # create a connection
        con = mysql.connector.connect(user=self.usr,password=self.pwd, host=self.hst,
                                      database=self.dab)

        rs = con.cursor(cursor_class=MySQLCursorPrepared)
        statement = """
        INSERT INTO Plant(locationID,plantName,plantType)
        VALUES(%s,"%s","%s");""" % (locationID,plantName,plantType)
        rs.execute(statement)
        con.commit()
        rs.close()
        con.close()

    def add_water_event(self,userID,plantID):
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
        print "text: ",text
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


if __name__ == '__main__':
    pass
