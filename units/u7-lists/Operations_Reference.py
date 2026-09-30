# Unit 7.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: sort() sorts in place and returns None; make a copy first if a separate
# sorted list (and the original, unsorted) is needed.
def warmup():
    scores = [72, 95, 61]
    ordered = scores.copy()
    ordered.sort()
    print(ordered)


# Task 1: check membership before removing
def safe_remove(items, target):
    if target in items:
        items.remove(target)
        return True
    print("Task not found")
    return False


def task1():
    tasks = ["study", "exercise"]
    print(safe_remove(tasks, "exercise"), tasks)
    print(safe_remove(tasks, "rest"), tasks)


# Task 2: pop(0) until the queue is empty
def process_queue(tasks):
    while len(tasks) > 0:
        current = tasks.pop(0)
        print("Working on:", current)


# Task 3: split, then join with a different separator
def csv_round_trip(text):
    parts = text.split(",")
    return " | ".join(parts)


warmup()
# task1()
# process_queue(["collect data", "run model", "check result"])
# print(csv_round_trip("cat,dog,bird"))
