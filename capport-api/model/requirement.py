class Requirement:

    def __init__(self,uuid,reqtype,url):
        self.uuid = uuid
        self.type = reqtype
        self.url = url
        return

    def getType(self):
        return self.type

    def getUrl(self):
        return self.url

    ## delete will delete the requirement from redis.
    def delete(self):
        return

def newRequirement(uuid,reqtype,url):
    req = Requirement(uuid,reqtype,url)
    return req

def loadRequirement(uuid,reqtype):
    return
