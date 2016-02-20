#still working on it but right now, the application is fully interactive
from notesapplication import NotesApplication

name = raw_input("Please input Author's Name: ")

notes = NotesApplication(name)
inp = ""
while inp!= "q":
	print("\n\n\t\t\t\t\t\t\t\tMain Menu\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
	print("\n------------------------------------------------------------------------------------------------------------------------------------")
	response = raw_input("Enter c to create a new Note or q to quit or n to go to next menu ")
	if response=="c":
		notes_content = raw_input("\n\nPlease Enter your note: ")
		notes.create(notes_content)

		print("\n\nNotes have been saved successfully")
		print("\n\n\t\t\t\t\t\t\t\tMenu\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
		print("\n------------------------------------------------------------------------------------------------------------------------------------")
		print("\n\nPress m to return to menu")
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
			notes.search(search_text)
		elif res=="r":
			index = raw_input("Please enter index of note to retrieve: ")
			while not index.isdigit():
				index = raw_input("Please enter valid index of note to retrieve: ")
				
			else:
				index = int(index)
				print "\n" + notes.get(index)

		elif res=="d":
			note_index = raw_input("Please enter index of note to delete: ")
			while not note_index.isdigit():
				note_index = raw_input("Please enter valid index of note to delete: ")
				
			else:
				note_index = int(note_index)
				notes.delete(note_index)
				

		elif res=="e":
			edit_no = raw_input("Please enter index of note to edit: ")
			while not edit_no.isdigit():
				edit_no = raw_input("Please enter valid index of note to edit: ")
			else:
				edit_no = int(edit_no)
			edit_text = raw_input("Please enter text: ")
			notes.edit(edit_no, edit_text)



		else:
			print("\n\nNot a valid response, Returning you back to menu")

	elif response=="n":
		
		print("\n\n\t\t\t\t\t\t\t\tMenu\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
		print("\n------------------------------------------------------------------------------------------------------------------------------------")
		print("\n\nPress m to return to menu")
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
			index = raw_input("Please enter index of note to retrieve: ")
			while not index.isdigit():
				index = raw_input("Please enter valid index of note to retrieve: ")
				
			else:
				index = int(index)
				print "\n" + notes.get(index)

		elif res=="d":
			note_index = raw_input("Please enter index of note to delete: ")
			while not note_index.isdigit():
				note_index = raw_input("Please enter valid index of note to delete: ")
				
			else:
				note_index = int(note_index)
				notes.delete(note_index)
				print("\n Note with index %d has been successfully deleted! Taking you back to main menu" % note_index)

		elif res=="e":
			edit_no = raw_input("Please enter index of note to edit: ")
			while not edit_no.isdigit():
				edit_no = raw_input("Please enter valid index of note to edit: ")
			else:
				edit_no = int(edit_no)
			edit_text = raw_input("Please enter text: ")
			notes.edit(edit_no, edit_text)



		else:
			print("\n\nNot a valid response, Returning you back to menu")


	elif response=="q":
		break



