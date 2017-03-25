FROM centos:centos7

RUN yum -y install \
            epel-release \
            gcc \
            gcc-c++ \
            python-devel \
            mariadb-devel && \
    yum -y install \
            python-pip

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /app

# Make port 5000 available for links and/or publish
EXPOSE 5000

# Define our command to be run when launching the container
CMD ["python", "app.py"]
