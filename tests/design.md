# 1. Design a problem.
    # As a user
    So that I can record my experiences
    I want to keep a regular diary

    # As a user
    So that I can reflect on my experiences
    I want to read my past diary entries

    As a user
    So that I can reflect on my experiences in my busy day
    I want to select diary entries to read based on how much time I have and my reading speed

    As a user
    So that I can keep track of my tasks
    I want to keep a todo list along with my diary

    As a user
    So that I can keep track of my contacts
    I want to see a list of all of the mobile phone numbers in all my diary entries

# 2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

# Nouns
Diary
Diary entries
Experiences
Time
Reading speed
Todo list
Tasks
Phone numbers
List of phone numbers

# Verbs
Record
Keep
Read
Reflect
Select
See a list
Mark complete
List complete
List incomplete
Add

_Also design the interface of each class in more detail._

```python
class Diary():
    # No property entries

    def add(self, diary_entry)
        # diary_entry: instance of DiaryEntry
        # returns nothing
        # side-effects: adds to list of diary entries
        pass

    def all(self):
        # returns a list of DiaryEntry instances
        pass

class DiaryEntry():
    # Public properties:
    # title: a string representing an entry title
    # contents: a string representing entry contents
    def __init__(self, title, contents)
        # title: a string representing an entry title
        # contents: a string representing entry contents
        # side-effects: sets the above properties
        pass

class TaskList():
    def add(self, task)
        # task: an instance of Task
        # returns: nothing
        # side-effects: adds to list of tasks
        pass

    def all_incomplete(self):
        # returns a list of instances of Task
        # representing the incomplete tasks
        pass

    def all_complete(self):
        # returns a list of instances of Task
        # representing the complete tasks
        pass

class Task():
    # Public propertis:
    # Title: a string representing a job to do
    def __ init__(self, title):
        # Title: a string representing a job to do
        # side-effects: sets title property
        pass

    def mark_complete(self):
        # side-effect: sets title property
        # returns nothing
        pass

class PhoneNumberExtractor():
    def __init__ (self, diary)
        # diary: an instance of Diary
        # side-effect: set diary property
        pass

    def extract(self):
        # returns a list of strings representing
        # a list of phone numbers

class ReabableEntryExtractor():
     def __init__ (self, diary)
        # diary: an instance of Diary
        # side-effect: set diary property
        pass

    def extract(self, wpm, minutes):
        # wpm: integer
        # minutes: integer
        # returns the longest diary entry that can be read
        # in the time given the wpm and minutes
        pass
```
# 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

```python
"""
When I add multiple diary entries
#all lists them out in the order they were added
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My Contents 1")
entry_2 = DiaryEntry("My Title 2", "My Contents 2")
entry_3 = DiaryEntry("My Title 3", "My Contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.all() # => [entry_1, entry_2, entry_3]

"""
When I add multiple tasks
And I don't mark any complete
#all_incomplete lists them out in the order they were added
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task.list.add(task_1)
task.list.add(task_2)
task.list.add(task_3)
task_list.all_incomplete() # => [task_1, task_2, task_3]

"""
When I add multiple tasks
And I mark one as complete
#all_complete only lists the complete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task.list.add(task_1)
task.list.add(task_2)
task.list.add(task_3)
task_2.mark_complete()
task_list.all_complete() # => [task_2]

"""
When I add multiple diary entries
And I call PhoneNumberExtractor #extract
I get a list of phone numbers from all diary entry contents
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 0780000000 and 0780000001")
entry_2 = DiaryEntry("My Title 2", "My Contents 2")
entry_1 = DiaryEntry("My Title 1", "My friend is 0780000002")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = PhoneNumberExtractor(diary)
extractor.extract()  # => ["0780000000". "0780000001", "0780000002"]

"""
When I add multiple diary entries
And I call PhoneNumberExtractor #extract
It ignores duplicate numbers
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 0780000000 and 0780000000")
entry_2 = DiaryEntry("My Title 2", "My friend is 0780000000")
diary.add(entry_1)
extractor = PhoneNumberExtractor(diary)
extractor.extract()  # => ["0780000000"]

"""
When I add a diary entry
And I call PhoneNumberExtractor #extract
It ignores non-valid phone numbers
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 078000001 and 078, 13454")
extractor = PhoneNumberExtractor(diary)
extractor.extract()  # => []

"""
When I add no deary entries
and I call PhoneNumberExtractor #extract
It returns an empty list
"""
diary = Diary()
extractor = PhoneNumberExtractor(diary)
extractor.extract()  # => []

"""
When I add one diary entry that fits in the time
and I call ReadebleEntryExtractor #extract
With a wpm of 2 and a minutes if 2
It gets that diary entry
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four")
diary.add(entry_1)
extractor = ReadeableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2)  # => entry_1

"""
When I add one diary entry that does not fit in the time
and I call ReadebleEntryExtractor #extract
With a wpm of 2 and a minutes if 2
It return None
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four five")
diary.add(entry_1)
extractor = ReadeableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2)  # => None

"""
When I add multiple diary entries, one readable
and I call ReadebleEntryExtractor #extract
With a wpm of 2 and a minutes if 2
It gets the readable one
"""
diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four five")
entry_2 = DiaryEntry("Title", "one two three four")
diary.add(entry_1)
diary.add(entry_2)
extractor = ReadeableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2)  # => entry_2

"""
When I add multiple diary entries, multiple readable
and I call ReadebleEntryExtractor #extract
With a wpm of 2 and a minutes if 2
It gets the longest readable one
"""
diary = Diary()
entry_1 = DiaryEntry("Title", "one two three four five")
entry_2 = DiaryEntry("Title", "one two three four")
entry_3 = DiaryEntry("Title", "one two three")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = ReadeableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2)  # => entry_2

"""
When I add no deary entries
and I call ReadebleEntryExtractor #extract
With a wpm of 2 and a minutes if 2
It returns None
"""
diary = Diary()
extractor = ReadeableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2)  # => None

```

# 4. Create Examples as Unit Tests

# Diary
```python
"""
Initially, Diary has no entries
"""
diary = Diary()
diary.all() # => []

# DiaryEntry
"""
DiaryEntry is constructed with a title and contents
"""
entry = DiaryEntry("My Title", "My Contents")
entry.title() # => "My Title"
entry.contents() # => "My Contents"

# TaskList
"""
Initially, TaskList has no incomplete tasks
"""
task_list = TaskList()
task_list.all_incompplete() # => []

# TaskList
"""
Initially, TaskList has no complete tasks
"""
task_list = TaskList()
task_list.all_compplete() # => []

# Task
"""
Task constructs with a title
"""
task = Task("Walk the dog")
task.title # => "Walk the dog"
```