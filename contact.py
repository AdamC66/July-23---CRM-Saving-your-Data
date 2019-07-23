from peewee import SqliteDatabase, Model, CharField, TextField, Update, Delete, Select

db = SqliteDatabase('crm.sqlite3')


class Contact(Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField()
  note = TextField()

  class Meta:
      database = db

  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


  # Feel free to add other methods here, if you need them.
db.connect()
db.create_tables([Contact])
# Contact.create()
# Contact.create()
# Contact.create()


# Contact.list_of_contacts[0].update("email", "adam.cote66@gmail.com")
# print(Contact.all())
# Contact.list_of_contacts[2].delete()
# print(Contact.all())
# print(Contact.list_of_contacts[1].full_name())
