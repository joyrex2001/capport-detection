#   "requirements": [
#     {"view_page": "http://portal.example.com/welcome/terms_and_conditions.html?session=<session_uuid>"},
#     {"provide_credentials": "http://<server>/capport/sessions/<session_uuid>/credentials"}]

class Requirement:

    def __init__(self,uuid,reqtype):
        self.uuid = uuid
        self.type = reqtype
        return

    ## delete will delete the requirement from redis.
    def delete(self):
        return

def newRequirement(uuid,reqtype):
    req = Requirement(uuid,reqtype)
    return req

def loadRequirement(uuid,reqtype):
    return
