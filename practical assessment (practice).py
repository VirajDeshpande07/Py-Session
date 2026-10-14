#create a dictionary with studnent details

students = {
    101: {"Name": "Aditi", "Scores": [20, 20, 25]},
    102: {"Name": "Aditi", "Scores": [20, 20, 25]},
    103: {"Name": "Aditi", "Scores": [20, 20, 25]},
    104: {"Name": "Aditi", "Scores": [20, 20, 25]},
    105: {"Name": "Aditi", "Scores": [20, 20, 25]},
}

# Calculate average and flag pass/fail
for sid, details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 30

# Print names of students who passed
print("Students who passed:")

for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])

