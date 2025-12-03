from datetime import datetime

def format_datetime(dt) :
    if dt is None :
        return ""
    return dt.strftime("%B %d, %Y at %I : %M%p")
