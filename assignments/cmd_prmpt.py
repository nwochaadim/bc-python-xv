#still working on it but right now, the application is fully interactive
from notesapplication import NotesApplication

name = raw_input("Please input Your Name: ")

notes = NotesApplication(name)
inp = ""
while inp!= "q":
	response = raw_input("Enter c to create a new Note or q to quit ")
	if response=="c":
		notes_content = raw_input("\n\nPlease Enter your note: ")
		notes.create(notes_content)

		print("\n\nNotes have been saved successfully")
		print("\nPress m to return to menu")
		print("\nPress s to search for a specific string")
		print("\nPress r to retrieve a specific note")
		print("\nPress d to delete a specific note")
		print("\nPress e to edit a specific note")
		print("\nPress l to retrieve all notes: ")

		res = raw_input("\nEnter Choice: ")

		if(res=="l"):
			notes.list()
		elif res=="m":
			continue
		elif res=="s":
			search_text = raw_input("Please enter search text: ")
		elif res=="r":
			search_text = raw_input("Please enter index of note to retrieve: ")
			while not search_text.isdigit():
				search_text = raw_input("Please enter valid index of note to retrieve: ")
				search_text = int(search_text)
				notes.search(search_text)
		elif res=="d":
			note_index = raw_input("Please enter index of note to delete: ")
			while not note_index.isdigit():
				note_index = raw_input("Please enter valid index of note to delete: ")
				note_index = int(note_index)
				notes.delete(note_index)
		elif res=="e":
			edit_no = raw_input("Please enter index of note to edit: ")
			while not edit_text.isdigit():
				edit_no = raw_input("Please enter valid index of note to edit: ")
				edit_no = int(edit_no)
			edit_text = raw_input("Please enter text: ")
			notes.edit(edit_no, edit_text)
		else:
			print("\\nNot a valid response")

	elif response=="q":
		break



