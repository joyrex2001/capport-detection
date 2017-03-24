import model.database

class Requirement:

    def __init__(self,uuid,reqtype,url):
        self.uuid = uuid
        self.type = reqtype
        self.url = url
        return

    ## getType will return the requirement type (view_page, provide_credentials).
    def getType(self):
        return self.type

    ## getUrl will provide the url for the requirement.
    def getUrl(self):
        return self.url

    def store(self):
        cnx = model.database.getCnx()
        cursor = cnx.cursor()
        query = ("INSERT INTO requirement SET uuid=%s,type=%s,url=%s")
        cursor.execute(query,(self.uuid,self.type,self.url))
        cursor.close()
        cnx.commit()
        cnx.close()
        return

    ## delete will delete the requirement from mysql.
    def delete(self):
        cnx = model.database.getCnx()
        cursor = cnx.cursor()
        query = ("DELETE FROM requirement WHERE uuid=%s AND type=%s")
        cursor.execute(query,(self.uuid,self.type))
        cursor.close()
        cnx.commit()
        cnx.close()
        return

## newRequirement will create a new Requirement object.
def newRequirement(uuid,reqtype,url):
    req = Requirement(uuid,reqtype,url)
    return req

## loadRequirement will load the Requirement object from mysql.
def loadRequirement(uuid,reqtype):
    cnx = model.database.getCnx()
    cursor = cnx.cursor()
    query = ("SELECT uuid,type,url FROM requirement WHERE uuid=%s AND type=%s")
    cursor.execute(query, (uuid,reqtype))
    req = None
    for (uuid,reqtype,url) in cursor:
        req = Requirement(uuid,reqtype,url)
    cursor.close()
    cnx.close()
    return req

## loadRequirements will return a list of all the Requirement objects for given uuid.
def getRequirements(uuid):
    cnx = model.database.getCnx()
    cursor = cnx.cursor()
    query = ("SELECT uuid,type,url FROM requirement WHERE uuid=%s")
    cursor.execute(query, (uuid,))
    req = []
    for (uuid,reqtype,url) in cursor:
        req.append(Requirement(uuid,reqtype,url))
    cursor.close()
    cnx.close()
    return req
