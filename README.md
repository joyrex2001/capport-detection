# CAPPORT API proof of concept

This is a proof of concept implementation of a capport api based on the draft
specification [draft-donnelly-capport-detection](https://datatracker.ietf.org/doc/draft-donnelly-capport-detection/). Note that this is not an
exact implementation of this draft, but actually implements the [comments](https://www.ietf.org/mail-archive/web/captive-portals/current/msg00312.html)
that were given on this draft.

# Running the capport

The capport api is written in Python, and uses MySQL/mariadb for the storage of the
sessions. The accompanied docker-compose file will set-up a complete
environment, however the capport-api can also run without it (as long as
redis is available, and the python dependecies are installed as well
```pip install -r capport-api/requirements.txt```).

To start with docker-compose: ```docker-compose up --force-recreate```.

To start without docker-compose: ```cd capport-api; python app.py```

# Accessing the api

The following curl commands will be helpful;

```
curl -H'Accept: application/json' http://localhost:5000/capport
```
```
curl -H'Accept: application/json' http://localhost:5000/capport/sessions -d '{"identity": "1234567890"}'
```
```
curl -H'Accept: application/json' http://localhost:5000/capport/sessions/9d09f746-10c7-11e7-a298-0242ac1b0003
```
```
curl -H'Accept: application/json' -X DELETE http://localhost:5000/capport/sessions/9d09f746-10c7-11e7-a298-0242ac1b0003
```

# References

* https://www.ietf.org/mail-archive/web/captive-portals/current/msg00312.html
* https://datatracker.ietf.org/doc/draft-larose-capport-architecture/
* https://datatracker.ietf.org/doc/draft-donnelly-capport-detection/
