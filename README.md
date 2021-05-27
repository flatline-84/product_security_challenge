# The Zendesk Product Security Challenge

## Description
The good ol' one-two combo of Python + Flask.
<hr>

## Setup

This was tested using Python 3.6.9 and Python 3.8.5 on WSL and Linux, respectively.

1. Ensure Python 3.6 is installed or higher with `python3 -V`
2. Create a virtualenv to keep your host system clean from pip packages - `python3 -m venv .venv`
3. Activate the virtual env with `source .venv/bin/activate`
4. Install all requirements and dependencies with `python3 -m pip install -r requirements.txt`
5. Run the program with `python3 main.py`
6. Navigate to `http://localhost:8080/` in your browser.

## Implementation

### Main Features
* :white_check_mark: todo list
* :white_check_mark: virtual env
* :white_check_mark: create / register user page  
    * :white_check_mark: id, username, email, password
    * :white_check_mark: user id, index on email
    * :white_check_mark: 2FA
    * :white_check_mark: show 2FA here
    * :white_check_mark: password validations
    * :white_square_button: password complexity
    * :white_square_button: placeholder text with new forms
* :white_square_button: login page
    * :white_check_mark: don't return email or password wrong message
    * :white_check_mark: session tokens (check session fixation)
    * :negative_squared_cross_mark: will cookies be secure (generate SSL?)
    * :white_check_mark: require 2FA
    * :white_square_button: remember me
* :white_check_mark: log out
    * :white_check_mark: invalidate session correctly
* :white_square_button: reset password
    * :white_square_button: require email, old password, and OTP
* :white_square_button: app hardening
    * :white_square_button: CORS (won't implement)
    * :white_square_button: CSP
    * :white_square_button: Pragma, Cache, etc
    * :white_check_mark: CSRF on login, logout, register, change password
    * :white_check_mark: bruteforce protection?
* :white_square_button: CI/CD pipeline to build Docker image
    * :white_square_button: or to lint and verify no security issues


### Nice To Have  
*  captcha / bruteforce protection
* gunicorn
* IP filtering / geoblocking
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

