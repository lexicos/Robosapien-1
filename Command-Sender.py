# by Carl Monk (@ForToffee)
# github.com/ForToffee/Robosapien

# command codes from http://www.aibohack.com/robosap/ir_codes.htm
import robo

rs=robo.Robo(21)	#create Robo object for GPIO 21
#rs.send_code(0xB1)	#Issue reset command

while True:
	Hex_command = raw_input("Input Command or bye to exit now")
	if Hex_command == "bye" : break
	print "Hex command is"
	print Int(Hex_command)
	print int(Hex_command, 16)
	rs.send_code(Hex_command)
	print "Command sent"
	rs.send_code(0xB1)

print "fin"
