# File Organizer

### Explanation

File Organizer is the app to ease the organizing the folder specifically for download folder. Place the **fileOrganizer.py** file securely in your system.

# Easy Way To Use
## Linux

Open your terminal where you keep the file and type

```bash
> alias {{Your alias name}}='python {{your path here}}/fileOrganizer.py'
```
Example,

```bash
> alias test='python /Home/fileOrganizer.py'
```

After applying the alias, open terminal in the folder where you need to organize and type organize to organize the folder.

## Mac

```bash
!/bin/zsh

cd { Location to your fileOrganizer.py }
python fileOrganizer.py
```
Example
```bash
!/bin/zsh

cd /Users/APPS/fileOrganizer.py
python fileOrganizer.py
```
### Questions

> Your 'Other' folder filled with the files that is not supposed to. Whet should I do?
- Open the**fileOrganizer.py** and modify **self.shorts** according to your needs. Add the file type to the place you want the folder in and apply the organization steps again.

> I misspelled the alias. What should I do?
- Type the line abow according to your needs then redo the alias

```bash
unalias {{your misspelled alias name}}
```
Example
```bash
unalias test
```