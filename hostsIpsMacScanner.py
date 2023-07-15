import subprocess
import json

def get_host_ip_mac_address():

    p = ['ping', '127.0.0.1', '-c', '1'] # linux and mac
    subprocess.check_output(p) # ping is neded to refresh arp table 
    
    arp_command = ['arp', '-a']
    output = subprocess.check_output(arp_command).decode()
    lines = output.splitlines()

    results = []
    for i in range(len(lines)):     
        id=i
        if("(" in lines[i].split()[0]):
            hostname = ""
        else:
            hostname=lines[i].split()[0] 
        if('at' in lines[i].split()[1] ):
            ip = lines[i].split()[0].replace("(","").replace(")","")
        else:
            ip=lines[i].split()[1].replace("(","").replace(")","")
        if('on' in lines[i].split()[3] ):
            mac=lines[i].split()[2]
        else:
            mac=lines[i].split()[3]

        value = {
            "id": id,
            "hostname": hostname,
            "ip": ip,
            "mac": mac
         }
        results.append(value)
    
    
    toJson = {
        "host" : results
    }
    return json.dumps(toJson)


with open("scanResults.json", "w") as outfile:
    outfile.write(get_host_ip_mac_address())

######## how to load this json #########
i =json.loads(get_host_ip_mac_address()) 
print(i,'\n')
print(i['host'][0])
print(i['host'][0]['hostname'])



