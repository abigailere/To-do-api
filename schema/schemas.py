#create an individual serializer for the todo model, this will be used to validate the data that is sent to the API and to serialize the data that is sent back to the client. This will be used in the routes.py file to validate the data that is sent to the API and to serialize the data that is sent back to the client.
#connect todo object to a dictionary to see ids and other data that is sent to the API, this will be used in the routes.py file to validate the data that is sent to the API and to serialize the data that is sent back to the client. This will be used in the routes.py file to validate the data that is sent to the API and to serialize the data that is sent back to the client.

def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "complete": todo["complete"]
    }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]
    #will run the above funtion for each 'todo' in the 'todos' list and return a list of dictionaries that can be sent back to the client.