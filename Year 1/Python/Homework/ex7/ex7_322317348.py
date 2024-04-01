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
class Museum:

    def __init__(self, art_displays):
        self.art_displays = art_displays
        self.subscribers = []

    def get_art_displays(self):
        return self.art_displays

    def get_art_display(self, name):
        return list(filter(lambda display: display.name == name, self.art_displays))[0]

    def get_subscriber(self, name):
        return list(
            filter(lambda subscriber: subscriber.name == name, self.subscribers)
        )[0]

    def add_art_display(self, artDisplay):
        self.art_displays.append(artDisplay)

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def change_preserving_date(self, name, new_date):
        displayToChange = self.get_art_display(name)
        displayToChange.change_preserving_date(new_date)
        return None

    def get_total_worth(self):
        worthSum = 0
        for display in self.art_displays:
            worthSum += display.worth
        return worthSum

    def subscriber_entry(self, name):
        self.get_subscriber(name).set_entry()

    def find_loved_disp(self):
        loveDict = {display.name: 0 for display in self.art_displays}
        for sub in self.subscribers:
            for display in sub.favorites:
                loveDict[display.name] += 1

        maxLove = max(loveDict.values())
        resList = []

        for display in loveDict:
            if loveDict[display] == maxLove:
                resList.append(display)

        return resList
    
#########################################
# Question 4 - do not delete this comment
#########################################

def create_museum(filename):
    path = "Year 1\Python\Homework\ex7"
    try:
        f = open(path + "/" + filename, "r")
        dataRows = f.readlines()
        artList = []
        subList = []
        totalWorth = 0
        for row in dataRows:
            data = row.split(",")
            if data[0] == "artDisplay":
                artWorth = int(data[5])
                newDisplay = ArtDisplay(data[1], data[2], data[3], data[4], artWorth)
                totalWorth += artWorth
                artList.append(newDisplay)
            elif data[0] == "subscriber":
                newSub = MuseumSubscriber(
                    data[1],
                    data[2],
                    [
                        artList[int(data[3]) - 1],
                        artList[int(data[4]) - 1],
                        artList[int(data[5]) - 1],
                    ],
                )
                subList.append(newSub)
        print("This museum's worth is %s" % totalWorth)
        return Museum(artList)

    except IOError:
        print("Unable to load %s due to an IO Error" % (filename))
        f.close()
