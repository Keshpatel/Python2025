file_name = "StudentName.txt"

with open(file_name, "r") as file:
    data = file.read()

    print("Data values : ", data)
    parsed_data = data.split(", ")
    print("parse Data: ", parsed_data)
    print("Student at index 3 : ", parsed_data[3])
    

