class Note:
  def __init__(self, titles, contents):
        self.title = titles
        self.content = contents

def header(Count):
  print("______________________________________________________\n")
  print("--------Notes App--------")
  print("there are {} Notes saved".format(Count))

def reseter():
    option = 0
    header(nCount)
    print("\n1. Show Notes \n2. Create new Notes \n9. Exit")
    option = input("\n\nEnter the Option\t: ")
    return option


Storage = []
nCount = len(Storage)
option = reseter()

while True:
    if (option == '1'):
        for note in Storage:
          title = note.title
          content = note.content
          print("\n----------------- Title : {} -------------------".format(title))
          print("\n{}".format(content))
          print("\n---------------------------------------------\n")

        option = reseter()

    elif (option == '2'):
        header(nCount)
        title = input("\nEnter the Title :  ")
        content = input("\nEnter the Content :  ")
        note = Note(title,content)
        Storage.append(note)
        nCount = len(Storage)
        option = reseter()

    elif (option == '9'):
        print("\nExiting....")
        break

    else :
        print("\n-----------\nwrong input")
        option = reseter()


