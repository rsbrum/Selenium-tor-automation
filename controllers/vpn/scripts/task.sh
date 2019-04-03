#!/bin/bash

cmd=$1
echo $$ > ./controllers/vpn/scripts/output2.txt
cd /etc/openvpn/ovpn_udp/
sudo openvpn $cmd
