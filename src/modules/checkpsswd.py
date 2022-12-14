import modules.utils.stdmsg as msg
from getpass import getpass
from modules.cript import CryptKey, DecriptKey

def RequirePsswd():
	usrPsswd = str(getpass("Password: "))
	if DecriptKey(usrPsswd.encode()) and CryptKey(usrPsswd.encode()):
		return usrPsswd.encode()
	elif usrPsswd == 'c' or usrPsswd == 'C':
		return None
	else:
		msg.TryAgainPsswd()
		RequirePsswd()
	return None


def NewPsswd():
	usrInput = str(getpass("Write a new password: "))
	if usrInput == 'c' or usrInput == 'C':
		msg.load_msg("Canceled.")
		return None
	if CheckPsswdLength(usrInput):
		usrCheck = getpass("Write the same password again: ")
		if usrInput != usrCheck:
			msg.err_msg("Passwords must match.")
			return None
		elif usrInput == usrCheck:
			return usrInput
	return None


def CheckPsswdLength(psswd):
	if len(psswd) < 6 or len(psswd) > 16:
		msg.err_msg("Password would be with 6 minimum characters and max 16")
		return False
	else:
		return True
