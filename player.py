class Player:
  # idk what i'm doing aaaa

  def __init__(self, current_location, minerals, energy):
   self.current_location = current_location
   self.minerals = minerals
   self.energy = energy

  def show_status(self):
  # prints resource amounts
    print(f"You have {self.minerals} minerals. You have {self.energy} energy.\n")

  def mine(self):
  # takes amount to mine as input, calls mine function of location, increases player minerals
    amount = input("How much will you mine? ")
    self.current_location.get_mined(int(amount))
    if int(amount) <= int(self.current_location.minerals):
      self.minerals += int(amount)

  def breathe(self):
  # increase player energy by set amount breath_amt
    breath_amt = 50
    self.energy += breath_amt
    print(f"Your dark energy condenser hums quietly. You have gained {breath_amt} energy. Your energy is now {self.energy}.\n")

  def move(self, destination):
  # sets player location
    self.current_location = destination
