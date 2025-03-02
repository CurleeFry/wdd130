class Person:
  """A representation of a person.
    Attributes: 
        given_name (str): The first name of a person
        family_name (str): The last name of a person
        age (int): A numerical representation of the age
        gender (str): Lowecase fully typed gender
        """
  def __init__(self, given_name, family_name, age, gender):
    self.given_name = given_name
    self.family_name = family_name

    self.age = age
    self.gender = gender

  def get_full_name(self):
    """Get the person's full name, which is the given name and family name."""

    if self.given_name is None:
        return self.family_name
    
    if self.family_name is None:
       return self.given_name

    return f"{self.given_name} {self.family_name}"

person1 = Person("John", "Smith", 20, "male")
person2 = Person("Jane", "Doe", 21, "female")

print(person1.get_full_name())
print(person2.get_full_name())

