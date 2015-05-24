import os

user = "root"
workers = 2
bind = "10.31.45.10:8002"
pidfile = "/var/run/gunicorn-cncmaps.pid"
backlog = 2048
logfile = "/var/log/gunicorn-cncmaps.log"
loglevel = "debug"
