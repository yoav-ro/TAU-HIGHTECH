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
        self.preserving_date = new_date


#########################################
# Question 2 - do not delete this comment
#########################################
class MuseumSubscriber:

    def __init__(self, name, ticket_type, favorites):
        self.name = name
        if ticket_type == "1":
            self.entries_left = 1
        elif ticket_type == "5":
            self.entries_left = 5
        else:
            self.entries_left = ticket_type

        self.favorites = favorites

    def set_entry(self):
        if type(self.entries_left) == str:
            print("Welcome subscriber!")
        elif self.entries_left == 0:
            print("Please renew your subscription")
        else:
            self.entries_left = self.entries_left - 1
            print("Welcome! %s entries left" % (self.entries_left))

    def get_favorites(self):
        return self.favorites


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
