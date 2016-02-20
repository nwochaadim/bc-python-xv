import unittest
from notesapplication import NotesApplication

class NotesApplicationTest(unittest.TestCase):

		def test_notes_instance(self):
			notes = NotesApplication('Author')
			self.assertIsInstance(notes, NotesApplication, msg='The object should be an instance of the "NotesApplication" class')


		def test_notes_instance_with_empty_string(self):
			notes = NotesApplication('Author', '')
			length = len(notes.notes)
			self.assertEqual(length, 0, msg='No String was passed in, A note is not to be created')

		def test_notes_instance_with_string(self):
			notes = NotesApplication('Author', 'Test Content')
			length = len(notes.notes)
			self.assertEqual(length, 1, msg='A new note was not created')

		def test_notes_instance_with_list(self):
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

		def test_notes_create_4(self):
			notes = NotesApplication('Author', 'Test Content1')
			notes.create("Test Content2")
			notes.create("Test Content3")
			notes.create("Test Content4")
			length = len(notes.notes)
			self.assertEqual(length, 4, msg='A new note was not created')

		def test_notes_create_5(self):
			notes = NotesApplication('Author', ['Test Content1', 'Test Content2', 'Test Content3'])
			notes.create("Test Content4")
			notes.create("Test Content5")
			notes.create("Test Content6")
			length = len(notes.notes)
			self.assertEqual(length, 6, msg='A new note was not created')

		def test_retrieve_notes_valid_index(self):
			notes = NotesApplication('Author')
			notes.create("Test Content")
			note = notes.get(0)
			self.assertEqual(note, "Test Content", msg='Retrieving a note with a valid index should return the correct note')

		def test_retrieve_notes_invalid_index(self):
			author_notes = NotesApplication('New Author', "Test Content1")
			author_note = author_notes.get(1)
			self.assertEqual(author_note, "Invalid Index", msg='Retrieving a note with Invalid Index should fail')

		def test_retrieve_notes_invalid_index(self):
			author_notes = NotesApplication('New Author', "Test Content1")
			author_note = author_notes.get(-10)
			self.assertEqual(author_note, "Invalid Index", msg='Retrieving a note with Invalid Index should fail')

		def test_list_notes(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			notes_list = author_notes.list()
			self.assertListEqual(notes_list, ["Test Content1", "Test Content2", "Test Content3"], msg='list() should return all created notes')

		def test_list_notes1(self):
			author_notes = NotesApplication('New Author', [])
			notes_list = author_notes.list()
			self.assertListEqual(notes_list, [], msg='list() should return empty list when not instantiated')

		def test_search_notes(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			notes_list = author_notes.search("Content")
			self.assertListEqual(notes_list, ["Test Content1", "Test Content2", "Test Content3"], msg='search should return all notes with search string')

		def test_search_notes1(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			notes_list = author_notes.search("Content4")
			self.assertListEqual(notes_list, [], msg='search should return an empty array when no text is found in any notes')

			
		def test_delete_valid_index(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			author_notes.delete(2)
			notes_length = len(author_notes.notes)
			self.assertEqual(notes_length, 2, msg='Delete should reduce the size of the list')

		def test_delete_invalid_index(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			delete_result = author_notes.delete(4)
			self.assertTrue(delete_result, msg='Delete should return True for a wrong index')

		def test_delete_invalid_index1(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			delete_result = author_notes.delete(-4)
			self.assertTrue(delete_result, msg='Delete should return True for a negative index')

		def test_edit_valid_index(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			author_notes.edit(1, "Test Content4")
			notes_list = author_notes.list()
			self.assertListEqual(notes_list, ["Test Content1", "Test Content4", "Test Content3"], msg='Edit should alter supplied index in the notes list')


		def test_edit_invalid_index(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			author_notes.edit(3, "Test Content4")
			notes_result = author_notes.list()
			self.assertTrue(notes_result, msg='Delete should return True for Invalid Index')

		def test_edit_invalid_index1(self):
			author_notes = NotesApplication('New Author', ["Test Content1", "Test Content2", "Test Content3"])
			author_notes.edit(-3, "Test Content4")
			notes_result = author_notes.list()
			self.assertTrue(notes_result, msg='Delete should return True for a negative Invalid Index')




if __name__ == '__main__':
    unittest.main()