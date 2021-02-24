import telnetlib

allShades = '"CC10344A.1"'
eastWall = '"CC10344A.2"'
southWall = '"CC10344A.3"'
shade1 = '"CC10344A.8"'
shade2 = '"CC10344A.7"'
shade3 = '"CC10344A.6"'
shade4 = '"CC10344A.4"'
shade5 = '"CC10344A.5"'

up = '"myLink.move.up"'
down = '"myLink.move.down"'

shade = allShades
direction = down

#move = '{ "id":1, "method": %s, "params": { "auth": "homeShades", "targetID" : %s} }' % (up, allShades)

move = '{ "id":1, "method": "mylink.down", "params": { "auth": "homeShades", "targetID" : %s} }' % (allShades)

tn = telnetlib.Telnet("10.88.111.118", "44100")


tn.write(move)
tn.close()
