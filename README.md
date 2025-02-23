Communication Contract

NOTE: Please do not use the test program provided below (it is not required), all code must be wrriten on your own.

Activity Recommendation Microservice
    -   This microservice provides activity recommendations based on user inputs such as location, activity type, and budget.

How to Request Data from the Microservice
    -   To request activity recommendations, send a POST request to the microservice with the required parameters.

    Endpoint
        -   POST /recommendations

    Required Parameters
        -   location (String) – City or zip code where the user is located (e.g., "Los Angeles", "90001")
        -   activity_type (String) – Type of activity (e.g., "outdoor", "food & drink", "social", "relaxation")
        -   budget (String or Range) – User's spending limit (e.g., "free", "$10-50", "$100+")

    Example Request (Python)

        import requests

        url = "http://127.0.0.1:5000/recommendations" # Choose desired port number

        data = {
            "location": "Los Angeles",
            "activity_type": "outdoor",
            "budget": "$10-50"
        }

        response = requests.post(url, json=data)

        print(response.json())  # Prints the recommended activities

    Example Request (JavaScript Fetch) - choose desired port number

        const response = await fetch('http://127.0.0.1:5000/recommendations', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                location: 'Los Angeles',
                activity_type: 'outdoor',
                budget: '$10-50'
            })
        });
        const recommendedActivities = await response.json();
        console.log(recommendedActivities);

How to Receive Data from the Microservice
    -   The microservice responds with a JSON array of activity recommendations. Each activity object contains the following fields:
    -   Example Response (JSON):

        [
            {
                "name": "Gourmet Food Truck Festival",
                "description": "A variety of gourmet food trucks offering unique dishes.",
                "price": 20,
                "distance": 2.0,
                "type": "food & drink"
            },
            {
                "name": "Local Brewery Tour",
                "description": "Discover the city's best local breweries and enjoy tastings.",
                "price": 30,
                "distance": 3.5,
                "type": "food & drink"
            }
        ]

![Alt text](UML.png)
