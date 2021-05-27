# The Zendesk Product Security Challenge

## Description
The good ol' one-two combo of Python + Flask.
<hr>

## Setup

This was built using Python 3.8.5.

1. Ensure Python 3.8 is installed or higher with `python3 -V`
2. Install all requirements and dependencies with `python3 -m pip install -r requirements.txt`
3. Run the program with `python3 main.py`

## Implementation

### Main Features
* :heavy_check_mark: todo list
* :o: virtual env
* :o: create user page  
    * :o: id, username, email, password, 2fa token
    * :o: user id, index on email
    * :o: show 2FA here
* :o: login page
    * :o: don't return email or password wrong message
    * :o: CSRF ?
    * :o: session tokens (check session fixation)
    * :o: will cookies be secure (generate SSL?)
    * :o: require 2FA
    * :o: remember me
* :o: log out
    * :o: invalidate session correctly
    * :o: 302 redirect
* :o: reset password
    * :o: Send email? Pretty hard to do
    * :o: Security questions are bad practice
* :o: header hardening
    * :o: CORS
    * :o: CSP
    * :o: Pragma, Cache, etc
* :o: CI/CD pipeline to build Docker image?
    * :o: or to lint and verify no security issues


### Nice To Have  
*  captcha / bruteforce protection
* gunicorn
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

