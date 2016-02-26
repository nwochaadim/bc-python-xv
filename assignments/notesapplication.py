class NotesApplication(object):
	"""
		Base Class for Creating NotesApplication Objects

		Args:
			author(string): The First Parameter of the NotesApplication Class specifying the name of the Author
			notes(optional[list]): The Second optional Parameter specifying a pre-exisiting note

	"""
	def __init__(self, author, notes=[]):
		self.author = author
		if type(notes)==str and notes!='':
			self.notes = [notes]
		elif type(notes)==type([]):
			self.notes = notes
		else:
			self.notes = []


	def create(self, note_content):
		"""
			Method creates a new Note for a NotesApplication Object

			Args:
				note_content(string): Specifies the note to create
		"""
		if len(note_content)>0:

			self.notes.append(note_content)


	def list(self):
		"""
			Method lists all notes in a NotesApplication Object

			Returns:
				list: List of All notes
		"""
		if len(self.notes)>0:

			for k,v in enumerate(self.notes):
				print("\n\nNOTE_ID: %d" %(k))
				print(v)
				print("\n")
				print("By Author: %s\n" %self.author)

		return self.notes

	def get(self, note_id):
		"""
			Method retrieves a specific note in a NotesApplication Object

			Args:
				note_id(int): Specifies the index of the note to retrieve

			Returns:
				str: The specific note retrieved
		"""
		index_length = len(self.notes) -1
		if note_id<0 or note_id > index_length:
			return "Invalid Index"
		else:
			return self.notes[note_id]

	def search(self, search_text):

		"""
			Method searches for a specific string in the NotesApplication Object

			Args:
				search_text(str): Specifies search string

			Returns:
				list: List of notes matching the search text
		"""
		
		search_notes = filter(lambda x: search_text in x, self.notes)
		if len(search_notes)==0:
			print("\nNo results for  %s" % search_text)
			return []
		else:
			print("\nShowing results for search %s" % search_text)
			for id, note in enumerate(search_notes):
				print("NOTE_ID: %s" % id)
				print(note)
				print("\nBy Author: %s\n" %self.author)
			return search_notes

	def delete(self, note_id):
		"""
			Method deletes a specific note in the NotesApplication Object

			Args:
				note_id(int): Specifies the Id of the note to delete

			Returns:
				bool: Returns True when Id is Invalid
		"""
		note_length = len(self.notes) -1
		if note_id<0 or note_id > note_length:
			print "\nInvalid Index"
			return True
		else:
			
			del self.notes[note_id]
			print("\n Note with index %d has been successfully deleted! Taking you back to main menu" % note_id)

	def edit(self, note_id, new_content):
		"""
			Method deletes a specific note in the NotesApplication Object

			Args:
				note_id(int): Specifies the Id of the note to delete
				new_content(str): The new string to replace in the NotesApplication Object

			Returns:
				bool: Returns True when Id is Invalid
		"""
		note_length = len(self.notes) -1
		if note_id<0 or note_id > note_length:
			print "\nInvalid Index"
			return True
		else:
			print "\n Changes Committed Succesfully!"
			self.notes[note_id] = new_content

