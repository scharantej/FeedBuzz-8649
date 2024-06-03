
# Import necessary modules
from flask import Flask, render_template, request
import sqlite3

# Create a Flask application
app = Flask(__name__)

# Establish a connection to the database
conn = sqlite3.connect('newsfeed.db')
c = conn.cursor()

# Define the main page route
@app.route('/')
def main_page():
    # Retrieve a list of news articles from the database
    c.execute("SELECT * FROM articles")
    articles = c.fetchall()
    
    # Render the main page, passing the list of articles
    return render_template('index.html', articles=articles)

# Define the individual article route
@app.route('/article/<int:article_id>')
def article(article_id):
    # Retrieve the specific news article by its ID
    c.execute("SELECT * FROM articles WHERE id=?", (article_id,))
    article = c.fetchone()
    
    # Render the individual article page, passing the article data
    return render_template('article.html', article=article)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
