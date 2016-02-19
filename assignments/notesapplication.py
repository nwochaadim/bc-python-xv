#still working on it but right now, the application is fully interactive
class NotesApplication(object):
	def __init__(self, author, notes=[]):
		self.author = author
		self.notes = notes

	def create(self, note_content):
		self.notes.append(note_content)

	def list(self):
		for k,v in enumerate(self.notes):
			print("\n\nNOTE_ID: %d" %(k))
			print(v)
			print("\n")
			print("By Author: %s\n" %self.author)

	def get(self, note_id):

		return self.notes[note_id]

	def search(self, search_text):
		print("Showing results for search %s" % search_text)
		search_notes = filter(lambda x: search_text in x, self.notes)
		for id, note in enumerate(search_notes):
			print("NOTE_ID: %s" % id)
			print(note)
			print("\nBy Author: %s\n" %self.author)

	def delete(self, note_id):
		del self.notes[note_id]

	def edit(self, note_id, new_content):
		self.notes[note_id] = new_content

	

