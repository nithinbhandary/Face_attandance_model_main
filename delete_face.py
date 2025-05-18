import os
import shutil
import subprocess
import sys
from mysql.connector import connection

def delect_from_db(rno):
    conn = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='attendance')

    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM attendance.users WHERE username = ( select name FROM attendance.studentdetails WHERE roll_no =%s);", (rno,))
    cursor.execute("DELETE FROM attendance.studentdetails WHERE roll_no = %s", (rno,))
    cursor.execute("DELETE FROM attendance WHERE roll_no = %s", (rno,))
    conn.commit()
    conn.close()


def delete_person(person_id, name):
    
    # Construct path to the person's folder
    path_to_person = f"data/data_faces_from_camera/person_{person_id}_{name}"
    
    # Check if the folder exists
    if os.path.exists(path_to_person):
        try:
            # Attempt to remove the entire folder and its contents
            delect_from_db(person_id)
            shutil.rmtree(path_to_person)
            print(f"Data for person {person_id} ({name}) deleted successfully.")
            return True
        except Exception as e:
            print(f"Error deleting data for person {person_id}: {str(e)}")
            return False
    else:
        print(f"Data for person {person_id} ({name}) not found.")
        return False

# Assuming you want to delete all data associated with person 1
if __name__ == '__main__':
    person_id= sys.argv[1]
    name=sys.argv[2]
    deleted = delete_person(person_id, name)
    if deleted:
        print("Data for person deleted successfully.")
    else:
        print("Failed to delete data for person.")
    subprocess.run(["python", "features_extraction_to_csv.py"])