#enscript.exe wrapper
import os
import sys
import subprocess
import datetime

def today(): #daynote of today create or open
	f = open((datetime.date.today()).__format__("%y%m%d"), "w")
	

	
	subprocess.check_call([ens_path, 'shownotes', '/q',  ], shell=False, stderr=subprocess.STDOUT)

def open_note(): #include idpw, daynote 
	subprocess.check_call([ens_path, 'shownotes', '/q', sys.argv[1]], shell=False, stderr=subprocess.STDOUT) #open title notebook

def open_ev(): #just evernote.exe open. because loader name is ev
	try:
		subprocess.check_call(ev_prg_path + "\evernote.exe"	, shell=False, stderr=subprocess.STDOUT)
	except:
		pass #print "except"
	
if __name__ == "__main__":
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
	
	if (len(sys.argv) < 2):		
		open_ev()
	elif (sys.argv[1] == "t"):
		today()
	else: #except anything. sys.argv[1] is note title
		open_note()
		
