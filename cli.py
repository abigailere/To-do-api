import requests
# setting up basic cli for user to create todos and view them
BASE_URL = "http://127.0.0.1:8000"

def create_todo():
    title = input("Enter the title of the todo: ")
    description = input("Enter the description of the todo: ")
    response = requests.post(f"{BASE_URL}/", json={"title": title, "description": description, "complete": False})
    
    if response.status_code == 200:
        print(f"✓ Todo added!")
    else:
        print(f"Error: {response.text}")

def update_todo():
    #search via the title
    #ask user what they want to do with the retrieved item
    title = input("Enter the title of the todo to update: ")
    
    print("What would you like to update?")
    print("1. title")
    print("2. description")
    
    choice = input("Enter your choice: ")
    if choice == "2":
        new_description = input("Enter the new description: ")
        response = requests.put(f"{BASE_URL}/", json={"title": title, "description": new_description})
        response = requests.get(f"{BASE_URL}/{title}")
        if response.status_code == 200:
            print(f"✓ Todo updated!")
            print(response.text)
        else:
            print(f"Error: {response.text}")
update_todo()

    
    