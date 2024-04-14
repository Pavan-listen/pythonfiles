import re
def find_seat_allotment( usn ):
    with open("/Users/pavan/Git/pythonfiles/college_project/input1.txt", "r", encoding='utf-8') as R:
        data = R.read()
        mdata = data.split(
            '================================================================================================================')
        for line in mdata:
            if usn in line:
                room_index = line.find('Room No. :')
                coursecode_index = line.find('Course Code :')
                usn_index = line.find(usn)
                course_ti_index = line.find('Course Title :')

                if room_index != -1:
                    # Extract the room number
                    room_number = line[room_index + len('Room No. :'): room_index + len('Room No. :') + 7].strip()

                if coursecode_index != -1:
                    # Extract the course_code
                    course_code = line[coursecode_index + len('Course Code :'): coursecode_index + len('Course Code :') + 8].strip()

                if usn_index != -1:
                    # Extract the seat number
                    seat_num = line[(usn_index - 7): usn_index ].strip().lstrip()
                    original_string = seat_num
                    seat_num = re.sub(r'[^0-9]', ' ', original_string)

                if course_ti_index != -1:
                    # Extract the course title number
                    course_title = line[course_ti_index + len('Course Title :'): course_ti_index + len('Course Title :') + 60].strip()
                    original_string = course_title
                    course_title = re.sub(r'[^a-zA-Z]', ' ', original_string)


                print(f"USN : {usn}")
                print("Course Title :",course_title)
                print("Course Code :", course_code)
                print("Room No. : ", room_number)
                print("Seat No : ", seat_num)


def main():
    usn = input("Enter Usn to search thr Seat allotment : ")
    find_seat_allotment(usn.upper())

if __name__ == "__main__":
    main()


