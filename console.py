#!/usr/bin/python3
"""defines HBNB command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter (Ctrl+D)"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

