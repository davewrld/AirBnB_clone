#!/usr/bin/python3
"""
Entry point of command interpreter for HBNB
"""

import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import storage
from models.user import User


class HBNBCommand(cmd.Cmd):

    """
    command line interpreter class
    supports commands
        quit - exit program.
        help - provide available commands
        EOF - same as quit(end of file).
    """

    prompt = "(hbnb)"

    def do_quit(self, line):
        """
        Exits the program.
        """
        return True

    def do_EOF(self, line):
        """
        Same as quit
        """
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]

        if class_name not in globals():
            print("** class name missing **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name.
        usage: all [<class name>]
        """
        str_list = []

        if not arg:
            all_dict = storage.all()
            for obj_id, obj in all_dict.items():
                class_name = obj_id.split('.')[0]
                Class = globals().get(class_name)
                if Class:
                    instance = Class(**obj)
                    str_list.append(str(instance))
            print(str_list)
        else:
            storage.reload()
            args = args.split()
            class_name = args[0]

            if class_name in globals():
                all_dict = storage.all()
                for obj_id, obj in all_dict.items():
                    if class_name in obj_id:
                        Class = globals()[class_name]
                        instance = Class(**obj)
                        str_list.append(str(instance))
                print(str_list)
            else:
                print("** class doesn't exist **")
                return False

    def do_update(self, arg):
        """
        Update an instance based on the class name and id
        by adding or updating an attribute.
        Usage:
        update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        obj_id = args[1]
        attr_name = args[2]
        attr_value = args[3]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        setattr(instance, attr_name, attr_value)
        instance.save()

    def help_help(self):
        """
        Dispaly help information
        """
        print("Available commands")

    def emptyline(self):
        """
        Handles an empty line + ENTER
        shouldn’t execute anything
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
