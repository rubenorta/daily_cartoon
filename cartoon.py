class Cartoon:

    def __init__(self,title,image,url,publisher,author,date):
        self.title = title
        self.image = image
        self.url = url
        self.publisher = publisher
        self.author = author
        self.date = date

    def __str__(self):
        s = "De " + self.author + "@" + self.publisher + "\n"
        s = s + self.title + " / " + self.date  + "\n"
        s = s + " URL " + self.url + "\n SRC " + self.image  + "\n"
        return s


