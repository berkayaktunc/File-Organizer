from sys import platform
import shutil
import time
import os


class FileOrganizer:
    def __init__(self):

        # Need to update
        self.shorts = {
            "Project": ["exe", "c", "py"],
            "Picture": ["jpg", "bmp", "png"],
            "Video": ["mp4", "mov", "mkv"],
            "Document": ["docx", "doc", "pdf", "xlsx", "ods", "ppt", "txt"],
            "Compressed": ["rar", "zip", "7zip", "tar"]
        }

        self.counter = "0"

        # Log file name
        self.logFile = "OrganizerLog"

        # Get location to run
        self.cwd = os.getcwd()

        # Get all items in the folder
        self.items = os.listdir(self.cwd)

        # Remove folders in list
        self.items = [x for x in self.items if os.path.isfile(
            os.path.join(self.cwd, x))]

    # Return all items in location
    def get_items(self):
        return self.items

    # Returns the key of the dictionary
    #   to use them as folder
    def get_divKeys(self):
        return self.shorts.keys()

    # Creates a folder for key
    def create_folder(self, key):
        if not os.path.exists(key):
            os.makedirs(key)

    def create_record(self):
        f = open(self.logFile, "a")
        f.close()

    def move_item(self, item, key, flag=0):
        self.create_folder(key)

        # Move the item
        if not os.path.exists(os.path.join(self.cwd, key, item)):
            shutil.move(item, key)
            self.add_record(item, key)
        elif flag == 1:
            # Rename the item that has file type
            #   and recall the method
            temp = item.split(".")[0] + self.counter + "." + item.split(".")[1]
            os.rename(item, temp)
            self.move_item(temp, key, 1)
        else:
            # Rename the item that does not have any file type
            #   which will be moved to Other folder
            #   and recall the method
            temp = item + str(self.counter)
            os.rename(item, temp)
            self.move_item(temp, key, 2)

    def prapere_item(self, item):
        # Cheks item type and
        if "." in item:
            temp = item.split(".")[1]
            for key in self.get_divKeys():
                if temp in self.shorts[key]:
                    self.move_item(item, key, 1)
        else:
            self.move_item(item, "Other", 2)

    def add_record(self, item, key):
        f = open(self.logFile, "a+")
        f.write(str(item) + "\t->\t" + str(key) + "\n")
        f.close()


# Main runner
def main():
    fo = FileOrganizer()
    items = fo.get_items()

    for item in items:
        fo.prapere_item(item)


if __name__ == "__main__":
    main()
