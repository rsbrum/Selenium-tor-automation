import subprocess, os, time

class Vpn(object):
    """
        Interfaces with OpenVPN through bash scripts and 
        manages its connection
    """
    def __init__(self):
        self.status = False
        self.pid = 0

    def start(self,server_address):
        """
            Creates the script directory,
            forms the server using *server_address*,
            creates the bash command using the script dir and server address,
            opens a new terminal and uses the created command,
            checks if the PID of the terminal has been written to a file,
            sets the VPN status to True
            if VPN status is false, throws an error
        """

        file_path = os.path.dirname(os.path.realpath(__file__)) + '/scripts/pid.txt'
        #server = server_address + ".udp.ovpn"
        server = server_address
        cmd = "gnome-terminal -e ' sh -c \"sudo echo $$ >> /home/rnsbrum/Desktop/dev/fatal/likerbot/controllers/vpn/scripts/pid.txt; /home/rnsbrum/Desktop/dev/fatal/likerbot/controllers/vpn/scripts/test.sh {}; sleep 20\"'" \
            .format(server)
        try:
            os.remove(file_path)
        except:
            pass 

        subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, 
                        stdout=subprocess.PIPE, shell=True)
        time.sleep(1)
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.pid = int(file.read())
                file.close()
                os.remove(file_path)

        else:
            raise Exception("Failed to get OpenVPN's PID")

        self.set_OpenVPN_status()
        
        if not self.status: 
            self.kill()
            raise Exception("OpenVPN connection failed")

    
    def set_OpenVPN_status(self):
        """
            Checks if the OpenVPN process is active
            It wasn't possible to find the exact PID so there is a 
            but it is usually 3 very close to the provided *pid*
            if both tests fail, OpenVPN is False
            else True
        """
        flag = None
        
        try:
            os.kill(self.pid,0)
        except:
            flag = True

        if flag == True:
            self.status = False
            return

        self.status = True
        

    def kill(self):
        """
            Kills any OpenVPN process and scripts spawned by the VPN
        """
        self.status = False
        os.system("sudo killall openvpn")
