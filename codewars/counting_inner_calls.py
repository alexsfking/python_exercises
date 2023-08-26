import sys

function_call_count = 0

def count_calls(func, *args, **kwargs):
    global function_call_count
    function_call_count = 0
    sys.settrace(trace_calls)
    return_value=func(*args)
    sys.settrace(None)
    return(function_call_count-1,return_value)

def trace_calls(frame, event, arg):
    global function_call_count
    if event == 'call':
        function_call_count += 1
    return trace_calls

