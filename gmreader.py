#!/usr/bin/env python

import sys, time, subprocess, os
import getpass, argparse
import textwrap, BeautifulSoup, HTMLParser
import imaplib, email

def getTerminalSize():#gets size of terminal screen
	env = os.environ
def ioctl_GWINSZ(fd):
	try:
		import fcntl, termios, struct
		cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,'1234'))
	except:
		return
	return cr
	cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
	if not cr:
		try:
			fd = os.open(os.ctermid(), os.O_RDONLY)
			cr = ioctl_GWINSZ(fd)
			os.close(fd)
		except:
			pass
	if not cr:
		cr = (env.get('LINES', 25))
		try:
			cr = (env['LINES'], env['COLUMNS'])
		except:
			cr = (25, 80)
	return int(cr[1]), int(cr[0])

def element_find(element, body):
	try:
		element = body.findAll(element)[0].text
	except IndexError:
		element = None

	return element

def sythesize_elements(*arg):
	message = []
	for i in range(len(arg)):
		if arg[i]:
			message.append(arg[i] + '. ')
	if not message:
		message = 'Undefinable'
	else:
		message = ', '.join(message)
	return message

def speak(cmd, messages):
	for i in range(len(messages)):
		subprocess.call([cmd, messages[i]])
		time.sleep(0.5)

def reader(server):
	h = HTMLParser.HTMLParser()#for parsing html in text/html compliant messages
	
	server.select(readonly=1)
	(retcode, msgs) = server.search(None, "UNSEEN")#get unseen messages

	if retcode == 'OK':
		for msg in reversed(msgs[0].split(' ')):
			msg_num = msg
			(width, height) = getTerminalSize()
			print width*'-','Email #', msg_num,'\n',width*'-'
			(ret, msginfo) = server.fetch(str(msg), "RFC822")
			
			if ret == 'OK':
				msg = email.message_from_string(msginfo[0][1])
				for part in msg.walk():
					content = part.get_content_type()
					if part.get_content_type() == 'text/plain':
						message = str(part.get_payload())

					if part.get_content_type() == 'text/html':
						body = BeautifulSoup.BeautifulSoup(part.get_payload())
						p = element_find("p", body)
						font = element_find("font", body)
						div = element_find("div", body)
						synth_msg = textwrap.wrap(sythesize_elements(p, font, div))
						Message = h.unescape(' '.join(synth_msg))

				From = h.unescape(str(msg['From']))
				Date = h.unescape(str(msg['Date']))
				Subject = h.unescape(str(msg['Subject']))

				print 'From: ',From,'\n'
				print 'Date: ',Date,'\n'
				print 'Subject: ',Subject,'\n'
				print 'Message: ',Message,'\n'

				if sys.platform == 'linux' or sys.platform == 'Win32' or sys.platform == 'linux2':#checks if system is linux/windows or mac
					cmd = 'espeak'
				elif sys.platform == 'darwin':
					cmd = 'say'
				else:
					print "Your os is not compatible with gmreader. Sorry."
					sys.exit(1)

				#compiles message into one array of text
				speech = ['Email number, ' + str(msg_num), 'Subject: ' + Subject, 'fruhm: ' + From, 'Message: ' + Message]
				
				speak(cmd, speech)#start speech mechanism ->see above

def main():
	parser = argparse.ArgumentParser(version='gmreader v0.1.6', description="Listen to your gmails instead of reading them. Let python do the talking.")  

	parser.add_argument('address', help='Your email address')	
	parser.add_argument('password', help='The password to your gmail account')

	
	#User Authorization
	if len(sys.argv)==1:
		address = raw_input("Email Address: ")
		password = getpass.getpass('Password: ')
	else:
		args=parser.parse_args()
		address = str(args.address)
		password = str(args.password)

	mail_server = imaplib.IMAP4_SSL("imap.gmail.com", 993)#initiate gmail server along 992 port

	#Authorizing email and password through server
	try:
		mail_server.login(address, password)
	except:
		print sys.exc_info()[1]
		sys.exit(1)

	reader(mail_server)	
	mail_server.close()

if __name__ == '__main__':
	main()
