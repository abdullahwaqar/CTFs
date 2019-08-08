import zlib

compressesd_data = open('inDesign', 'rb').read()
dd = zlib.decompress(compressesd_data)

print(dd)

