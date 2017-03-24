# CAPPORT API proof of concept

This is a proof of concept implementation of a capport api based on the draft
specification [draft-donnelly-capport-detection](https://datatracker.ietf.org/doc/draft-donnelly-capport-detection/). Note that this is not an
exact implementation of this draft, but actually implements the [comments](https://www.ietf.org/mail-archive/web/captive-portals/current/msg00312.html)
that were given on this draft.

# Running the capport

The capport api is written in Python, and uses MySQL/mariadb for the storage of the
sessions. The accompanied docker-compose file will set-up a complete
environment, however the capport-api can also run without it.

## Run with docker-compose

To start with docker-compose: ```docker-compose up --force-recreate```.

## Run without docker compose

This proof of concept can also run without docker, but requires some manual installation
of the dependencies.

On centos7, install the following:
```bash
yum -y install epel-release gcc gcc-c++ python-devel mariadb-devel mariadb-server
yum -y install python-pip
pip install -r capport-api/requirements.txt
```

Create the database, and add a default user:
```bash
sudo systemctl start mariadb
sudo mysql
MariaDB [(none)]> CREATE DATABASE capport CHARACTER SET utf8 COLLATE
utf8_unicode_ci;
MariaDB [(none)]> GRANT ALL PRIVILEGES ON capport.* TO 'capport'@'%' IDENTIFIED
BY 'capport';
```

Finally, to start the service:
```cd capport-api; python app.py```.

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
