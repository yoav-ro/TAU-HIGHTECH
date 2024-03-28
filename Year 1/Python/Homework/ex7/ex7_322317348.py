""" Exercise #7. Python Programming."""

#########################################
# Question 1 - do not delete this comment
#########################################


class ArtDisplay:

    def __init__(self, name, date, art_type, preserving_date, worth):
        self.name = name
        self.date = date
        self.art_type = art_type
        self.preserving_date = preserving_date
        if worth <= 0:
            raise ValueError("Invalid worth value")
        else:
            self.worth = worth

    def change_preserving_date(self, new_date):
        self.date = new_date


newArt = ArtDisplay("test", "22.1.1990", "painting", "22.2.1990", 1)
print(newArt.worth)

#########################################
# Question 2 - do not delete this comment
#########################################
# class MuseumSubscriber:

#     def __init__(self, name, ticket_type, favorites):

#     def set_entry(self):

#     def get_favorites(self):


##########################################
# Questions 3 - do not delete this comment
##########################################

# class Museum:

#     def __init__(self,art_displays):

#     def get_art_displays(self):

#     def get_art_display(self,name):

#     def add_art_display(self,artDisplay):

#     def add_subscriber(self, subscriber):

#     def change_preserving_date(self, name , new_date):

#     def get_total_worth(self):

#     def subscriber_entry(self,name):

#     def find_loved_disp(self):

#########################################
# Question 4 - do not delete this comment
#########################################

# def create_museum(filename):


# use the following code to test your code:
# museum=create_museum('museum.csv')
# print (museum)
