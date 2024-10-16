import time

def parse_duration(duration):
    """Parses a duration string and returns the corresponding future Unix timestamp.

    Args:
        duration (str): A string representing the duration. 
                        Valid formats are:
                        - 'm' for minutes (e.g., '5m' means 5 minutes)
                        - 'h' for hours (e.g., '2h' means 2 hours)
                        - 'd' for days (e.g., '1d' means 1 day)
                        - 'w' for weeks (e.g., '3w' means 3 weeks)

    Returns:
        float: The Unix timestamp of the current time plus the given duration.
                       Returns None if the input is invalid.
    """    
    try:
        if duration.endswith('m'):
            return time.time() + (int(duration[:-1]) * 60)
        elif duration.endswith('h'):
            return time.time() + (int(duration[:-1]) * 3600)
        elif duration.endswith('d'):
            return time.time() + (int(duration[:-1]) * 86400)
        elif duration.endswith('w'):
            return time.time() + (int(duration[:-1]) * 604800)
        else:
            return None
    except ValueError:
        return None
