import pyodbc


def mssql_connect(host,
                  user,
                  passwd,
                  db):
    """
    Create a Microsoft SQL Server database connection and
    cursor.

        Args:
            host (string): server name
            user (string): username
            passwd (string): password
            db (string): the database to connect
    """
    global conn, cursor
    server = host
    database = db
    username = user
    password = passwd
    conn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = conn.cursor()
