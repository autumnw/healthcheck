Health
======================================

A simple daemon to host a http health check on port 10241
for a backend program.

Healthcheck checks the status of a backend program according
to the command which is configured in config.json. If the command 
returns 0, it will start the HTTP server and returns "200 OKOKOK",
if not, the HTTP server will be terminated.
 