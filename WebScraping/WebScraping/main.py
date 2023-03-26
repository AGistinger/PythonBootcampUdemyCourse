# Web Scraping
# A general term for the techniques involving automating
# the gathering of data from a website.
# When a browser loads a website, the user gets to see
# what is known as the "front-end" of the website.
# Main things you need to understand:
# * Rules of Web Scraping
#   - Always try to get permission before scraping.
#   - If you make too many scraping attempts or requests
#   your IP address could get blocked.
#   - Some sites automatically block scraping software.
# * Limitations of Web Scraping
#   - In general every website is unique, which means
#   every web scraping script is unique.
#   - A slight change or update to a website may completely
#   break your web scraping script.
# * Basic HTML and CSS
import lxml  # Beautiful soup uses this for the backend
import requests
import bs4

# Grabbing a Title
result = requests.get("http://www.example.com")
print(type(result))  # Response

# Create soup variable
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
title = soup.select("title")[0].getText()
print(title)
site_paragraphs = soup.select("p")
print(site_paragraphs)

# Grabbing a Class
# Syntax                    Match Results
# soup.select("div")        All elements with "div" tag
# soup.select("#some_id")   Elements containing id="some_id"
# soup.select(".some_class) Elements containing class="some_class"
# soup.select("div span")   Any elements named span with a dev element
# soup.select("div > span") Any elements named span directly within a div element
# These use CSS syntax
res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
wiki_soup = bs4.BeautifulSoup(res.text, "lxml")
first_item = wiki_soup.select(".vector-toc-list")[0]

for item in wiki_soup.select(".vector-toc-list-item"):
    print(item.text.split("\n"))

# Grabbing an Image
web_res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
chess_soup = bs4.BeautifulSoup(web_res.text, "lxml")
print(chess_soup.select(".thumbimage"))
computer = chess_soup.select(".thumbimage")[0]
print(computer["src"])
img_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png")
# img_link.content
f = open("my_computer_image.jpg", "wb")  # Write Binary "wb"
f.write(img_link.content)
f.close()

# Book Examples
# Working with Multiple Pages and Items
# Get the title of every book with a 2-star rating
# https://books.toscrape.com/catalogue/page-1.html

# Deal with page number changes for URLs
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
page_num = 12
base_url.format(page_num)

# Scrap every page in catalogue with the loop and get the star rating
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, "lxml")
products = soup.select(".product_pod")
example = products[0]
print(example)
# You need to use dots to fill out space
example.select(".star-rating.Three")
# How to get the title of the book
print(example.select("a")[1]['title'])

# We can check if something has 2 stars (string call in, example.select(rating))
# example.select('a')[1]['title'] to grab the book title

two_star_titles = []

for n in range(1, 51):
    # Get the URL for the correct page
    scrape_url = base_url.format(n)
    # Start a request for the URL
    res = requests.get(scrape_url)
    # Start a soup on the text for the page
    soup = bs4.BeautifulSoup(res.text, "lxml")
    # Get the book product object
    books = soup.select(".product_pod")

    for book in books:
        # Check if the select does not return an empty list
        if len(book.select(".star-rating.Two")) != 0:
            # Get the book title
            book_title = book.select('a')[1]["title"]
            # Add the book title to the list
            two_star_titles.append(book_title)

for book in two_star_titles:
    print(book)

# Connect to http://quotes.toscrape.com/ and get the HTML text from the homepage
res = requests.get("http://quotes.toscrape.com/")
home = res.text

# Get the names of all the authors on the first page
soup = bs4.BeautifulSoup(res.text, "lxml")
authors = set()

for name in soup.select(".author"):
    authors.add(name.text)

# Create a list of all the quotes on the first page
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

# Inspect the site and use Beautiful soup to extract the top ten tags
# from the requests text shown on the right of the home page.
for item in soup.select(".tag-item"):
    print(item.text)

# Notice how there is more than one page, Use what you know about for loops
# and string concatenation to loop through all the pages and get all the
# unique authors on the website.
url = "http://quotes.toscrape.com/page/{}"
authors = set()
page_still_valid = True
page = 1

while page_still_valid:
    page_url = url.format(str(page))
    res = requests.get(page_url)

    if "No quotes found!" in res.text:
        page_still_valid = False
        break

    soup = bs4.BeautifulSoup(res.text, "lxml")

    for name in soup.select(".author"):
        authors.add(name.text)

    page += 1

print(authors)
