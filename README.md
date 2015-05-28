Health Check Service
======================================

A simple daemon to host a http health check on port 10241
for a backend program.

Healthcheck checks the status of a backend program according
to the command which is configured in config.json. If the command 
returns 0, it will start the HTTP server and returns "200 OKOKOK",
if not, the HTTP server will be terminated.
 
The general use cases:

1. In AWS :
   if you use ELB, use the daemon to monitor your service status,
   then ELB just check the TCP port 10241.

2. UDP service:
   use this daemon to provide a TCP health check for load balancers. 