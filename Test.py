import mysql.connector as connector
from getpass import getpass

try:
  with connector.connect(
    host="localhost",
    user=input("Wprowadz login: "),
    password=getpass("Wprowadz haslo: "),
    database="testowa"
  ) as connection:
    #create_db="CREATE DATABASE testowa"
    #with connection.cursor() as cursor:
    #  cursor.execute(create_db)
    # create_lists_table="""
    # CREATE TABLE lists(
    #   list_id INT UNSIGNED PRIMARY KEY,
    #   name VARCHAR(50)
    # )
    # """
    # create_items_table="""
    # CREATE TABLE items(
    #   item_id INT UNSIGNED PRIMARY KEY,
    #   name VARCHAR(50),
    #   price DECIMAL(10,2) UNSIGNED,
    #   list_id INT UNSIGNED,
    #   FOREIGN KEY(list_id) REFERENCES lists(list_id)
    # )
    # """
    with connection.cursor() as cursor:
      #cursor.execute(create_lists_table) #tu mozna bylo uzyc executemany
      # cursor.execute(create_items_table)
      # connection.commit()
except connector.Error as e:
  print(e)