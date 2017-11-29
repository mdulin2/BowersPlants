from Project import SQLClient
import mysql.connector
class User:
    """
    The UI of the database
    """
    def __init__(self):
        S = SQLClient()
        S.test()

if __name__ == '__main__': #runs if it's the main function being called
    Y = User()
