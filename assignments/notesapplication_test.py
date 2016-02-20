#still working on it but right now, the application is fully interactive
import unittest
from notesapplication import NotesApplication

class NotesApplicationTest(unittest.TestCase):

		def test_notes_instance(self):
			notes = NotesApplication('Author')
			self.assertIsInstance(notes, NotesApplication, msg='The object should be an instance of the "NotesApplication" class')

		def test_notes_with_empty_string(self):
			notes = NotesApplication('Author', '')
			length = len(notes.notes)
			self.assertEqual(length, 0, msg='No String was passed in, A note is not to be created')

		def test_notes_create_1(self):
			notes = NotesApplication('Author', 'Test Content')
			length = len(notes.notes)
			self.assertEqual(length, 1, msg='A new note was not created')

		def test_notes_create_2(self):
			notes = NotesApplication('Author', ['Test Content 1', 'Test Content 2', 'Test Content 3'])
			length = len(notes.notes)
			self.assertEqual(length, 3, msg='A new note was not created')

		def test_create_with_empty_string(self):
			notes = NotesApplication('Author')
			notes.create('')
			length = len(notes.notes)
			self.assertEqual(length, 0, msg='No String was passed in, A note is not to be created')


		def test_notes_create_3(self):
			notes = NotesApplication('Author')
			notes.create("Test Content")
			length = len(notes.notes)
			self.assertEqual(length, 1, msg='A new note was not created')

		def test_retrieve_notes_valid_index(self):
			notes = NotesApplication('Author')
			notes.create("Test Content")
			note = notes.get(0)
			self.assertEqual(note, "Test Content", msg='Retrieving a note with note_id fails')

		def test_retrieve_notes_invalid_index(self):
			author_notes = NotesApplication('New Author', "Test Content1")
			author_note = author_notes.get(1)
			self.assertEqual(author_note, "Invalid Index", msg='Retrieving a note with Invalid Index should fail')

		def test_list_notes(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			notes_list = author_notes.list()
			self.assertListEqual(notes_list, ["Test Content1", "Test Content2", "Test Content3"], msg='list() should return all created notes')

		def test_search_notes(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			notes_list = author_notes.search("Content")
			self.assertListEqual(notes_list, ["Test Content1", "Test Content2", "Test Content3"], msg='search should return all notes with search string')




if __name__ == '__main__':
    unittest.main()