
from __future__ import print_function # This is for   end='' feature for v2.6+
import os
import gui2
import sys
from gi.repository import GLib

global j1
j1 = 0
global j4
j4 = 0
def main() :
	# Open the fifo file named 'v2f' to read the matches
	fd = os.open("v2f", os.O_RDONLY)
	count = 0
	st = ""
	gtw = 0
	opn = 0	
	nom = 0
 	nomp = 0
	rl_count = 0
	# Never ending loop
	while True:
		# Read single character at a time so that parsing can be done as required
		ch = os.read(fd,1)
		if ch == '(' :
			# '(' is encounted at the beginning of the line input of terminal
			opn = 1
			rl_count = 0
			gui2.matches1 = []
			j1 = 0			
			nom = 0			
			count = 0
			st = ""
			gtw = 0
			
		elif ch == ')' :
			# ')' is encountered at the end of the line input of terminal
			opn = 0
			
		elif opn == 1 :					
			if ch == ' ':
				# 'space' is encountered when one word is completly read
				if rl_count == 0:
					gui2.num = 1
					gui2.matches1.insert(rl_count,st)
					try :			
						# Call 'textinit' funtion of gui2.py				
						GLib.idle_add(gui2.textinit)					
					except :
						e = sys.exc_info()
						print(e)
				rl_count += 1

			else :
				st += ch
		
		elif ch == ' ':
			# 'space' is encountered when one word is completly read
			# Then add that word to matches1 array of gui2
			# Same code in both 'if' and 'else' part. 2 parts are added for future modifications.
			if gtw == 1 :						
				gui2.matches1.insert(nom,st)
				nom += 1
			else :
				gui2.matches1.insert(nom,st)
				nom += 1
			# Store current number of matches to global 'num' of gui2
			gui2.num = nom
			count = 0	# initialize current word length and string variable
			st = ""

		elif ch == '!' : # If more that 20 matches are yet to be received
			gtw = 1
		elif ch == '^' :
			gui2.j4 = 0
			try :		
				# Call 'textinit' funtion of gui2.py					
				GLib.idle_add(gui2.textinit)					
			except :
				e = sys.exc_info()
				#print(e)
			
		elif ch == '#' :
			# End of input for current possibilities. Initialize variables to 0
			gui2.matches1 = []
			j1 = 0			
			nom = 0			
			count = 0
			st = ""
			gtw = 0

		else :
			count += 1			# Increment current word length
			if count <= 14 :
				st += ch		# Copy character to 'st' untill the word length is 14



