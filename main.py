import rollerShade

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

while True:
    myShade3 = rollerShade.MyShade(shade3)
    value = input("Enter Shade Position:\n")
    myShade3.moveshade(value)

#move = '{ "id":1, "method": "mylink.move.up", "params": { "auth": "homeShades", "targetID" : %s} }' % shade3

#tn = telnetlib.Telnet ("10.88.111.118", "44100")
