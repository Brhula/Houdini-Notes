import os


path="//sloth/jobs/gwr_1194/films/main/shots"

for item in os.listdir(path):
    if not item.startswith('.'):
        print(item)
