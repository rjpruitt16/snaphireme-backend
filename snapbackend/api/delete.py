from subprocess import call

if __name__ == "__main__":
    call(["python3", "manage.py", "deleteDayOldCapsules"])
