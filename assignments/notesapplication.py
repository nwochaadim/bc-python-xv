class NotesApplication(object):
	def __init__(self, author, notes=[]):
		self.author = author
		if type(notes)==str and notes!='':
			self.notes = [notes]
		elif type(notes)==type([]):
			self.notes = notes
		else:
			self.notes = []


	def create(self, note_content):
		if len(note_content)>0:

			self.notes.append(note_content)


	def list(self):
		if len(self.notes)>0:

			for k,v in enumerate(self.notes):
				print("\n\nNOTE_ID: %d" %(k))
				print(v)
				print("\n")
				print("By Author: %s\n" %self.author)

		return self.notes

	def get(self, note_id):
		index_length = len(self.notes) -1
		if note_id<0 or note_id > index_length:
			return "Invalid Index"
		else:
			return self.notes[note_id]

	def search(self, search_text):
		
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
		note_length = len(self.notes) -1
		if note_id<0 or note_id > note_length:
			print "\nInvalid Index"
			return True
		else:
			
			del self.notes[note_id]
			print("\n Note with index %d has been successfully deleted! Taking you back to main menu" % note_id)

	def edit(self, note_id, new_content):
		note_length = len(self.notes) -1
		if note_id<0 or note_id > note_length:
			print "\nInvalid Index"
			return True
		else:
			print "\n Changes Committed Succesfully!"
			self.notes[note_id] = new_content

