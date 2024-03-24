#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):

    """
    Entry point of command interpreter for HBNB

    supports commands
        quit - exit program.
        help - provide available commands
        EOF - same as quit(end of file).
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Exits the program.
        """
        print("Exiting interpreter")
        return True

    def do_EOF(self, line):
        """
        Same as quit
        """
        print("Exiting")
        return True

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
