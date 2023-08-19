import mysql.connector
from rich import print as printc
from rich.console import Console
console = Console()

def dbconfig():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="password" # Your Password
        )
    except Exception as e:
        console.print_exception(show_locals=True)
    
    return mydb
