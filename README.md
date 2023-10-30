# Docker Manager

## Running app

App needs to be run is sudo
(maybe will implement logging into docker in the future, who knows?)

Also, there must be two variables in .env:
- PASSWORD
- SECRET_TOKEN

## Session manager
On login user gets a session token (token from now on) in a cookie, 
that he/she uses to authenticate. 

In future implement token rotation (if necessary).

## TODO
- api calls:
  - creating new container (with git link to clone)
  - checking status
  - turning on containers (one/all)
  - setting to be always on
- brute force protection