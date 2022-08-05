from modules.globvars import keypath
from modules.ft_otp import GenerateTOTP
from modules.checkpsswd import NewPsswd
import modules.stdmsg as msg
from modules.cript import CryptKey, DecriptKey
from modules.checkkey import CheckValidKey, WriteKey
from getpass import getpass
from os.path import exists
from modules.checkpsswd import CheckPsswdLength

def ChangePassword():
	usrPsswd = getpass("Password: ")
	if usrPsswd == 'c' or usrPsswd == 'C':
		return False
	if DecriptKey(usrPsswd.encode()):
		newPsswd = NewPsswd()
		if newPsswd != None:
			if CryptKey(newPsswd.encode()):
				return True
	else:
		msg.err_msg("Incorrect password. Try again or press 'C' + [Enter] to cancel.")
		ChangePassword()


def ChangeMasterKey(key):
	if CheckValidKey(key):
		usrPsswd = getpass("Password: ")
		if usrPsswd == 'c' or usrPsswd == 'C':
			return False
		if CheckPsswdLength(usrPsswd):
			if not exists(keypath):
				WriteKey(key)
				if CryptKey(usrPsswd.encode()):
					return True
			elif exists(keypath):
				if DecriptKey(usrPsswd.encode()):
					WriteKey(key)
					if CryptKey(usrPsswd.encode()):
						return True
				else:
					msg.err_msg("Incorrect password. Try again or press 'C' + [Enter] to cancel.")
					ChangeMasterKey(key)
		else:
			print("Try again or press 'C' + [Enter] to cancel.")
			ChangeMasterKey(key)
	return False

def ObtainTOTP(key):
	totp = GenerateTOTP(key)
	msg.info_msg(totp)