## Flask Application Design for a Kids' Newsfeed

### HTML Files

- **index.html:**
   - The main page of the newsfeed, displaying a list of news articles. It will include placeholder elements for the news article titles, summaries, and images.
- **article.html:**
   - An individual news article page, displaying the full content of the article. When a news article title is clicked on the main page, it will load this page.

### Routes

- **main page**:
   - **Route:** '/'
   - **Method:** GET
   - **Function:** Retrieves a list of news articles from a data source (e.g., a database or API) and renders the `index.html` page, passing the list of articles as data.
- **individual article**:
   - **Route:** '/article/<int:article_id>'
   - **Method:** GET
   - **Function:** Retrieves a specific news article by its ID, based on the `<int:article_id>` variable in the URL. It renders the `article.html` page, passing the article data as data.