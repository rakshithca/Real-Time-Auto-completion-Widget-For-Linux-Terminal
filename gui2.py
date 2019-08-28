
from gi.repository import Gtk, GdkPixbuf, Gdk, GLib, GObject
import Image
import os, sys
import time
import vfifo3
import threading


global num
num = 0
global j4
j4 = 0

global matches1
matches1=[]

global prev_man
prev_man = 0

global lock
lock = 0
global lockbutton


global i 
i = 0
j2 = 0
 
 #creating table buttons
button11 = Gtk.Button(label="Open ")#array added as label
button12 = Gtk.Button(label="Source")
button13 = Gtk.Button(label="Project")
button14 = Gtk.Button(label="")
button21 = Gtk.Button(label="")
button22 = Gtk.Button(label="Developed")
button23 = Gtk.Button(label="By")
button24 = Gtk.Button(label="")
button31 = Gtk.Button(label="VARUN")
button32 = Gtk.Button(label="SHARMA")
button33 = Gtk.Button(label="N")
button34 = Gtk.Button(label="")
button41 = Gtk.Button(label="KARTHIK")
button42 = Gtk.Button(label="PRABHU")
button43 = Gtk.Button(label="")
button44 = Gtk.Button(label="")  
button51 = Gtk.Button(label="LIBIN")
button52 = Gtk.Button(label="K J")
button53 = Gtk.Button(label="")
button54 = Gtk.Button(label="")

button61 = Gtk.Button(label="RAKSHITH")
button62 = Gtk.Button(label="C A")
button63 = Gtk.Button(label="")
button64 = Gtk.Button(label="")


global c1
c1 = 0

class TableWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Auto-Completion Widget")
	
	self.set_size_request(500,200)
	self.connect_after('destroy', self.destroy)#call self.destroy on destroy event
#	self.connect_after('delete_event', self.destroy)
	
	self.main_box=Gtk.VBox()# vertical box which is added in
	global box1
	box1 = self.main_box
	
	global prev_man
	prev_man = 0
	 
	self.main_box.set_spacing(5)

	self.label = Gtk.Label("Commands") 
	
	global table
        table = Gtk.Table(7,4, True)#table of 7*4
        
	self.add(self.main_box)
        self.main_box.pack_start(self.label, False, False, 0)# packing vbox from top with label
        self.main_box.pack_start(table, False, False, 0)#adding a table 

               
    	global buttonX
	global buttonX1
	buttonX = Gtk.Button(label="Alt + P for more")   # Alt + P button will be binded in future revisions
	label = Gtk.Label.new_with_mnemonic("_ Alt + P for more")
	label.set_mnemonic_widget(buttonX)
	buttonX.connect_after('clicked', self.start_clicked)
	buttonX.set_label("Click for more options")
	buttonX1 = Gtk.Button(label="Alt + P for more") 
	buttonX1.connect_after('clicked', self.start_clicked1)
	buttonX1.set_label("back")

	button11.connect_after('clicked', show_man)
	button12.connect_after('clicked', show_man)
	button13.connect_after('clicked', show_man)
	button14.connect_after('clicked', show_man)
	button21.connect_after('clicked', show_man)
	button22.connect_after('clicked', show_man)
	button23.connect_after('clicked', show_man)
	button24.connect_after('clicked', show_man)
	button31.connect_after('clicked', show_man)
	button32.connect_after('clicked', show_man)
	button33.connect_after('clicked', show_man)
	button34.connect_after('clicked', show_man)
	button41.connect_after('clicked', show_man)
	button42.connect_after('clicked', show_man)
	button43.connect_after('clicked', show_man)
	button44.connect_after('clicked', show_man)
	button51.connect_after('clicked', show_man)
	button52.connect_after('clicked', show_man)
	button53.connect_after('clicked', show_man)
	button54.connect_after('clicked', show_man)
	button61.connect_after('clicked', show_man)
	button62.connect_after('clicked', show_man)
	button63.connect_after('clicked', show_man)
	button64.connect_after('clicked', show_man)


	table.attach(button11, 0, 1, 0, 1) 
        table.attach(button12, 1, 2, 0, 1)
        table.attach(button13, 2, 3, 0, 1)
        table.attach(button14, 3, 4, 0, 1)
	table.attach(button21, 0, 1, 1, 2)
        table.attach(button22, 1, 2, 1, 2)
        table.attach(button23, 2, 3, 1, 2)
        table.attach(button24, 3, 4, 1, 2)
	table.attach(button31, 0, 1, 2, 3)
        table.attach(button32, 1, 2, 2, 3)
        table.attach(button33, 2, 3, 2, 3)
        table.attach(button34, 3, 4, 2, 3)
        table.attach(button41, 0, 1, 3, 4)
        table.attach(button42, 1, 2, 3, 4)
        table.attach(button43, 2, 3, 3, 4)
        table.attach(button44, 3, 4, 3, 4)
        table.attach(button51, 0, 1, 4, 5)
        table.attach(button52, 1, 2, 4, 5)
        table.attach(button53, 2, 3, 4, 5)
        table.attach(button54, 3, 4, 4, 5)
        table.attach(button61, 0, 1, 5, 6)
        table.attach(button62, 1, 2, 5, 6)
        table.attach(button63, 2, 3, 5, 6)
        table.attach(button64, 3, 4, 5, 6)
	table.attach(buttonX, 1, 3, 6, 7)
	table.attach(buttonX1, 0, 1, 6, 7)
	
	global lockbutton
	lockbutton = Gtk.ToggleButton("Lock")
	lockbutton.set_active(False)
	lockbutton.connect("toggled",on_button_toggled)
	table.attach(lockbutton,3, 4, 6, 7)

	
    	self.show_all() 
    	   
    def start_clicked(self, button):

    	if lock == 0:
    		if (num - vfifo3.j1) >= 24:
			settext(vfifo3.j1 + 24)		# Add 24 to 'j1' and refresh button labels
		
    def start_clicked1(self, button):

    	if lock == 0:
    		bj1 = vfifo3.j1 - 24
    		if(bj1 >= 0) :			  
			settext(bj1)		# Subtract 24 from 'j1' and refresh button labels
    
    def destroy(window, self):
        Gtk.main_quit()

 
