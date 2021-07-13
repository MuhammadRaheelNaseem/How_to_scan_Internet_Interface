# Made By Muhammad Raheel

# First install library in this way 
# pip3 install psutil
# pip3 install tabulate

# if you install in windows you must in this way
# py -m pip install psutil
# py -m pip install tabulate

import psutil
from tabulate import tabulate

class InterfaceScanner(object):
    def __init__(self):
        self.instance=psutil.net_if_addrs()
    
    def scanner(self):
        self.interfaces=[]
        self.address_ip=[]
        self.netmask_ip=[]
        self.broadcast_ip=[]
        for interface_name,interface_addresses in self.instance.items():
            self.interfaces.append(interface_name)
            for address in interface_addresses:
                if str(address.family)=="AddressFamily.AF_INET":
                    self.address_ip.append(address.address)
                    self.netmask_ip.append(address.netmask)
                    self.broadcast_ip.append(address.broadcast)
        
        data={"Interface ":[*self.interfaces],
              "IP-Address ":[*self.address_ip],
              "Netmask ":[*self.address_ip],
              "Broadcast-IP ":[*self.netmask_ip]
             }
        return tabulate(data,headers="keys",tablefmt="github")
    
    def __str__(self):
        return str(self.scanner())
    
if __name__=="__main__":
    print(InterfaceScanner())
