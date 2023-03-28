./env/Sc  # python-bp
Python Boilerplate

# Example Project

This repo contains an example python project with a folder structure and files you need to develop
software professionally.

Clone the repo,
``` batch
git clone https://github.com/clazie/python-bp.git
cd python-bp
```

create a virtual environment with
``` batch
python -m venv env
.\env\Scripts\activate.ps1
```

maybe update with
````batch
python.exe -m pip install --upgrade pip
pre-commit autoupdate
``` 

and run `pip install -e .[dev]` to setup the project locally.

After that, run `tox` which will run pre-commit, linting and pytest for you.

# Git Credentials
``` bash
git config user.name "new name"
git config credential.username "new name"
```
