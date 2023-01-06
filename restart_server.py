import re

with open("data.txt", "r", encoding="utf8") as f:
    text = f.readlines()
    line_before = ""
    for line in text:
        if re.search("syslogd", line) and re.search("restart", line):
            if re.search("exiting", line_before):
                server_stop = line_before.rsplit()[2]
                print(f"{server_stop}: Server turned off")
                server_start = line.rsplit()[2]
                print(f"{server_start}: Server restarted")
            else:
                last_info = line_before.rsplit()[2]
                print(f"{last_info}: Last information! Server crashed !")
                server_start = line.rsplit()[2]
                print(f"{server_start}: Server restarted")          
        line_before = line
            