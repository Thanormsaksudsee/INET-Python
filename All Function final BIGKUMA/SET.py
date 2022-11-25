albums = ["Dub,Dancehall","Industrial,Heavy Metal","Techno,Dubstep","Synth-pop,Euro-Disco","Industrial,Techno,Minimal"]

albums = ','.join(albums)
albums = albums.split(',')
albums = set(albums)
albums = len(albums)
print(albums)
# print(len(set(','.join(albums).split(','))))