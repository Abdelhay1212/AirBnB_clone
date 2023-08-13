# /usr/bin/python3
"""
This script defines a basic command-line interpreter for the HBNB project.

The interpreter provides a simple prompt "(hbnb) " where users can input commands.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program.

        Usage: quit
        """
        return True  # Exit the interpreter loop

    def do_EOF(self, args):
        """
        EOF command to exit the program.

        Usage: Press Ctrl+D
        """
        return True  # Exit the interpreter loop

    def do_create(self, args):
        """
        Create an instance of the specified class and print its ID.

        Usage: create <class_name>
        """
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name == 'BaseModel':
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Show the string representation of an instance.

        Usage: show <class_name> <instance_id>
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]

        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        req_instance = all_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)

    def do_destroy(self, args):
        """
        destroy an instance.

        Usage: destroy <class_name> <instance_id>
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]

        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        req_instance = all_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, args):
        """
        prints all exist instances of class BaseModel

        usage: all <class_name> or all
        """
        args_list = args.split()
        all_objs = storage.all()

        if len(args_list) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return

        if args_list:
            if args_list[0] not in ("BaseModel"):
                print("** class doesn't exist **")
                return
            else:
                print(["{}".format(str(v))
                       for _, v in all_objs.items() if type(v).__name__ == args_list[0]])
                return
    
    def do_update(self, args):


if __name__ == '__main__':
    # Start the HBNBCommand interpreter loop
    HBNBCommand().cmdloop()
