import datetime

######################################################################
## Reader Class
######################################################################
class Reader():
    def __init__(self, username:str, email:str, gender:str, dob:datetime.datetime, password:str) -> None:
        self.username = username
        self.email = email
        self.gender = gender
        self.dob = dob
        self.password = password
        self.library_books = []
        self.library_bookclubs = []
        self.my_wish_list = []
        self.notifications = []
        self.favorite_genres = []

    def create_comment(self):
        #create a Comment class and add data to Comment database
        pass

    def create_wish(self):
        #create a Wish class and add data to Wish database
        pass

    def delete_wish(self):
        #remove wish from Wish database
        pass

    def add_book_to_library(self):
        #add data to library database
        pass

    def remove_book_from_library(self):
        #remove data from library database
        pass

    def join_bookclub(self):
        #add data to bookclub_members database
        pass

    def quit_bookclub(self):
        #remove data from bookclub_members database
        pass

    def write_feedback(self):
        #create Feedback class and add data to Feedback database
        pass

######################################################################
## Book Class
######################################################################
class Book():
    def __init__(self, title:str, author:str, genre:str, summary:str) -> None:
        #self.book_id = generate_book_id()
        #self.book_cover
        self.book_title = title
        self.book_author = author
        self.book_genre = author
        self.book_summary = summary
        self.no_of_readers = 0
        self.bookclubs = []
        self.comments = []

    def  generate_bookclubs(self):
        #create 4/5 Bookclub class and add data to Bookclub database
        pass

    def display_comments(self):
        #view data from Comments database
        pass 
    ## not decided how to renew bookclubs yet
    # def add_bookclub(self):
    #     pass

    # def delete_bookclub(self):
    #     pass

######################################################################
## BookClub Class
######################################################################
class BookClub():
    def __init__(self, bookID:str, close_date:datetime.datetime) -> None:
        #self.bookclub_id = generate_bookclub_id
        self.book_id = bookID
        self.close_date = close_date
        self.end_date = self.close_date + datetime.timedelta(days=7)
        self.members =[]

    # def add_member(self):
    #     pass

    # def remove_member(self):
    #     pass

    # def add_comment(self):
    #     pass

    def display_comments(self):
        #view data from Comment database
        pass

######################################################################
## Comment Class
######################################################################

class Comment():
    def __init__(self, type:str, type_id:str, commenter:str, comment:str) -> None:
        #self.comment_id = generate_comment_id()
        self.book_or_bookclub = type
        self.book_or_bookclub_ID = type_id
        self.commenter = commenter
        self.comment = comment
        self.commented_time = datetime.datetime.now()

######################################################################
## Wish Class
######################################################################
class Wish():
    def __init__(self, wisher:str, title:str, author:str, description:str) -> None:
        #self.wish_id = generate_wish_id
        self.wisher = wisher
        self.wish_title =  title
        self.wish_author = author
        self.wish_description = description
        self.wish_status = False

######################################################################
## Notification Class
######################################################################
class Notification():
    def __init__(self, reciever:str, message:str) -> None:
        self.reciever = reciever
        self.message = message
        self.seen = False

######################################################################
## Feedback Class
######################################################################
class Feedback():
    def __init__(self, reader:str, feedback:str) -> None:
        self.respondent = reader
        self.feedback = feedback
        self.read = False

