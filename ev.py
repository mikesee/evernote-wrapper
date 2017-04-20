import os
import sys
import subprocess
import datetime

def today(): #daynote of today create or open(if exist)
	date = (datetime.date.today()).__format__("%y%m%d")

	try:
		f = open(ev_prg_path + "\\note.txt", mode="r+") #note file open or create
		data = f.read()
		f.close()	
	except:
		f = open(ev_prg_path + "\\note.txt", mode="w+")
		f.write(" ")
		f.close()
		subprocess.check_call([ens_path, 'createNote', '/s', ev_prg_path + '\\note.txt', '/n', 'day note', '/i', date]) #, shell=False, stderr=subprocess.STDOUT)
		""" not bed
		cmd = [ens_path, 'createNote', '/s', 'C:\\Program Files (x86)\\Evernote\\Evernote\\note.txt', '/n', 'day note', '/i', date]
		fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
		data = fd_popen.read().strip()
		fd_popen.close()
		"""
	subprocess.check_call([ens_path, 'shownotes', '/q', date ], shell=False, stderr=subprocess.STDOUT)

def open_note(): #Open note with query(sys.argv[1]). 
	subprocess.check_call([ens_path, 'shownotes', '/q', sys.argv[1]], shell=False, stderr=subprocess.STDOUT) #open title notebook

def open_ev(): #Just open evernote.exe. Because loader name is ev
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
	
	if (len(sys.argv) < 2): #ev
		open_ev()
	elif (sys.argv[1] == "t"): #ev t
		today()
	else: #anything. ignored over than "sys.argv[2]" 
		open_note()