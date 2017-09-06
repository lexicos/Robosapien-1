# by Carl Monk (@ForToffee)
# github.com/ForToffee/Robosapien

# command codes from http://www.aibohack.com/robosap/ir_codes.htm
import robo
Hex_integer = 0

rs=robo.Robo(21)	#create Robo object for GPIO 21
#rs.send_code(0xB1)	#Issue reset command

while True:
	Hex_string = raw_input("Input Command or bye to exit now  ")
	if Hex_string == "bye" : break
	try:
		Hex_integer = int(Hex_string, 16)
		rs.send_code(Hex_integer)
		print "Command sent"
	except :
		print "Invalid string"
		continue

print "fin"
