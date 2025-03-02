from classes import Person

def test_get_full_name():
  """Test to make sure that the function runs properly"""
  person = Person("jane", "doe", 20, "female")

  assert person.get_full_name() == "Jane Doe"

def test_get_full_name_with_none():
  person = Person("jane", None, 30, "female")

  assert person.get_full_name() == "Jane"