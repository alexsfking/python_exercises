def check_logs(log):
    if(not log):
        return 0
    last_entry,days="0",1
    for entry in log:
        if(entry<=last_entry):
            days+=1
        last_entry=entry
    return days