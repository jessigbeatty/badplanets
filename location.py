class Location:
# generic class for all locations. just planets right now, eventually orbits, asteroids, etc

    def __init__(self, title, description, minerals):
        self.title = title
        self.description = description
        self.minerals = minerals

    def __str__(self):
        return f"Location(title={self.title}, minerals={self.minerals})"

    def show_description(self):
        # prints nice-ish looking description of location
        print(f"You are on {self.title}. {self.description} \n")
        print(f"Minerals are {self.minerals}.\n")

    def get_mined(self, amount):
        # decreases available minerals, prints messages 
        if self.minerals >= amount:
            print(f"You mine {amount} minerals from {self.title.lower()}.")
            self.minerals -= amount
            print(f"{self.title} now has {self.minerals} minerals.\n")
        else:
            print(f"You tried to mine {amount} but {self.title.lower()} only has {self.minerals}. Try a smaller amount.\n")

# define game world. definitely a better place to do this, maybe its own file game_world?
## alpha = Location("a rocky planet", "It's rocky and bad. This is coming from the location class.", 1000)
## beta = Location("a desert planet", "It's sandy and bad. This is coming from the location class", 500)

