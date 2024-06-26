import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        try:
            response = requests.get(URL)
            response.raise_for_status()  # Check if the request was successful
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

        return response.json()

if __name__ == "__main__":
    programs = GetPrograms().get_programs()
    
    if programs:
        # Print the JSON response in a formatted manner
        print(json.dumps(programs, indent=2))
    else:
        print("No programs found or an error occurred.")
