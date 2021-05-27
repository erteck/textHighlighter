class Author:
    def __init__(self, name, email, gender):
      self.__name = f'{name}'
      self.__email = f'{email}'
      self.__gender = f'{gender}'
      
    @property
    def name(self):
      return self.__name
    
    @property
    def email(self):
      return self.__email
      
    @property
    def gender(self):
      return self.__gender
    
    @email.setter
    def email(self, email):
      self.__email = f'{email}'
    
    def __repr__(self):
      return f'Author[name={self.__name}, email={self.__email}, gender={self.__gender}]'
      

class Book:
    __catalogue = []
    
    def __init__(self, name, authors, price, qty):
        Book.__catalogue.append(self)
        self.__name = f'{name}'
        self.__authors = authors
        self.__price = float(price)
        self.__qty = int(qty)
        
    @property
    def name(self):
      return self.__name
    
    @property
    def authors(self):
      return self.__authors
    
    @property
    def price(self):
      return self.__price
    
    @property
    def qty(self):
      return self.__qty
    
    @price.setter
    def price(self, price):
      self.__price = price
    
    @qty.setter
    def qty(self, qty):
      self.__qty =qty
    
    def __repr__(self):
      return f'Book[name={self.__name}, authors={self.__authors}, price={self.__price}, qty={self.__qty}]'
  
    def author_names(self):
      authorNames = []
      for author in self.__authors:
          authorNames.append(author.name) 
      return ', '.join(authorNames)
    
    def catalogue():
      return Book.__catalogue
      
      