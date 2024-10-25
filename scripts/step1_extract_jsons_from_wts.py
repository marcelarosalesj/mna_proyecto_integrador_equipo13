import json
import subprocess
import shutil

res = subprocess.run('fd  ".json"', shell=True, text=True, capture_output=True)
resultados = res.stdout.splitlines()

caption_filenames = []

count_total = 0
count_caption = 0
count_not_caption = 0

for filename in resultados:
    count_total += 1

    with open(filename, "r") as ff:
        data = json.load(ff)

    if data.get("event_phase"):
        caption_filenames.append(filename)
        count_caption += 1
    else:
        count_not_caption += 1

base_filenames = []
for cap in caption_filenames:
    basename = cap.split("/")[-1]
    if basename in base_filenames:
        # repeated
        pass
    else:
        base_filenames.append(basename)
        shutil.copyfile(f"{cap}", f"./data_captions/{basename}")

print(f"count total = {count_total}")
print(f"count caption = {count_caption}")
print(f"count not caption= {count_not_caption}")
