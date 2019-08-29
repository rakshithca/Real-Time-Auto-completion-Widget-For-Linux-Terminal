#Real Time Auto completion Widget For Linux Terminal
“Real-Time Auto-Completion Widget” has two new features in real time alongside bash terminal, those are Double Press Tab(generating possible completion words) and Man Pages. This widget displays the completion of commands in set of 24 possibilities, and man pages on a scrollable window in two cases: when a command is completed on a terminal or when button on widget is clicked. We have also given a ‘lock’ button with which one can save the state of widget and refer this state while working in terminal. However, the features like man pages and double press tab are available in existing bash implementation, this work is recommended for the beginners and new users, so that they can overcome the complexities working with commands.
#Installation :
#Dependencies:
•	You need Gtk+ developer tools to compile and run the source, You can get it by typing the command
sudo apt-get install libgtk-3-dev


#Installation of ACwidget:
1.	Download  bash-4.3.30.tar.gz ( https://ftp.gnu.org/gnu/bash/bash-4.3.30.tar.gz ) and place in home directory
2.	Unzip the bash-4.3.30.tar.gz by command tar –zxvf  bash-4.3.30.tar.gz
3.	Change directory to bash-4.3.30/ by giving command cd bash-4.3.30/
4.	Run the below commands
a.	./configure --prefix=/user --bindir=/bin
b.	sudo make
c.	sudo make install
d.	exec bash
5.	Place gui2.py,vfifo3.py and acwidget.py in home directory
#Running the widget:
Open a new terminal run the command python acwidget.py
=======
# Real-Time-Auto-completion-Widget-For-Linux-Terminal

We introduced “Real-Time Auto-Completion Widget” alongside existing bash terminal. Two new features in real-time have been presented: Double Press Tab (generating possible completion words) and Man Pages. This widget displays the completion of commands in the set of 24 possibilities, and man pages on a scrollable window in two cases: when a command is completed on a terminal or when a button on the widget is clicked. Introduced a ‘lock’ button with which one can save the state of the widget and refer this state while working in the terminal.