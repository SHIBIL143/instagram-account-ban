import os
import time
import requests

def login(username, password):
    login_url = 'https://www.instagram.com/accounts/login/'
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    login_data = {
        'username': username,
        'password': password,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    response = session.post(login_url, data=login_data)
    if response.ok:
        print("Login successful")
        return session
    else:
        print("Login failed")
        return None

def report_user(session, user_id):
    report_url = f'https://www.instagram.com/users/{user_id}/report/'
    response = session.get(report_url)
    if response.ok:
        print(f"{user_id} Ban reported successfully { i+1 }/{num_reports}.")
    else:
        print(f"Failed to report user with ID {user_id}.")

if __name__ == "__main__":
    with open('u.txt', 'r') as file:
        uinfo = file.read().strip()
    with open('p.txt', 'r') as file:
        pinfo = file.read().strip()
    with open('v.txt', 'r') as file:
        vinfo = file.read().strip()

    your_username = uinfo
    your_password = pinfo
    user_id_to_report = vinfo
    num_reports = 1000

    session = login(your_username, your_password)

    if session:
        for i in range(num_reports):
            report_user(session, user_id_to_report)
            
        print("All ban reports completed.")  # Proper indentation
        
        def delete_file(file_path):
            try:
                os.remove(file_path)
            except FileNotFoundError:
                pass

        file_paths = ["u.txt", "p.txt", "v.txt"]
        for file_path in file_paths:
            delete_file(file_path)

    else:
        print("Unable to proceed without login.")
