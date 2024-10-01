import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, create_staff, get_all_staffs)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))


'''
Staff Commands: Add student
'''

staff_cli = AppGroup('student', help='Staff objects commands')

@staff_cli.command("create", help="Creates a staff")
@click.argument("firstname", default="akash")
@click.argument("lastname", default="singh")
@click.argument("password", default= "akashpass")
def create_staff_command(firstname, lastname, password):
    create_staff(firstname, lastname, password)
    print(f'{firstname, lastname, password} created!')


@staff_cli.command("get-student", help="Retrieves staff by name")
@click.argument("staffname", default="string")
def list_staff_command(staffname):
    if staffname == 'string':
        print(get_all_staffs())
   


app.cli.add_command(staff_cli)

'''
Review Commands
'''
review_cli = AppGroup('review', help= 'Review objects commands')

@review_cli.command("add_review", help = "Adds a review")
@click.argument('firstname', default = 'akash')
@click.argument('lastname', default = 'singh')
@click.argument('text', default = 'Nirvan is a student who tend to lose focus in class.')
def add_review_command(firstname, lastname, text):
    akash = User.query.filter_by(firstname=firstname).first()
    if not akash:
        print(f'{firstname} not found!')
        return
        new_review = Review(text)
        akash.reviews.append(new_review)
        db.session.add(akash)
        db.session.commit()
        print('Review added!')

app.cli.add_command(review_cli)


