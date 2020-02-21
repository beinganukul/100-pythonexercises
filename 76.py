import zlib
s = 'Hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print t
print zlib.decompress(t)

