#!/usr/bin/expect 
set cmd [lindex $argv 0];
set pid [exp_pid]

spawn ~/Desktop/dev/fatal/likerbot/controllers/vpn/scripts/task.sh "$cmd" "$pid"

expect  "Enter Auth Username:" {
    send -- "rnsbrum@gmail.com\r"
    
    expect  "Enter Auth Password:" {
        send -- "Cel91476045!\r"
    }

}

interact    
