# This  class is responsible for modeling the author who writes articles and 
# keeps track of an author's articles, the magazines they have written  for and the topics they cover

class Author:

    # this is a class attribute keeping track of the author instances
    # when an Author object is instantiated is gets added to the list
    all_authors = []

    # initializes a new Author instance with name and validates the input given by the user or during test implementation
    
    def __init__(self, name):

# checks if a name is string if not raises an exception

        if not isinstance(name, str):
            raise Exception("Name must be a string")
        # checks if name is not an empty string
        if len(name) <= 0:
            raise Exception("Name must be longer than 0 characters")
        
        # this sets the name attribute a private variable to store the name
        self._name = name
        # adds the author instance to the all_authors list
        # it is called by Author(name)
        # e.g author1= Author("Sir Elly")
        Author.all_authors.append(self)

   # this sets the name attribute a private variable to store the name attribute and 
   # allows access to name while ensuring it cannot be changed after initialization
   # the @property decorator makes it read only propert which makes it accessible e.g print(author1.name) but cannot be modified after initialization
    
    @property
    def name(self):
        return self._name
    
    # this return a list of of all Article objects written by the  given author, by iterating through the class attribute Article.all which is a list of all the articles and filters them and when it encounters the matching author it returns the articles, called by author1.articles()
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    

    # this returns a list of all Magazine objects the author has written for
    # it calls the articles()   method to get all the articles written by the author and extracts the magazine attribute from each article
    # it utilizes set to remove any duplicates since an author might have written several articles for the same magazine then converts the set back to list, called by author1.magazines()

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    

    # creates and returns a new Article instance which associates with the author
    # it receives a magazine instance and a title as argument
    # then calls the Article class constructor, passing self which is the author, the magazine and title
    # called by magazine1= Magazine("Taifa Leo", "Daily Nation")
    # author1.add_article(magazine1, "River and the source")

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    


    # returns a list of categories for magazines the author has contributed to, it gives None if the author has no articles.
    # it calls the articles() method checking if the author has written any articles
    # if yes it then calls magazines() to get the magazines the author has written for and 
    # extracts the category from each magazine removing dublicates using set and taking it back to list, (sounds amazing!!!)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([magazine.category for magazine in self.magazines()]))



# In this class, itis used to represent a magazine.
# Each magazine has a name and category
# It tracks all the magazines instances and  lists the articles assorciated with each magazine, identify the contributors and provide info on its articles and assorciated authors

class Magazine:

    # class attribute keeping track of all Magazine instances
    # when a Magazine object is instantiated, it gets added to the list
    all_magazines = []

    # This is a constructor method that initializes a new Magazine instance with name (of the magazine) and category (of the magazine) and validates the input given by the user or during test implementation
    # it initializes the the name attribute to None which ensures that the property setter is used when assinging it
    # the  self.name = name  assigns the name using the property setter which then validates the input
    # self.category = category assigns the category using the property setter which then validates the input
    # then adds the new instance to the list of magazines 
    
    def __init__(self, name, category):
        self._name = None  
        self.name = name  
        self.category = category
        Magazine.all_magazines.append(self)

    # this is a property getter method that allows external access to the name attribute which is set as private
    # when one accesses the name of the magazine e.g magazine.name, the method gets called
    
    @property
    def name(self):
        return self._name
    
    # this is a property setter method that validates and sets the value of name attribute, it ensures it is a string
    # and it also ensures the length is between 2 and 16 characters, inclusive
    # if valid the name is assigned to self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be between 2 and 16 characters, inclusive")
        self._name = name

    # this allows access to the private category attribute
    
    @property
    def category(self):
        return self._category
    
    # this is a property setter method that validates and sets the value of category attribute, it ensures it is a string
    # and it also ensures the length is not empty
    # assigns the input to self._category if valid

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise Exception("Category must be a string")
        if len(category) <= 0:
            raise Exception("Category must be longer than 0 characters")
        self._category = category
    
    # this method returns a list of articles published in the given magazine
    # it loops through the Articles.all which has all the Article instances
    # for the given article encountered it checks if the magazine matches the current instance self e.g magazine.articles()
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    

    # this method returns a list of authors contributing to the given magazine
    # it gets the list of articles for this magazine using self.articles()
    # then it extracts the author attribute from each article and adds them to a set to remove duplicates and converts it back to a list, called by magazine.contributors()
    
    def contributors(self):
        return list(set([article.author for article in self.articles()]))
    

    # returns a list of all the article titles published in this magazine
    # it first gets the list of articles using self.articles() 
    # if no articles exists returns None otherwise returns title of each article
    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]
    
    # this method identifies and returns authors who have contributed to more than 2 articles to this magazine
    # it loops through all the articles in this magazine using self.articles()
    # it then counts how many articles the author has cointributed using dictionary author_count
    # it then filters the authors with contributions greater than 2
    # it returns the qualifying authors, or None if there are no authors contributing more than 2 articles
    
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        
        qualifying_authors = [author for author, count in author_count.items() if count > 2]
        return qualifying_authors if qualifying_authors else None
    
    # this class method identifies and returns the magazine with the most articles
    # it first checks if there are any articles in Article.all
    # if not, it returns None
    # if there are articles, it iterates through Article.all and keeps track of the magazine with the maximum count
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        
        magazine_count = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_count[magazine] = magazine_count.get(magazine, 0) + 1
        
        return max(magazine_count.items(), key=lambda x: x[1])[0]



# In this class, it is used to represent an article.
# Each article has its own title, author, and magazine
# keeps track of all articles created, validates inputs and provides access to related properties

class Article:

    # class attribute keeping track of all Article instances
    # when a Article object is instantiated, it gets added to the list
    all= []

    # This is a constructor method that initializes a new Article instance with title, author, and magazine and validates the input given by the user or during test implementation
    # it ensures that the author must be an instance of the class Author class
    # it ensures that the magazine must be an instance of the class Magazine
    # it also ensures that title is between 5 and 50 characters long

    # if all validations pass they are assigned to their respective attributes
    # the article instance is then added to Article.all list


   
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters, inclusive")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    # this is a read only property that allows external access to the private _title attribute
    # when one calls article.title, the method returns articles title
    
    @property
    def title(self):
        return self._title
    
    # this is a getter property that allows external access to the private _author attribute
    # when one calls article.author, this getter method returns articles author
    
    @property
    def author(self):
        return self._author
    
    # this is a setter method which validates and sets the article's author
    # if the author is an instance of Author class, it assigns the author to self._author, otherwise it raises an exception
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        self._author = author
    
    # this is a getter property that allows external access to the private _magazine attribute
    # when one calls article.magazine, this getter method returns article magazine associated with that article
    
    @property
    def magazine(self):
        return self._magazine
    
    # this is a setter method which validates and sets the article's magazine
    # if the magazine is an instance of Magazine class, it assigns the magazine to self._magazine, otherwise it raises an exception
    
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        self._magazine = magazine