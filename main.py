from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

# Route to retrieve a list of books
@app.route('/books', methods=['GET'])
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

# Route to create a new book    
@app.route('/books', methods=['POST'])
def create_book():
    # Get the required information from the submission form
    title = request.form.get('title')
    author = request.form.get('author')
    price = request.form.get('price')
    description = request.form.get('description')
    
    # Checking if all required fields are given
    if not title or not author or not price:
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        #Connect to the 'books' database
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        
        # Add the new book to the table
        cursor.execute("INSERT INTO books (title, author, price, description) VALUES (?, ?, ?, ?)",
                (title, author, price, description))

        # Commit changes and close the database
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite database", error)
    
    # Return a message that the book was successfully created
    return jsonify({'message': 'The book was successfully created!'}), 201

# Route to render the html.file for the book creation form
@app.route('/create_book', methods=['GET'])
def render_book_creation():
    return render_template('book_creation.html')
# Running the app
if __name__ == "__main__":
    app.run()