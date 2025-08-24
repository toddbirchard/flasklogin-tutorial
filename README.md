# Flask-Login Tutorial

![Python](https://img.shields.io/badge/Python-v3.12-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v3.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Login](https://img.shields.io/badge/Flask--Login-v0.6.3-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v2.1.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-WTF](https://img.shields.io/badge/Flask--WTF-v1.2.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-v3.1.1-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/flasklogin-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/flasklogin-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/flasklogin-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/flasklogin-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/flasklogin-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/flasklogin-tutorial/network)

![Flask Login](https://raw.githubusercontent.com/toddbirchard/flasklogin-tutorial/master/flask_login_tutorial/static/dist/img/flasklogin%402x.jpg)

Add user authentication to your Flask app.

* **Tutorial**: [https://hackersandslackers.com/flask-login-user-authentication/](https://hackersandslackers.com/flask-login-user-authentication/)
* **Demo**: [https://flasklogin.hackersandslackers.com](https://flasklogin.hackersandslackers.com)

## Getting Started

Get set up locally in two steps:

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `ENVIRONMENT`: The environment to run your app in (either `development` or `production`).
* `FLASK_DEBUG`: Whether to enable "DEBUG" logging (either `True` or `False`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database.
* `LESS_BIN`: Path to your local LESS installation via `which lessc` (optional for static assets).

*Remember never to commit secrets saved in .env files to Github.*

### Installation

Get up and running with `make deploy`:

```shell
git clone https://github.com/toddbirchard/flasklogin-tutorial.git
cd flasklogin-tutorial
make install
make run
```

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
