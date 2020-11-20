class Article:
   '''
   Article class to define News Objects
   '''
   def __init__(self,author,title,description,url,urltoImage,pusblishedAt,content):
       self.author=author
       self.title=title
       self.description=description
       self.url=url
       self.urlImage=urlImage
       self.publishedAt= publishedAt
       self.content=content
 
 
class Sources:
   '''
   Sources class to define Source Objects
   '''
 
   def __init__(self,id,name,description,url,category,country):
       self.id=id
       self.name=name
       self.description=description
       self.url=url
       self.category=category
       self.country=country
