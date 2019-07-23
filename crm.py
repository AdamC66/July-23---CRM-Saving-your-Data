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
    first_name = input("Please enter contact's first name: ").lower()
    last_name = input("Please enter contact's last name: ").lower()
    email = input("Please enter contact's email address: ").lower()
    note = input("Please enter a note for the contact, if desired: ")
    if note == None:
      note = " "    
    Contact.create(first_name, last_name, email,note)

  def modify_existing_contact(self):
    if len(Contact.list_of_contacts) == 0:
      print("Error, no contacts to modify")
    else:
      id_to_update = int(input("Enter the ID of the contact you would like to update: "))
      attribute_to_update = input("Enter the attribute you would like to change: ")
      value_to_update_to = input("Enter the new value")
      Contact.list_of_contacts[id_to_update-1].update(attribute_to_update, value_to_update_to)
 
  def delete_contact(self):
    if len(Contact.list_of_contacts) == 0:
      print("Error, no contacts to delete")
    else:
      id_to_delete = int(input("please enter the contact id you would like to delete: "))
      Contact.delete(id_to_delete-1)

  def display_all_contacts(self):
    all_contacts = Contact.all()
    for item in all_contacts:
      print(item)
    print(" ")

  def search_by_attribute(self):
    if len(Contact.list_of_contacts) == 0:
      print("Error, no contacts to search")
    else:
      attribute = input("Enter the attribute you would like to search: ").lower()
      value = input("Enter the value you would like to search for: ").lower()
      if attribute == "id":
        value = int(value)
      print(Contact.find_by(attribute,value))
      print(" ")

crm = CRM()
#crm.main_menu()

# Contact.create("jj", "ben", 'ff', 'fff')
# crm.search_by_attribute()
# print(Contact)