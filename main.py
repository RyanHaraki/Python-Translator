import mysql.connector
from difflib import get_close_matches

conn = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database",
    connection_timeout=300
)

cursor = conn.cursor()
word = input("Enter a word: ")
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)

results = cursor.fetchall()

if results:
    for result in results:
        print(results[1])
else:
    query = cursor.execute("SELECT Expression FROM Dictionary")
    results = cursor.fetchall()
    words = [word[0] for word in results]
    match =  get_close_matches(word, words)
    if len(match) > 0:
        response = input(f"Did you mean {match}? Press Y if you did, press N if you didn't. ").upper()
        if response == 'Y':
            query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % match[0])
            results = cursor.fetchall()
            print(results[0])
        elif response == 'N':
            print("We do not understand what word you're looking for.")
        else:
            print("We do not understand what word you're looking for.")
    else:
        print("Error")