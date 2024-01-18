

# General purpose

This is a small personal project to setup a lightweight database locally and build a basic UI to add, update and delete records in said database. 
The application allows users to 
The idea was to research as much as possible on my own, without following any kind of tutorial.
Any feedback is welcome, but remember that these are my first steps in python :)!

# The address book app

## Use 

Users can download the script and run the main.py file to open the GUI. 
The local database contains a few example rows. 
The GUI allows them to add addresses to the database. 
The script does contain a module that shows the initialization of the database. 

[!IMPORTANT]
The database uses an open source website to retrieve the zipcodes of Belgian municipalities, of wich only the Flemish ones were selected. 
Users can therefore only select municipalities in the Flemish region in Belgium.

## Goals 

I had several goals for this project. 
Generally, i wanted to increase my overall knowledge and familiarity with python. 
More specifically, I had the following goals in mind: 

- Use python to open a very lightweight database and use sqlalchemy as a method to query it. 
I am very used to querying databases in raw sql so this was new to me. 

- I wanted to build a small weight GUI and researched Tkinter a bit for a basic UI with some interactivity

- Setting up a full-fletched project with a more typical python structure (seperate logic and UI, License, Readme) and use git to share and document it.