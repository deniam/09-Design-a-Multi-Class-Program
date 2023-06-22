from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
When I add multiple diary entries
#all lists them out in the order they were added
"""
def test_adds_and_list_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents 1")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    entry_3 = DiaryEntry("My Title 3", "My Contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.all() == [entry_1, entry_2, entry_3]

# """
# When I add multiple tasks
# And I don't mark any complete
# #all_incomplete lists them out in the order they were added
# """
# task_list = TaskList()
# task_1 = Task("Walk the dog")
# task_2 = Task("Walk the cat")
# task_3 = Task("Walk the frog")
# task.list.add(task_1)
# task.list.add(task_2)
# task.list.add(task_3)
# task_list.all_incomplete() # => [task_1, task_2, task_3]