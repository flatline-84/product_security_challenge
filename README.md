# The Zendesk Product Security Challenge

## Description
The good ol' one-two combo of Python + Flask.

[![ZenChair CI](https://github.com/flatline-84/product_security_challenge/actions/workflows/main.yml/badge.svg)](https://github.com/flatline-84/product_security_challenge/actions/workflows/main.yml)
<hr>

## Setup

### Running with Docker-Compose
1. Ensure docker-compose and docker are installed on your system.
2. `docker-compose up -d` from the root folder of this project (i.e where docker-compose.yml is)
3. Profit

### Running with Docker  
1. Build the image with `docker build --tag zenchair .`
2. `docker run --name zenchair -p 5001:5001 zenchair`

### Running Natively with Python  
This was tested using Python 3.6.9 and Python 3.8.5 on WSL and Linux, respectively.

1. Ensure Python 3.6 or higher is installed with `python3 -V`
2. Create a virtualenv to keep your host system clean from pip packages - `python3 -m venv .venv`
3. Activate the virtual env with `source .venv/bin/activate`
4. `cd` into the `project` folder.
5. Install all requirements and dependencies with `python3 -m pip install -r requirements.txt`
6. Run the program with `python3 main.py`
7. Navigate to `https://localhost:8080/` or what is shown in the console in your browser.

### Running Unit Tests  
1. `cd project`
2. `python tests/test_basic.py` will run all tests by default

## Implementation

### Todo List
* :white_check_mark: todo list
* :white_check_mark: virtual env
* :white_check_mark: create / register user page  
    * :white_check_mark: id, username, email, password
    * :white_check_mark: user id, index on email
    * :white_check_mark: 2FA
    * :white_check_mark: show 2FA here
    * :white_check_mark: email, password validations
    * :white_check_mark: password complexity
    * :white_check_mark: placeholder text with new forms
* :white_check_mark: login page
    * :white_check_mark: don't return email or password wrong message
    * :white_check_mark: session tokens (check session fixation)
    * :white_check_mark: will cookies be secure (generate SSL?)
    * :white_check_mark: require 2FA
* :white_check_mark: log out
    * :white_check_mark: invalidate session correctly
* :white_check_mark: reset password
    * :white_check_mark: require email, old password, and OTP
* :white_square_button: app hardening
    * :x: CORS
    * :white_check_mark: CSP
    * :white_check_mark: XSS, mimetype, etc headers
    * :white_check_mark: CSRF on login, logout, register, change password
    * :white_check_mark: bruteforce protection on login / IP lockout
* :white_check_mark: CI/CD pipeline
    * :white_check_mark: docker image from dockerfile
    * :white_check_mark: lint and verify no security issues (bandit)

### Misc / Nice To Have  
* captcha 
* :white_check_mark: bruteforce protection
* :x: gunicorn
* :white_check_mark: IP filtering / geoblocking
* email reset?
* :white_check_mark: SSL 
* :white_check_mark: logging
* :white_check_mark: unit tests

### Issues 
* ~~email enumeration when registering. Not sure the correct thing to do here~~

<hr>

## Main Features

1. Accounts
    * Password ~~SHA256 hashed + salted~~ bcrypt and salted
    * Password complexity requirement (custom validator)
    * OTP required for login and password change
    * 5 failed logins blocks IP ADDRESS, not account 
    * last login time and IP address logged in DB
2. Cookies
    * HTTPOnly, Secure
    * Signed (but not encrypted)
3. Sessions
    * proper invalidation - log out clears all session data
    * page permissions (no roles)
    * no session fixation 
4. Input
    * all input is sanitized coming in and jinja templates encode on the way out
    * CSRF tokens on all forms  
5. SSL
    * SSL certificate added for encrypted comms (check versions?)
6. IP Whitelisting  
    * allow specific subnets to access
7. Logging
    * logs on auth attempts and logout, db errors
    * logs to both console and logfile
8. Security Headers
   * X-Content-Type-Options
   * X-XSS-Protection
   * X-Frame-Options
   * Referrer-Policy
   * Content-Security-Policy
   * Server
9. Unit Testing
   * unit testing implemented (need better checks)
10. Static Source Code Analyzer
   * runs bandit as part of pipeline (one issue: all interfaces, leave in as demo)
11. Dockerized
    * dockerfile receives secrets from environment
12. CI/CD pipeline
    * runs unit tests
    * dockerizes app


<hr>

## The Challenge

Implement an easy, secure authentication mechanism that allows users to:
- Create an account
- Log in and log out
- Reset their password

We have created the basic boilerplate for you (which you are free to modify) and it is up to you to implement the server-side functionality and expand from there. There is no restriction on language, frameworks or implementation, however we ask that: 
- You consider the security challenges that come with any authentication mechanism and implement controls to protect against common attacks.
- You document the controls you have implemented and come to your interview prepared to justify these decisions.
- Your submission is linked to your GitHub account (i.e. the forked repository you created) and contains all the source code and clear documentation on how to run the application (a dockerized, packaged, or compiled submission is welcome, but not essential). 
- You have fun and hopefully learn something! Whilst we know this isn’t strictly a developer role, the ability to understand what goes into secure design and implementation is an important part of our job. The time it takes to complete this task will vary based on your previous experience, but we don’t want you up until 2am every night trying to get this done. We are looking for a submission that demonstrates your abilities and knowledge.
 
If you are having trouble, for whatever reason, please reach out to us! 

