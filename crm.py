from contact import Contact

class CRM:

  def main_menu(self):
    while True: # repeat indefinitely
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)

  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')

  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      exit("Goodbye")
    else:
      print("selection invalid")
  def add_new_contact(self):
    first_name = input("Please enter contact's first name: ")
    last_name = input("Please enter contact's last name: ")
    email = input("Please enter contact's email address: ").lower()
    note = input("Please enter a note for the contact, if desired: ")
    contact = Contact.create(
      first_name=first_name,
      last_name=last_name,
      email=email,
      note=note
    )
  def modify_existing_contact(self):
    id_to_modify = input("enter the ID of the contact to be modified: ")
    # contact_to_update = Contact.get(Contact.id == id_to_modify)
    attribute_to_modify = input("enter the attribute you would like to modify: ")
    new_value = input("enter the new value: ")
    if attribute_to_modify == 'first name':
      q = (Contact.update({Contact.first_name : new_value}).where(Contact.id == id_to_modify))
      q.execute()
    elif attribute_to_modify == 'last name':
      q = (Contact.update({Contact.last_name : new_value}).where(Contact.id == id_to_modify))
      q.execute()
    elif attribute_to_modify == 'email':
      q = (Contact.update({Contact.email : new_value}).where(Contact.id == id_to_modify))
      q.execute()
  def delete_contact(self):
    id_to_delete = int(input('Please enter the ID of the contact you would like to delete: '))
    contact = Contact.get(Contact.id == id_to_delete)
    contact.delete_instance()
    
  def display_all_contacts(self):
    all_contacts = Contact.select()
    for contact in all_contacts:
      print("ID: {}, Name: {} {}, Email: {}, Note: {}".format(contact.id, contact.first_name.capitalize(), contact.last_name.capitalize(), contact.email, contact.note))
  
  def search_by_attribute(self):
    attribute = input('Please enter the attribute you would like to search: ').lower()
    value = input('Please enter the value you would like to search for: ').capitalize()
    if attribute == 'first name':
      result = Contact.get(Contact.first_name == value)
    elif attribute == 'last name':
      result = Contact.get(Contact.last_name == value)
    elif attribute == 'email':
      result = Contact.get(Contact.email == value)
    print(result)

    print("ID: {}, Name: {} {}, Email: {}, Note: {}".format(result.id, result.first_name.capitalize(), result.last_name.capitalize(), result.email, result.note))
    # for contact in result:
    #   print("ID: {}, Name: {} {}, Email: {}, Note: {}".format(contact.id, contact.first_name.capitalize(), contact.last_name.capitalize(), contact.email, contact.note))
crm = CRM()
crm.main_menu()

# Contact.create("jj", "ben", 'ff', 'fff')
# crm.search_by_attribute()
# print(Contact)