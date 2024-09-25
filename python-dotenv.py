#https://pypi.org/project/python-dotenv/

# 1 Basic
pip install python-dotenv

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
load_dotenv('.secrets.env')

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

# add .env to directory
# add your .env to .gitignore

# Development settings
DOMAIN=example.org
# If you use variables in values, ensure they are surrounded with { and }, like ${DOMAIN}
ADMIN_EMAIL=admin@${DOMAIN}
ROOT_URL=${DOMAIN}/app

# Read the environment variables
import os
domain_getenv = os.getenv("DOMAIN")
# or
domain_environ = os.environ["DOMAIN"]
#In this case, both lines are used to access the value of the "DOMAIN" environment variable, but the first line returnsNoneif the variable is not found, while the second line raises aKeyErrorif the variable is not present in the environment.

# 2 Commandline 
$ pip install "python-dotenv[cli]"
$ dotenv set MAIN_USER foo
$ dotenv -f .secrets.env set KEY 123456
$ dotenv list
$ dotenv -f .secrets.env list
USER=foo
EMAIL=foo@example.org
$ dotenv list --format=json
{
  "USER": "foo",
  "EMAIL": "foo@example.org"
}
$ dotenv run -- python foo.py
$ dotenv --help

# 3 Dotenv Values
from dotenv import dotenv_values
config = dotenv_values(".env")  
# config = {"DOMAIN": "example.org", "ADMIN_EMAIL": "admin@example.org", "ROOT_URL": "example.org/app"}

# 4 This notably enables advanced configuration management
config = {
    **dotenv_values(".env.shared"),  # load shared development variables
    **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

# 5 Parse configuration as a stream
# Load from other sources then Filesystem
from io import StringIO
config = StringIO("USER=foo\nEMAIL=foo@example.org")
config = "environment varaibles from your backend"
load_dotenv(stream=config)


# Override
# it looks in both, the env file and the environment, if the variable exists in both directions
load_dotenv(override=True)
# prefers the env

load_dotenv(override=False)
# prefers the environment

# Load .env files in IPython
%load_ext dotenv
%dotenv

or specify a path
%dotenv relative/or/absolute/path/to/.env
