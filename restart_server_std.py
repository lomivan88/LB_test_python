import re, sys

line_before = ""
regex_date_time = r"(([\w]{3})(\s{1})(\d{1,2})(\s{1})((\d{2}\:){2}\d{2}))"

for line in sys.stdin:
    if re.search("syslogd", line) and re.search("restart", line):
        if re.search("exiting", line_before):
            s_stop = re.match(regex_date_time, line)
            s_start = re.match(regex_date_time, line_before)
            # server_stop = re.split(r"\s+", line)[0:3]
            # server_start = re.split(r"\s+",line_before)[0:3]
            sys.stdout.write(f"{s_stop.group(0)}: Server turned off\n{(s_start.group(0))}: Server restarted")
        else:
            # last_info = line_before.rsplit()[0:3]
            # server_start = line.rsplit()[0:3]
            l_info = re.match(regex_date_time, line_before)
            s_start = re.match(regex_date_time, line_before)
            sys.stdout.write(f"{l_info.group(0)}: Server crashed! \n{s_start.group(0)}: Server restarted")
            
    line_before = line
        