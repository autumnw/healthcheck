#!/bin/sh
ps -ef | grep sensu-trapd | grep python
exit $?
