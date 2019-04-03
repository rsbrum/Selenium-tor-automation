#!/bin/bash
pid=$(pgrep vpn_init.sh)
kill -KILL $pid
