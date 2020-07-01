# AirBnb Clone

This project is the first step to build an AirBnB clone, its a command interpreter that can create objects and perform tasks with these.

## How to run?

```bash
    git clone https://github.com/MiguelP4lacios/AirBnB_clone
    cd AirBnB_clone
    ./console.py
```

## Usage
### Interactive mode
Following the previous steps, start the interactive mode of the console 

### Non interactive mode
A file with commands can be piped into the console to execute it

## Commands:
### all
Returns a list of instances with the class name given. If a class name is not given, the command all prints all the instances. 
The valid class names are: Amenity, BaseModel, City, Place, Review, State, User

```bash
./console.py 
(hbnb) all
["[User] (c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c) {'id': 'c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c', 'created_at': datetime.datetime(2020, 7, 1, 16, 17, 42, 68117), 'updated_at': datetime.datetime(2020, 7, 1, 16, 17, 42, 68147)}", "[City] (9da46466-c49d-4880-b323-2dbe8a0bc658) {'id': '9da46466-c49d-4880-b323-2dbe8a0bc658', 'created_at': datetime.datetime(2020, 7, 1, 16, 18, 41, 387475), 'updated_at': datetime.datetime(2020, 7, 1, 16, 18, 41, 387505)}"]
```

Alternative - <class name>.all()


### create

Creates a new instance of 'class-name', and returns the id of instance, and saves the instance to the json file.

```bash
./console.py 
(hbnb) create User
c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c
(hbnb) 
(hbnb) create City
9da46466-c49d-4880-b323-2dbe8a0bc658
```

### destroy
Deletes an instance based on 'class name' and 'id'. And updates the json file
```bash
./console.py 
(hbnb) destroy City 9da46466-c49d-4880-b323-2dbe8a0bc658
(hbnb) 
```

### show
Returns the string representation of an instance based on the class name and id

```bash
./console.py 
(hbnb) show User c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c
[User] (c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c) {'id': 'c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c', 'created_at': datetime.datetime(2020, 7, 1, 16, 17, 42, 68117), 'updated_at': datetime.datetime(2020, 7, 1, 16, 17, 42, 68147)}
```
 
Alternative  <class name>.show(<id>)

### update
Updates an instance of 'class name' and 'id' with an attribute and value. The command ignores everything after the first attribute-value pair

```bash
./console.py 
(hbnb) show User c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c
[User] (c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c) {'id': 'c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c', 'created_at': datetime.datetime(2020, 7, 1, 16, 17, 42, 68117), 'updated_at': datetime.datetime(2020, 7, 1, 16, 17, 42, 68147)}
(hbnb) update User c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c name "Pepe"
(hbnb) show User c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c[User] (c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c) {'id': 'c0aa3e46-e5bd-4aab-8be6-edd1a8296e0c', 'created_at': datetime.datetime(2020, 7, 1, 16, 17, 42, 68117), 'updated_at': datetime.datetime(2020, 7, 1, 16, 23, 51, 199063), 'name': 'Pepe'}
```

### help

Provides the documentation of the avalaible commands

```bash
 ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

## Authors
[Miguel Palacios](http://https://github.com/MiguelP4lacios/ "Miguel Palacios")
[Valeria Alvarez](https://github.com/valvarezgi "Valeria Alvarez")
