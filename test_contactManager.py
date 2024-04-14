import unittest
from contact_manager import ContactManager

class testContactManager(unittest.TestCase):

    def setUp(self):
        self.contacts = ContactManager()
        contact1 = self.contacts.add_contact("Jim", 999999999)

    def test_displayContacts(self):
        self.assertEqual(self.contacts.display_contacts(), "Name: Jim, Phone Number: 999999999")
        self.contacts.remove_contact("Jim")
        self.assertEqual(self.contacts.display_contacts(), "No contacts found.")
                         
    def test_addContact(self):
        self.assertEqual(self.contacts.add_contact("Sopo", 574827827), "Contact 'Sopo' added successfully.")
        self.assertEqual(self.contacts.add_contact("Sopo", 574827827), "Contact 'Sopo' already exists.")

    def test_searchContact(self):
        self.assertEqual(self.contacts.search_contact("Jim"),"Name: Jim, Phone Number: 999999999" )
        self.assertEqual(self.contacts.search_contact("Pam"),"Contact 'Pam' not found." )

    def test_removeContact(self):
        self.assertEqual(self.contacts.remove_contact("Jim"), "Contact 'Jim' removed successfully.")
        self.assertEqual(self.contacts.remove_contact("Jim"), "Contact 'Jim' not found.")

if __name__ == "__main__":
    unittest.main()


