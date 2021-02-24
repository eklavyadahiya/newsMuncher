##This is a scrapy project intended to crawl news websites

#Steps to set up the project and start using:

- Clone the repository
- Install mongoDB on your computer. Once mongo is installed, follow these two guides on the basics:

https://medium.com/@haxzie/getting-started-with-mongodb-setting-up-admin-and-user-accounts-4fdd33687741
https://geekflare.com/getting-started-mongodb/
https://www.mongodb.com/basics

- Install requirements using pip/pip3

``pip3 install -r requirements.txt``

- Additionally, you may choose to set up a new scrapy project and copy over the changes from this repo

- Copy the newsMuncher/mongoConfig.py.example file to mongoConfig.py (copy, don't rename it). Enter your username, password, databasename and collection name in this file. It is an untracked file so that passwords don't get committed in the repo.

#Now that you're setup, add a website to crawl

- Open the file newsMuncher/newsMuncher/spiders/crawlers.py
- Copy the code between the comments and change the Class, name, allowed_domains, start_urls to reflect the target website. Notice that in the allowed_domains example, there are two entries instead of 1.
- In the parse_item function, we're using the item loader to define the url, title, author, article, date, and site variables. This will be passed into scrapy's items.py file to be processed and then into the pipelines.py file to be sent to mongodb.

#Add you css/xpath selectors
- url: you don't need to change this
- title: use a css/xpath selector to find the title of the article (hint: it's usually h1/h2)
- author: use a css/xpath selector to find the name of the author
- article: use a css/xpath selector to get the content of the article
- date: use a css/xpath selector to get the date
- site: add your site's main url here, no http, https or www. This is a static string.

In the example crawler i'm not using xpath selectors. You can use loader.add_xpath instead of loader.add_css. You need to modify the second item inside the brackets, the first one can remain as it is.

#How to test your css/xpath selector
- Choose an article from your target site
- Open the terminal to the root of the project and type:
``scrapy shell yourlink``
- (replace yourlink with the actual article link)

Scrapy will then download this page and you can test your selectors using:
response.xpath("your xpath here").extract() or response.css("your css class here").extract()

Don't worry about the html tags, just make sure you're getting the right elements, test it on 2/3 pages.

Remember: when using a css selector, add a '.' before the classname if it's a custom class. You can also fetch a nested class (like i've done in the 'author' field in the example).

#How to run the crawler
- Open the terminal to the root of the project and type:

``scrapy crawl name``

- Replace name with the name of your crawler that you defined.

Use an app (for eg. Robo3T) to connect to your mongo instance and check if data is being inserted correctly.
