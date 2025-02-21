# Requests data (test program)

import requests
import json

class ActivityRecommendationClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_recommendations(self, location, activity_type, budget):
        url = f"{self.base_url}/recommendations"
        payload = {
            "location": location,
            "activity_type": activity_type,
            "budget": budget
        }
        response = requests.post(url, json=payload)
        return response.json()

    def display_recommendations(self, recommendations):
        print("\nRecommended Activities:")
        print("=======================")
        for activity in recommendations:
            print(f"\nName: {activity['name']}")
            print(f"Description: {activity['description']}")
            print(f"Location: {activity['location']}")
            print(f"Type: {activity['type']}")
            print(f"Price: ${activity['price']}")
            print(f"Distance: {activity['distance']} miles")
        print("\n=======================\n")

if __name__ == '__main__':
    client = ActivityRecommendationClient("http://127.0.0.1:6767")
    
    print("Sending request for activity recommendations...")
    result = client.get_recommendations("Los Angeles", "food & drink", "$30")
    client.display_recommendations(result)
