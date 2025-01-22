class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.add_article(self)
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title

    def __setattr__(self, name, value):
        if name == "title" and hasattr(self, "_title"):
            return  # Ignore invalid value
        if name == "title" and not isinstance(value, str):
            return  # Ignore invalid value
        super().__setattr__(name, value)

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 1:
            raise ValueError("Name must be at least one character")
        
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def __setattr__(self, name, value):
        if name == "name" and hasattr(self, "_name"):
            return  # Ignore invalid value
        super().__setattr__(name, value)

    def articles(self):
        return self._articles

    def add_article(self, article):
        self._articles.append(article)

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        # if not isinstance(name, str):
        #     raise ValueError("Name must be a string")
        # if not (2 <= len(name) <= 16):
        #     raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category) < 1:
            raise ValueError("Category must be at least one character")
        self.name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return  # Ignore invalid value
        if not (2 <= len(value) <= 16):
            return  # Ignore invalid value
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return  # Ignore invalid value
        if len(value) < 1:
            return  # Ignore invalid value
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        contributing_authors = [author for author in set(authors) if authors.count(author) > 2]
        return contributing_authors if contributing_authors else None