def on_button_toggled(button):
	global lock
	global lockbutton
	#lockbutton = Gtk.ToggleButton("Lock")
	lockbutton = button
	if button.get_active():
		lock = 1
		lockbutton.set_label("Unlock")
	else :
		lock = 0
		settext(vfifo3.j1)
		lockbutton.set_label("Lock")
	      
        
        
def textinit():		# called from vfifo3.py
	global prev_man	
	settext(0)
		

# back button linked function
def go_back_1(button):
	global prev_man
	try:
		if lock == 0 : 								
			app.remove(box2)
			app.add(box1)
			app.show_all()
			prev_man = 0
	except :
		e = sys.exc_info()
		#print(e)
		
	
    	
def show_man(button):
	global box2
	global prev_man
	global lock
	global lockbutton
	lockbutton = Gtk.ToggleButton("Lock")
	if lock == 0 :
		lockbutton.set_active(False)
		lockbutton.set_label("Lock")
	else :
		lockbutton.set_active(True)
		lockbutton.set_label("Unlock")
	if lock == 0 :
		box2 = Gtk.VBox()
		try:
			if prev_man == 0 :
				app.remove(box1)
				app.add(box2)
			
		except :
			e = sys.exc_info()
			#print(e)
		
		global table2
        	table2 = Gtk.Table(7,4, True)
		
		label = Gtk.Label("Man Page of " + button.get_label()) 
        	box2.pack_start(label, False, False, 0)# packing vbox from top with label
        	box2.pack_start(table2, False, False, 0)#adding a table 
	
        	#creating table buttons
   	
		buttonv2X =Gtk.Button(label="Go back") 
		buttonv2X.connect_after('clicked', go_back_1)
       
		table2.attach(buttonv2X, 0, 3, 6, 7)
		
		table2.attach(lockbutton,3, 4, 6, 7)
		lockbutton.connect("toggled",on_button_toggled)
		
		
   		sw = Gtk.ScrolledWindow()
   		table2.attach(sw,0,4,0,6)
        	textview = Gtk.TextView()
        	textview.set_editable(False)
        	textview.set_cursor_visible(False)
        	textbuffer = textview.get_buffer()

        	sw.add(textview)

        	box2.pack_start(sw, False, False, 0)

		# Find the manual entry for the text in button and copy the man page to file 'm2' of current directory
        	ret = os.system("man " + button.get_label() + " > m2")
        	#print ret;

		# If man page is found, open the 'm2' file and read its contents
        	if ret == 0 :
        		infile = open("m2", "r")
        		if infile:
        	   		string = infile.read()
        	   		prev_man = 1
        	    		infile.close()
        	    		
        	elif ret == 256:   
        		app.remove(box2)
			app.add(box1)    	        		
        		string = "Empty"
        		prev_man = 0
        	else :
	        	string = "No Manual entry for " + button.get_label()
	        	prev_man = 1
        	    	
        	textbuffer.set_text(string)   	
   		app.show_all()  		
   		global c1
   		c1 = 0
    	
    	
