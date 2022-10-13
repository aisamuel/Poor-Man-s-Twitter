# Poor-Man-s-Twitter

# Introduction

The goal of this project is to provide minimalist twitter application using Vue js and Django Rest Framework

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/aisamuel/Poor-Man-s-Twitter.git \
      --extension=py,md \
      Poor-Man-s-Twitter
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/aisamuel/Poor-Man-s-Twitter.git \
      --extension=py,md \
      Poor-Man-s-Twitter
      
      
After that just install the local dependencies, run migrations, and start the server.


# Poor man's Twitter

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/aisamuel/Poor-Man-s-Twitter.git
    $ cd server
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt   
    
Then simply apply the migrations:

    $ python manage.py makemigrations  

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver