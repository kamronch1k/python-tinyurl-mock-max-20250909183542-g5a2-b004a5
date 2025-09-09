import hashlib
s='maxbridge'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
