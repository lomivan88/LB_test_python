import re, sys

line_before = ""

for line in sys.stdin:
    if re.search("syslogd", line) and re.search("restart", line):
        if re.search("exiting", line_before):
            server_stop = line_before.rsplit()[0:3]
            server_start = line.rsplit()[0:3]
            sys.stdout.write(f"{' '.join(server_stop)}: Server turned off\n{' '.join(server_start)}: Server restarted")
        else:
            last_info = line_before.rsplit()[0:3]
            server_start = line.rsplit()[0:3]
            sys.stdout.write(f"{' '.join(last_info)}: Server crashed! \n{' '.join(server_start)}: Server restarted")
    #Z dat předpokládám jen dvě situace - log začíná datumem (lze zjistit čas před pádem serveru), či log začíná závorkou (nepotřebná informace)
    if line[0] != "(":                    
        line_before = line
        