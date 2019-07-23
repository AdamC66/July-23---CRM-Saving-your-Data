class Contact:
  list_of_contacts = []
  next_id = 1
  def __init__(self,first_name, last_name, email, note,id):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note
    self.id = id
    Contact.next_id += 1
  
  def __str__(self):
    return ("ID: {}, First Name: {}, Last Name: {}, Email: {}, Note: {}".format(self.id, self.first_name.capitalize(), self.last_name.capitalize(), self.email, self.note))

  def __repr__(self):
    return self.__str__()

  @classmethod
  def create(cls, first_name, last_name, email,note):
    """This method should call the initializer,
    store the newly created contact, and then return it
    """
    new_contact = Contact(first_name, last_name,email, note, cls.next_id)
    cls.list_of_contacts.append(new_contact)
    return new_contact

  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""
    return cls.list_of_contacts
    
  @classmethod
  def find(cls, id):
    """ This method should accept an id as an argument
    and return the contact who has that id
    """
    for contact in cls.list_of_contacts:
      if contact.id == id:
        return contact
      else:
        continue

  def update(self, attribute_to_update, new_value):
    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """
    if attribute_to_update.lower() == "first_name":
      self.first_name = new_value
    elif attribute_to_update.lower() == "last_name":
      self.last_name = new_value
    elif attribute_to_update.lower() == "email":
      self.email = new_value
    elif attribute_to_update.lower() == "note":
      self.note = new_value


  @classmethod
  def find_by(cls, attribute, attribute_value):
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """
    search_list = []
    for contact in cls.list_of_contacts:
      if attribute.lower() == "first_name":
        if contact.first_name == attribute_value:
          search_list.append(contact)
      elif attribute.lower() == "last_name":
        if contact.last_name == attribute_value:
          search_list.append(contact)
      elif attribute.lower() == "email":
        if contact.email == attribute_value:
          search_list.append(contact)
      elif attribute.lower() == "note":
        if contact.note == attribute_value:
          search_list.append(contact)
    return(search_list)

  @classmethod
  def delete_all(cls):
    """This method should delete all of the contacts"""
    cls.list_of_contacts.clear

  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

  def delete(index_to_delete):
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """
    Contact.list_of_contacts.pop(index_to_delete)
  # Feel free to add other methods here, if you need them.

# Contact.create()
# Contact.create()
# Contact.create()


# Contact.list_of_contacts[0].update("email", "adam.cote66@gmail.com")
# print(Contact.all())
# Contact.list_of_contacts[2].delete()
# print(Contact.all())
# print(Contact.list_of_contacts[1].full_name())
