################Definition Block#################
import pyautogui as pgui
import time

################Function Block#################
#Single press
def key_input_single( x , num = 1 ):
    for i in range( num ):
        pgui.keyDown( x )
        pgui.keyUp( x )

#Multiple press
def key_input_multiple( x , y , z = 'null'):
    pgui.keyDown( x )
    pgui.keyDown( y )
    if z != 'null':
        pgui.keyDown( z )
        pgui.keyUp( z )
    pgui.keyUp( y )
    pgui.keyUp( x )

################Body Block#################
#Focus change to previous window
key_input_multiple( 'alt' , 'tab' )

#Open Option
key_input_multiple( 'ctrlright' , 'return' )

#Check off
key_input_multiple( 'alt' , 'f' )

#Move to next setting
key_input_single('tab' , 7 )

key_input_single('down')
key_input_single('tab')
key_input_single('down')
key_input_multiple( 'alt' , 'c' )

#Enter the value
pgui.typewrite(['0', '.', '1'])

#Apply setting
key_input_single( 'return' )
time.sleep(1)

#Next
key_input_multiple( 'alt' , 't' )
key_input_single('p')
key_input_multiple( 'alt' , 's' )
time.sleep(3)

#Close notice window
key_input_multiple( 'alt' , 'F4' )

#Window close
key_input_single('esc')

#Open color palette
key_input_multiple( 'ctrlright' , 'alt' , 'c' )

#Move to next setting
key_input_single('tab' , 9 )

key_input_single('down')
key_input_single('return')