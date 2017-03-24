# { " id": { "uuid": "<session_uuid>",
#            "href": "http://<server>/capport/sessions/<session_uuid>" },
#   "identity": "<USERNAME>",
#   "state": { "permitted": false },
#   "requirements": [
#     {"view_page": "http://portal.example.com/welcome/terms_and_conditions.html?session=<session_uuid>"},
#     {"provide_credentials": "http://<server>/capport/sessions/<session_uuid>/credentials"}]
# }

# { " id": { "uuid": "<session_uuid>",
#            "href": "http://<server>/capport/sessions/<session_uuid>" },
#   "identity": "<USERNAME>",
#   "token": "<TOKEN>",
#   "state": { "permitted": true, "expires": "2017-02-25T19:00:00-06:00", "bytes_remaining": 10000000 },
#   "requirements": []
# }

import json
import redis
import uuid

class Session:

    def __init__(self,identity,uuid):
        self.uuid = uuid
        self.identity = identity
        self.requirements = []
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
        token = uuid.uuid1()
        return token

    ## addRequirement will add a requirement to this session.
    def addRequirement(self,requirement):
        self.requirements.append(requirement)
        return

    ## getRequirements will return a list of requirements objects that needs
    ## to be satisfied to gain access to the captive portal.
    def getRequirements(self):
        ## TODO: read from redis...
        return self.requirements

    ## metRequirments will check if all requirements are met, and will return true
    ## or false.
    def metRequirments(self):
        ## TODO: check if reqs > 0
        return

    ## getState will return a State object that describes the current state
    ## of the Session.
    def getState(self):
        ## TODO: determine state
        return

    ## setExpire will set the expire datetime for this session.
    def setExpire():
        ## TODO: set expire date
        return

    ## setDataLimit will set the maximum bytes this session is allowed to consume.
    def setDataLimit(bytes):
        ## TODO: store datalimit
        return

    ## isPermitted will check if access is permitted.
    def isPermitted():
        ## TODO: check expiry and datalimit
        return

    ## store will store the Session object in redis.
    def store(self):
        ## TODO: store in redis
        return

    ## delete will delete the Session object from redis.
    def delete(self):
        ## TODO: delete from redis
        return

## newSession will create a new session based on the given identity. The
## identity would be The USERNAME could be DHCP option-12 value or MAC address
## or t.b.d. It is not that important for security, but useful for diagnostics.
def newSession(identity):
    id = uuid.uuid1()
    session = Session(identity,id)
    return session

## loadSession will load a previously generated session, identified by the uuid.
def loadSession(uuid):
    return
    
