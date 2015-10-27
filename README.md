### Flask-Starter

This is just a simple working example of a Flask web application. The idea is that you can first verify that 
it works on your machine, then use it as a starting point for your application.

#### Installation

First, clone this repository into the directory of your choice:

    $ cd my/python/projects
    $ git clone git@github.com:ewilson/flask-starter.git

Next, if necessary, install Flask (either globally or into a virtual environment).
(USE `sudo` ONLY IF _NOT_ USING `virtualenv`)

    $ sudo pip install -r requirements.txt

#### Running the application

    $ python flask-starter.py

Now navigate to [localhost:5000](http://localhost:5000/) to verify that it is running locally. On that page there
will be links to the other examples.

Examine `flask-starter.py` and the templates and see if you can understand what is going on.

#### Templates

Notice that the `hello.html`, `bye.html`, and `form.html` templates extend the `base.html` template, when establishes the `title`
and links to `style.css`. Also notice that Flask expects you to use a `templates` folder.

#### Debug mode

You may notice `debug=True` in `flask-starter.py`. You shouldn't have this in production, but it is extremely useful
in development. In particular, it allows for automatic reloading of your application on each save.

