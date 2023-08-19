import random
import string
import sys
import hashlib
from getpass import getpass

from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console
console = Console()

def generateDeviceSecret(length= 10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))


def config():
    db = dbconfig()
    cursor = db.cursor()

    printc("[green][+] Creating new config [/green]")

    try:
        cursor.execute("CREATE DATABASE pm")
    except Exception as e:
        printc("[red][!] An error occurred while trying to create db.")
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Database 'pm' created")
    
    #Creating table for storing hastable of the master password
    query = "CREATE TABLE pm.secret (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT  NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'secret' created")

    #Creating table for storing email, username and password
    query = "CREATE TABLE pm.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created")

    while 1:
        mp = getpass("Choose a MASTER PASSWORD: ")
        if mp == getpass("Re-type: ") and mp != "":
            break
        printc("[yellow][-] Please try again. [/yellow]")
    
    #Hashing the MASTER PASSWORD
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of MASTER PASSWORD")

    #Generating DEVICE SECRET
    df = generateDeviceSecret()
    printc("[green][+][/green] Generated DEVICE SECRET ")

    #Adding the hashed MASTER PASSWORD and DEVICE SECRET key to the pm.secret table
    query = "INSERT INTO pm.secret (masterkey_hash, device_secret) values (%s, %s)"
    values = (hashed_mp, df)
    cursor.execute(query, values)
    db.commit()

    printc("[green][+][/green] Added to the database")
    printc("[green][+] Configuration done! [/green]")

    db.close()

config()


    