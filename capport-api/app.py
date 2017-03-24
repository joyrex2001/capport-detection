from flask import Flask, request, json, jsonify, redirect, render_template
import os

import model.session
import model.requirement

app = Flask(__name__)

####################
## helper methods ##
####################

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

####################
## captive portal ##
####################

@app.route('/')
def index():
    return app.send_static_file('index.html')

# terms page; check for if terms were accepted and delete requirement.
@app.route('/terms')
def terms():
    session_uuid = request.GET['session']
    if (session_uuid is None):
        return app.send_static_file('invalid.html')

    ## load the session with given session id
    session = model.session.loadSession(session_uuid)
    if (session is None):
        return app.send_static_file('invalid.html')

    ## check if terms
    accept = request.GET['accept']
    if (session is None):
        return app.send_static_file('terms.html')

    ## TODO: delete requirement
    ## TODO: check if all requirements are met; -> signal pcef?

    return app.send_static_file('accepted.html')

# login page; check for if password was given and delete requirement.
@app.route('/<session_uuid>/login')
def login():
    passwd = request.POST['password']
    if (passwd is None):
        return app.send_static_file('login.html')

    ## TODO: delete requirement
    ## TODO: check if all requirements are met; -> signal pcef?

    return app.send_static_file('welcome.html')

##############
## REST API ##
##############

# GET from the DHCP-provided URL:
# GET http://<server>/capport (Accept: application/json)
# 200 OK
@app.route('/capport', methods = ['GET'] )
def capport():
    ## get the create and browse urls from env, default to something fancy...
    create = os.getenv( "CAPPORT_CREATE_SESSION_URL",
                        request.url_root+"capport/sessions")
    browse = os.getenv( "CAPPORT_BROWSE_URL",
                        "http://portal.example.com/" )

    ## in case of json, return the urls
    if request_wants_json():
        return (json.dumps({ "create_href": create,
                             "browse_href": browse }),200)

    ## if request doesn't accept json; redirect to browse url
    return redirect(browse, code=307)

# Posting to the create_href:
# POST http://<server>/capport/sessions (Accept: application/json)
# { "identity": "<USERNAME>"}
# 200 OK
@app.route('/capport/sessions',methods = ['POST'] )
def post_sessions():
    ## get post data
    json_request = request.get_json(force=True)
    if (json_request is None):
        return (json.dumps({ "error": "invalid json payload" }), 500)

    ## get identity from
    if not ('identity' in json_request):
        return (json.dumps({ "error": "identity missing" }), 500)

    ## create a new session for this identity
    session = model.session.newSession(json_request['identity'])
    if (session is None):
        return (json.dumps({ "error": "could not inititate session" }), 500)

    ## add some requirements

    req1 = model.requirement.newRequirement(session.getId(),"view_page")
    req2 = model.requirement.newRequirement(session.getId(),"provide_credentials")

    session.addRequirement(req1)
    session.addRequirement(req2)

    ## TODO: return session status

    return ("", 204)

# The session now exists, and GET works:
# GET http://<server>/capport/sessions/<session_uuid> (Accept: application/json)
# 200 OK
@app.route('/capport/sessions/<session_uuid>',methods = ['GET'] )
def get_sessions(session_uuid):
    ## session status as html not implemented in this example
    if not request_wants_json():
        return app.send_static_file('htdocs/index.html')

    ## load the session with given session id
    session = model.session.loadSession(session_uuid)
    if (session is None):
        return (json.dumps({ "error": "invalid session" }), 500)

    ## TODO: return session status

    return ("", 204)

# When the client wants to explicitly leave the network, delete the href for the session:
# DELETE http://<server>/capport/sessions/<session_uuid>
# 200 OK
@app.route('/capport/sessions/<session_uuid>',methods = ['DELETE'] )
def delete_sessions(session_uuid):
    ## load the session with given session id
    session = model.session.loadSession(session_uuid)
    if (session is None):
        return (json.dumps({ "error": "invalid session" }), 500)

    ## delete the session
    session.delete()

    ## return status 204 "no content" instead of 200 "ok"
    return ("", 204)

##################
## let's do it! ##
##################

if __name__ == "__main__":
    app.run(host="0.0.0.0")
