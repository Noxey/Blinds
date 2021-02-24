import telnetlib


class MyShade:
    def __init__(self, target_id):
        self.position = 100
        self.target_id = target_id

    def moveshade(self, new_position):
        direction = new_position - self.position

        if new_position > 100: new_position = 100
        if new_position < 0: new_position = 0

        # moving shades down
        if new_position > self.position:
            move = '{ "id":1, "method": "mylink.move.down", "params": { "auth": "homeShades", "targetID" : %s} }' % self.target_id
            tn = telnetlib.Telnet("10.88.111.118", "44100")
            tn.write(move)
            self.position = new_position
            tn.close()
            self.position = new_position



        elif new_position < self.position:
            move = '{ "id":1, "method": "mylink.move.up", "params": { "auth": "homeShades", "targetID" : %s} }' % self.target_id
            tn = telnetlib.Telnet("10.88.111.118", "44100")
            tn.write(move)
            self.position = new_position
            tn.close()
            self.position = new_position


        else:
            return
