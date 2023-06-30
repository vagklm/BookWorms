from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Route to retrieve a list of books
@app.route('/books')
def retrieve_books():
    try:
        # Connect to the database
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        
        # Retrieve all the items from the 'books' table
        cursor.execute("SELECT title, author, price, description FROM books")
        books = cursor.fetchall()
        
        # Convert the books to a list of dictionaries
        list_of_books = []
        for book in books:
            dict_of_books = {
                'title': book[0],
                'author': book[1],
                'price': book[2],
                'description ': book[3]
                }
            list_of_books.append(dict_of_books)
            
        # Close the database connection
        connection.close()
        
        # Return the list as json
        return jsonify(list_of_books)
    except sqlite3.Error as error:
        print("Error while connecting to sqlite database", error)

# Running the app
if __name__ == "__main__":
    app.run()