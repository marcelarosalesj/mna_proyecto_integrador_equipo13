import os
import json

jsonfiles = os.listdir("data_captions")

header_line = (
    "id,video_name,fps,label,caption_pedestrian,caption_vehicle,start_time,end_time"
)

dataset_in_lines = []
dataset_in_lines.append(header_line)

for jf in jsonfiles:
    with open(f"data_captions/{jf}", "r") as ff:
        data = json.load(ff)

        base_line = f"{data['id']},{data.get('video_name')},{data.get('fps')}"

        for phase in data["event_phase"]:
            caption_pedestrian = phase["caption_pedestrian"]
            caption_vehicle = phase["caption_vehicle"]

            caption_pedestrian = caption_pedestrian.replace('"', "'")
            caption_vehicle = caption_vehicle.replace('"', "'")

            next_line = (
                f"{base_line},"
                + f"{phase['labels'][0]},"
                + f'"{caption_pedestrian}",'
                + f'"{caption_vehicle}",'
                + f"{phase['start_time']},"
                + f"{phase['end_time']}"
            )

            dataset_in_lines.append(next_line)


print(f"NUM OF LINES: {len(dataset_in_lines)}")

csv_filename = "captions_dataset.csv"
with open(csv_filename, "w") as ff:
    for line in dataset_in_lines:
        ff.write(line)
        ff.write("\n")

print(f"saved {csv_filename}")
print("Bye")
