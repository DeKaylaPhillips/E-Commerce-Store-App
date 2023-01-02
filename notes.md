# E-COMMERCE WEBSITE
*Pre-Project*
- ~~install~~ django
- ~~install~~ requests
- ~~install~~ dotenv
- ~~freeze~~ requirements.txt

*Store Project*
- ~~configure~~ settings.py: installed_apps, static files directory
- ~~configure~~ urls.py
- ~~mkdir~~ static: touch app.css, touch app.js  

  
*Store Application*
- ~~touch~~ urls.py
- ~~touch~~ templates.py
- views.py: set up API and routes  
  

  1. Home Page - index.html - Route: "/"
    - Includes site navigation links

  2. Category Pages - Route: "/category/<int:id>"
    - List all items in the category based on the category id
      - *Bonus*: Pagination Bootstrap component implementation
      - *Bonus*: "Featured Products" 
        - 3 special items at the top of each category page
        - check readme for additional features to implement here
  
  3. Individual Product Page - Route: "/product/<int:id>"
    - Display name, category, price, image
    - Give option to add to cart
      - Click button multiple times to increase quantity
  
  4.  Shopping Cart Page - Route: "/shopping-cart"
    - Include link back to homepage
    - Subtotal updates with quantity
    - Total updates when subtotal calculated
  
  5.  Search Page - Route: "/search/<str:query>"
    - Search for products based on keywords used in query
    - Display noun project icon and "out of stock" text if query unsuccessful

*Notes*
      - Bootstrap Navbar compenent or css
      - Bootstrap grid or css
      - Extra bootstrap component (dropdown, carousel, etc) or css
      - Basic styling using css
      - Avoid repeating HTML by using {% extends layout.html %}

*Root Directory*
- ~~touch~~ .env file
  - ~~API_KEY~~
  - ~~SECRET_KEY~~
  
- ~~touch~~ .gitignore 
  - ~~.venv~~
  - ~~.env~~
  - ~~__pycache__)~~

