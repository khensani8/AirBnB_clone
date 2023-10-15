#!/usr/bin/python3
"""defines HBNB command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User



class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    @staticmethod
    def convert_type(value):
        """Convert a string value to its appropriate data type."""
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value

    def do_EOF(self, arg):
        """Exit the command interpreter (Ctrl+D)"""
        return True

    def do_all(self, arg):
        """Print all string representations of instances."""
        args = arg.split()
        all_objects = storage.all()
        if not args:
            print([str(obj) for obj in all_objects.values()])
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objects.items() if args[0] in key])

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Update an instance's attributes."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key in all_objects:
                obj = all_objects[key]
                attr_name = args[2]
                attr_value = args[3]
                if hasattr(obj, attr_name):
                    attr_value = HBNBCommand.convert_type(attr_value)
                    setattr(obj, attr_name, attr_value)
                    obj.save()
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
