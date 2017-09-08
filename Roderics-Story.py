# by Carl Monk (@ForToffee)
# github.com/ForToffee/Robosapien

# command codes from http://www.aibohack.com/robosap/ir_codes.htm
import robo

rs=robo.Robo(21)	#create Robo object for GPIO 21
rs.send_code(0xB1)	#Issue reset command


raw_input('Enter to start my story')
rs.send_code(0x81)	#Right arm up
rs.send_code(0xA6)  #FORWARD STEP
rs.send_code(0xC6)	#BULLDOZER
rs.send_code(0xA5)	#LEAN FORWARD
rs.send_code(0xAB)	#LISTEN
rs.send_code(0xCE) #ROAR

raw_input('Enter')
rs.send_code(0xCE)	#Roar

print "fin"
