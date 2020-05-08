import mysql.connector

class MediumDB():
    def __init__(self):
        pass

    def writetodb(self):
        # Config
        config = {
            'user': '',
            'password': '',
            'host': 'localhost',
            'database': 'mediumtutorialdb',
            'port': 3306,
            'raise_on_warnings': True,
        }

        # Connect to DB
        conn = mysql.connector.connect(**config)

        # Create Cursor
        c = conn.cursor()

        # Query
        query = (f"INSERT INTO `mediumtutorialdb`.`mediumtable` (`Name`, `Age`) VALUES ('Darryl See', '21')")

        # Execute
        c.execute(query)

        # Commit
        conn.commit()

        # End Session
        c.close()
        conn.close()
        print('Sent To DB!\n')


x = MediumDB()
x.writetodb()
