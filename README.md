App to test if e-mail address is valid, using dig and telnet.

## Pipenv

Pipenv is a virtual enviroment, it makes it easy to record your dependencies.

For more info see: [https://pypi.org/project/pipenv/](https://pypi.org/project/pipenv/)

To install:

```ps
pip install pipenv
```

To install dependencies, in the directory run:

```ps
pipenv install
```

## Dockerfile

You can create a docker image of this using the following commands:

```ps
docker build -t python-emailalive
```

To run:

```ps
docker run -it python-emailalive
```

## What am I using?

- Python 3.10

## TODO

- Reduce the required inputs
- Setup a process to run multiple e-mails
