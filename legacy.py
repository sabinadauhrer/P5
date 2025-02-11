
"""
def createDB():
    try:
        Database.call(["python", "Database.py", "createDB()"])
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])

def seedDB():
    try:
        Seed.call(["python", "Seed.py"])
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])

def updateDB():
    try:
        UpdateDB.call(["python", "UpdateDB.py"])
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n"+e.args[0])
    except:
        print("Es ist ein Fehler aufgetreten: ", sys.exc_info()[0])
"""