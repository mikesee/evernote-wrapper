import os
import sys
import subprocess
import datetime

def create_and_show_note():
	f = open(ev_prg_path + "\\note.txt", mode="w+")
	f.write(" ")
	f.close()
	
	subprocess.check_call([ens_path, 'createNote', '/s', ev_prg_path + '\\note.txt', '/n', 'day note', '/i', date])
	subprocess.check_call([ens_path, 'shownotes', '/q', date], shell=False, stderr=subprocess.STDOUT)
	
	f = open(ev_prg_path + "\\note.txt", mode="w+")
	f.write(date) #date overwrite in note.txt
	f.close()

def open_ev(): #Just open evernote.exe. Because loader name is ev
	try:
		subprocess.check_call(ev_prg_path + "\evernote.exe"	, shell=False, stderr=subprocess.STDOUT)
	except:
		pass #print "except"

def today(): #daynote of today create or open(if exist)
	if os.path.isfile(ev_prg_path + "\\note.txt"):
		print "note.txt is exist"
		f = open(ev_prg_path + "\\note.txt", mode="r+")
		data = f.read()
		f.close()

		print "data: " + data

		if data == date:
			print "data == date"
			subprocess.check_call([ens_path, 'shownotes', '/q', date ])
		else:
			print "overwrite and open note" 
			create_and_show_note()
	else:
		print "note.txt is not exist"
		create_and_show_note()

def open_note(): #Open note with query(sys.argv[1]). 
	subprocess.check_call([ens_path, 'shownotes', '/q', sys.argv[1]], shell=False, stderr=subprocess.STDOUT) 
	
if __name__ == "__main__":
	date = (datetime.date.today()).__format__("%y%m%d")
	ev_prg_path = ""

	if os.environ.get("PROGRAMFILES(X86)") is None: #this case is 32bit 
	    ev_prg_path = os.environ.get("PROGRAMFILES")
	else:
	    ev_prg_path = os.environ.get("PROGRAMFILES(X86)")

	ev_prg_path = ev_prg_path + "\Evernote\Evernote"
	ens_path = ev_prg_path + "\enscript.exe" #enscript path

	"""
	x64: C:\Program Files (x86)\Evernote\Evernote\
	x86: C:\Program Files\Evernote\Evernote\
	"""
	
	if (len(sys.argv) < 2): #ev
		open_ev()
	elif (sys.argv[1] == "t" or sys.argv[1] == "T"): #ev t EV T
		today()
	else: #anything. ignored over than "sys.argv[2]" 
		open_note()
		