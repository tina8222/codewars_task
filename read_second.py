def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

print(make_readable(0))
print(make_readable(35678))
print(make_readable(3600))
print(make_readable(908765))
print(make_readable(29843))
print(make_readable(123456))