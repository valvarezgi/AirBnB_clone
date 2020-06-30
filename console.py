#!/usr/bin/python3
"""Module console
"""

import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


classes = {"BaseModel": BaseModel,
           "User": User,
           "Place": Place,
           "State": State,
           "City": City,
           "Amenity": Amenity,
           "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Class Command line"""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit commad to exit interpreter
        """
        return True

    def do_EOF(self, args):
        """exit → End of File
        """
        return True

    def emptyline(self):
        """An empty line → Enter should not execute nothing
        """
        return False

    def do_create(self, args):
        """Create a new instance of class in JSON file
        """
        if not args:
            print("** class name missing **")
        elif args in classes:
            for key in classes:
                if key == args:
                    new_instance = classes[key]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance
        """
        if len(args.split()) == 0:
            print("** class name missing **")
            return

        if args.split()[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args.split()) < 2:
            print("** instance id missing **")
            return

        key_to_find = args.split()[0] + "." + args.split()[1]

        if key_to_find not in storage.all().keys():
            print("** no instance found **")
            return

        print(storage.all()[key_to_find])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        if len(args.split()) == 0:
            print("** class name missing **")
            return

        if args.split()[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args.split()) < 2:
            print("** instance id missing **")
            return

        key_to_find = args.split()[0] + "." + args.split()[1]

        if key_to_find not in storage.all().keys():
            print("** no instance found **")
            return

        del storage.all()[key_to_find]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name
        """
        if args:
            if args not in classes:
                print("** class doesn't exist **")
                return

        instance_list = []
        for key in storage.all().keys():
            if key.split(".")[0] == args:
                instance_list.append(str(storage.all()[key]))
            elif not args:
                instance_list.append(str(storage.all()[key]))
        if len(instance_list) == 0:
                pass
        else:print(instance_list)
        return

    def do_update(self, args):
        """ Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>
        """
        array = shlex.split(args)
        if len(array) == 0:
            print("** class name missing **")
        elif array[0] not in classes:
            print("** class doesn't exist **")
        elif len(array) == 1:
            print("** instance id missing **")
        elif len(array) == 2:
            print("** attribute name missing **")
        elif len(array) == 3:
            print("** value missing **")
        else:
            key_to_find = array[0] + "." + array[1]
            name_attr = array[2]
            value = array[3]
            if value.replace(".", "").isdigit():
                if value.isdigit():
                    value = int(value)
                else:
                    value = float(value)
            setattr(storage.all()[key_to_find], name_attr, value)

            storage.all()[key_to_find].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