# settext() initializes the button label
def settext(j3) :
	global lock
    	global prev_man
    	global c1
    	if prev_man == 1 :
    		try :
    			if lock == 0 :
    				lockbutton.set_active(False)
    				if c1 == 0:
	    				prev_man = 0
					app.remove(box2)
					app.add(box1)
					app.show_all()
					c1 = 1
				
			else :
				lockbutton.set_active(True)				
    			
		except :
			e = sys.exc_info()
			#print(e)
		
	i = j3
	global j4
	if(j4 == 0) :
		i = 0
		j4 = 1
	vfifo3.j1 = i
	n = num   # number of matches 
		
	k = n - i
	
	# assign label to buttons if the 'lock' button is unlocked

	if lock == 0:
		try :	
			if k >= 1 :	
				button11.set_label(matches1[i+0])			
			else :
				button11.set_label(" ")
	
			if k >= 2 :
				button12.set_label(matches1[i+1])
			else :
				button12.set_label(" ")
	
			if k >= 3 : 
				button13.set_label(matches1[i+2])
			else :
				button13.set_label(" ")
			if k >= 4 :	
				button14.set_label(matches1[i+3])
			else :
				button14.set_label(" ")
			if k >= 5 :	
				button21.set_label(matches1[i+4])
			else :
				button21.set_label(" ")
			if k >= 6 :	
				button22.set_label(matches1[i+5])
			else :
				button22.set_label(" ")
			if k >= 7 :
				button23.set_label(matches1[i+6])
			else :
				button23.set_label(" ")
			if k >= 8 :
				button24.set_label(matches1[i+7]) 
			else :
				button24.set_label(" ")
			if k >= 9 :
				button31.set_label(matches1[i+8])
			else :
				button31.set_label(" ") 
			if k >= 10 :
				button32.set_label(matches1[i+9])
			else :
				button32.set_label(" ") 
			if k >= 11 :
				button33.set_label(matches1[i+10]) 
			else :
				button33.set_label(" ")
			if k >= 12 :
				button34.set_label(matches1[i+11])
			else :
				button34.set_label(" ") 
			if k >= 13 :
				button41.set_label(matches1[i+12])
			else :
				button41.set_label(" ") 
			if k >= 14 :
				button42.set_label(matches1[i+13])
			else :
				button42.set_label(" ") 
			if k >= 15 :
				button43.set_label(matches1[i+14])
			else :
				button43.set_label(" ") 
			if k >= 16 :
				button44.set_label(matches1[i+15])
			else :
				button44.set_label(" ") 
			if k >= 17 :
				button51.set_label(matches1[i+16])
			else :
				button51.set_label(" ") 
			if k >= 18 :	
				button52.set_label(matches1[i+17])
			else :
				button52.set_label(" ")
			if k >= 19 : 
				button53.set_label(matches1[i+18])
			else :
				button53.set_label(" ")
			if k >= 20 :
				button54.set_label(matches1[i+19])
			else :
				button54.set_label(" ")
			if k >= 21 :
				button61.set_label(matches1[i+20])
			else :
				button61.set_label(" ") 
			if k >= 22 :	
				button62.set_label(matches1[i+21])
			else :
				button62.set_label(" ")
			if k >= 23 : 
				button63.set_label(matches1[i+22])
			else :
				button63.set_label(" ")
			if k >= 24 :
				button64.set_label(matches1[i+23])
			else :
				button64.set_label(" ")
		except :
			print(" \n\n Exception \n\n")
		if n == 1:
			if prev_man == 0:
				ret1 = os.system("man " + button11.get_label() + " > m2")
				if ret1 == 0:
					show_man(button11)

	return
def main():
	global app
	app = TableWindow()
	
	# To keep the widget above all windows
	app.set_keep_above(True)
	
	app.set_gravity(Gdk.Gravity.SOUTH_WEST)	

	Gtk.main()

if __name__ == "__main__":# for any error, exit
    sys.exit(main())
