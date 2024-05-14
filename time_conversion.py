def time_conversion (s: str):
    
    period = s[-2:]
    
    minutes = s[3:5]
    
    seconds = s[6:8]
    
    important_hour = s[:2]
    
    important_hour_diff = s[1]
    
    
    if period == 'AM':
        if int(important_hour) == 12:
            print(f"00:{minutes}:{seconds}")
        else:
            print(s[:-2])
    else:
        if int(important_hour) == 12:
            print(s[:-2])
        else:
            if int(important_hour) >= 10: 
                print(f"{int(important_hour)+12}:{minutes}:{seconds}")
            else:
                print(f"{int(important_hour_diff)+12}:{minutes}:{seconds}")

            
            
    
time_conversion("12:40:22AM")