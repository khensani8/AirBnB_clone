#!/usr/bin/python3
"""defines the HBNB command interperter"""
import cmd

class HBNBCommand(cmd.Cmd):
	""""commnad interprter for HBNB"""
	
	prompt = (hbnb)
	
	def do_quit(self, arg):
		"""Exits the command interpreter"""
			return True

	def do_EOF(self, arg):
		"""Exits the commnad interpreter with (Ctrl+d)"""
			return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
