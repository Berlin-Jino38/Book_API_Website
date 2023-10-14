# Book_API_Website
# Project Description:

The Book API Website is a comprehensive platform that provides access to information about authors and the number of books they have published. This web application is equipped with a powerful RESTful API that enables Create, Read, Update, and Delete (CRUD) operations directly from API endpoints. The API is secured with JWT (JSON Web Tokens) authentication to ensure data integrity and user access control. Additionally, the API supports features such as pagination, searching, and ordering for efficient data retrieval.

# Key Features:

Access author details, including their names, biographies, and other relevant information.
Retrieve information on the number of books published by each author.
Utilize a RESTful API to perform CRUD operations for authors and books.
Secure API access with JWT-based authentication.
Implement pagination to efficiently navigate through large datasets.
Search for authors and books by various criteria.
Order and sort data for customized data presentation.

The application will be accessible at http://localhost:8000.

# API Endpoints:

/api/author/: Retrieve a list of all authors or create a new author.
/api/author/<author_id>: Get, update, or delete a specific author by ID.
api/book: Retrieve a list of all books or create a new book.
api/book/<book_id>: Get, update, or delete a specific book by ID.
api/auth-jwt/ : to create Token for authentication purpose
api/auth-jwt-refresh/: to refresh the existing token within 5 minutes
api/auth-jwt-verify/:to verify the Token is valid or not
