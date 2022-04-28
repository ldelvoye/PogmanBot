import mysql.connector
from mysql.connector import errorcode
from cogs.setup_db import db, cursor

def use_database(db_name):
    cursor.execute(f"USE {db_name}")

def create_database(db_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET 'utf8'")
    print(f"Database {db_name} created!")
    
def create_course_table(course):
    table = (
        f"CREATE TABLE `{course}` ("   
        "   `assignment_name` varchar(250) NOT NULL,"
        "   `date_due` varchar(250) NOT NULL,"
        "   `percentage_worth` int(11) NOT NULL,"
        "   `tag` varchar(250) NOT NULL,"
        "   PRIMARY KEY (`assignment_name`)"
        ") ENGINE=InnoDB")
    
    try:
        print("Creating table {}: ".format(course), end='')
        cursor.execute(table)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
        
def create_coop_table(term):
    table = (
        f"CREATE TABLE `{term}_COOP` ("   
        "   `round_number` varchar(250) NOT NULL,"
        "   `apps` int(11) NOT NULL,"
        "   `date_open` varchar(250) NOT NULL,"
        "   `date_due` varchar(250) NOT NULL,"
        "   `interview_period` varchar(250) NOT NULL,"
        "   `employer_rankings` varchar(250) NOT NULL,"
        "   `student_rankings_due` varchar(250) NOT NULL,"
        "   `match_results` varchar(250) NOT NULL,"
        "   PRIMARY KEY (`round_number`)"
        ") ENGINE=InnoDB")
    
    try:
        print("Creating table {}: ".format(f"{term} COOP"), end='')
        cursor.execute(table)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
        
def add_onto_course_table(name, end, worth, tag):
    cursor.execute(f"INSERT INTO pogmanbot.courses(assignment_name, date_due, percentage_worth, tag) VALUES('{name}', '{end}', '{worth}', '{tag}')")
    db.commit()

def add_onto_coop_table(round_num, apps, date_open, date_due, interview_period, employer_rankings, student_rankings, match_results):
    cursor.execute(f"INSERT INTO pogmanbot.1b_coop(round_number, apps, date_open, date_due, interview_period, employer_rankings, student_rankings_due, match_results) VALUES ('{round_num}', {apps}, '{date_open}', '{date_due}', '{interview_period}', '{employer_rankings}', '{student_rankings}', '{match_results}')")
    db.commit()

def retrieve_column_headers(table):
    sql = f"SELECT group_concat(column_name) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}'"
    cursor.execute(sql)
    values = cursor.fetchall()
    return values[0][0].split(',')

def count_rows(table):
    sql = f"SELECT COUNT(*) FROM PogmanBot.{table}"
    cursor.execute(sql)
    return cursor.fetchall()[0][0]

def get_specific_course_values(course):
    if course == "all":
        sql = f"SELECT * from PogmanBot.courses"
    else:
        sql = f"SELECT * from PogmanBot.courses WHERE tag = '{course}'"
    cursor.execute(sql)
    output = []
    values = cursor.fetchall()
    for i in values:
        output.append(list(i))
    return output

def get_coop_values():
    sql = f"SELECT * from PogmanBot.1b_coop"
    cursor.execute(sql)
    output = []
    values = cursor.fetchall()
    for i in values:
        output.append(list(i))
    return output
