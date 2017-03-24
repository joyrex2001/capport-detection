import json
import redis
import uuid
import time

class Session:

    def __init__(self,identity,uuid):
        self.uuid = uuid
        self.identity = identity
        self.requirements = []
        self.expire = 0
        self.datalimit = 0
        return

    ## getId will return the uuid of this session.
    def getId(self):
        return self.uuid

    ## getIdentity will return the identity for this session.
    def getIdentity(self):
        return self.identity

    ## getToken will return a generated token to allow re-login, based on this
    ## token. This requires further detail design.
    def getToken(self):
        token = str(uuid.uuid1())
        return token

    ## addRequirement will add a requirement to this session.
    def addRequirement(self,requirement):
        self.requirements.append(requirement)
        return

    ## getRequirements will return a list of requirements objects that needs
    ## to be satisfied to gain access to the captive portal.
    def getRequirements(self):
        return self.requirements

    ## metRequirments will check if all requirements are met, and will return true
    ## or false.
    def metRequirements(self):
        if (len(self.getRequirements())>0):
            return None
        return True

    ## setExpire will set the expire datetime for this session to the given epoch.
    def getExpire(self):
        return self.expire

    ## setExpire will set the expire datetime for this session to the given epoch.
    def setExpire(self,t):
        self.expire = t
        return

    ## isExpired will check if the session is expired.
    def isExpired(self):
        if (self.expire > 0) and (time.time() > self.expire):
            return True
        return None

    ## setDataLimit will set the maximum bytes this session is allowed to consume.
    def setDataLimit(self,limit):
        self.datalimit = limit
        return

    ## getDataLimit will return the maximum bytes this session is allowed to consume.
    def getDataLimit(self):
        return self.datalimit

    ## isDepleated will check if the datalimit has been crossed given current usage.
    def isDepleated(self,usage):
        if (self.datalimit > 0) and (current > self.datalimit):
            return True
        return None

    ## isPermitted will check if access is permitted given current usage in bytes.
    def isPermitted(self,usage):
        if (self.metRequirements() is None):
            return None
        if (self.isExpired() is True):
            return None
        if (self.isDepleated(usage) is True):
            return None
        return True

    ## store will store the Session object in redis.
    def store(self):
        ## TODO: store in redis
        # serialize, including requirements
        return

    ## delete will delete the Session object from redis.
    def delete(self):
        ## TODO: delete from redis
        return

## newSession will create a new session based on the given identity. The
## identity would be The USERNAME could be DHCP option-12 value or MAC address
## or t.b.d. It is not that important for security, but useful for diagnostics.
def newSession(identity):
    id = str(uuid.uuid1())
    session = Session(identity,id)
    return session

## loadSession will load a previously generated session, identified by the uuid.
def loadSession(uuid):
    return
