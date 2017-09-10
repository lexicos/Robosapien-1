# by Carl Monk (@ForToffee)
# github.com/ForToffee/Robosapien

# command codes from http://www.aibohack.com/robosap/ir_codes.htm
import robo
import time
Hex_integer = 0
Hex_list=[]

rs=robo.Robo(21)	#create Robo object for GPIO 21


raw_input('Enter to start programme my story')
programme = (raw_input("Type a series of commands   "))
string_list = programme.split(",")
print "Ok you typed in the folliwng list"
print string_list
time.sleep(2)
print "let convert that Hex to Numbers for Roderick"

for i in string_list :
    try:
        Hex_integer = int(i , 16)
        print Hex_integer
        Hex_list.append(Hex_integer)
    except:
        print "Invalid input"
        continue
print "About to start Sending"
time.sleep(2)

for i in Hex_list :
    print "Sending", i
    rs.send_code(i)
    time.sleep(5)

print "Finished nothing left to do"
