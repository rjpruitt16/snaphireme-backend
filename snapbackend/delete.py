from subprocess import call

if __name__ == "__main__":
 call(["/home/rjpruitt22/.virtualenvs/snaphireme/bin/python", "/home/rjpruitt22/snaphireme-backend/snapbackend/manage.py", "deleteDayOldCapsules"])
 print("success")
