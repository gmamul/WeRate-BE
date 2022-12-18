from flask import Flask, jsonify, request

app = Flask(__name__)

properties = [
    {
        'id': 1,
        'name': 'Property 1',
        'address': {
            'country': 'USA',
            'province': 'NY',
            'city': 'New York',
            'zip_code': '10001',
            'address': '123 Main St',
            'address2': '',
        },
        'sizeFee': {
            'price': 1000,
            'currency': 'USD',
            'size': 120,
            'water': 50
        },
        'amenities': {
            'wifi': True,
            'storage': False,
            'parking': False,
            'doorCode': False,
            'sauna': False,
            'electricity': False,
        },
        'additionalInfo': {
            "wifiName": "MyWifi",
            "wifiPassword": "secret1234",
            'storage': 'B451',
            'parking': 'A920',
            'doorCode': '2536',
            'saunaHours': '18:00 - 20:00',
            'electricityProvider': ''
        },
        'houseRules': {
            'silence': 'after 21:00',
            'smoking': False,
            'pets': False,
            'parties': False
        },
        'janitorInfo': {
            'janitorName': 'bastel',
            'janitorPhone': '+995568545678'
        },
        'status': 'new',
        'favorite': False,
        'uri': 'https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
    },
    {
        'id': 2,
        'name': 'Property 2',
        'address': {
            'country': 'USA',
            'province': 'LA',
            'city': 'Los Angeles',
            'zip_code': '90001',
            'address': '456 Hollywood Blvd',
            'address2': '',
        },
        'sizeFee': {
            'price': 1200,
            'currency': 'USD',
            'size': 120,
            'water': 60
        },
        'amenities': {
            'wifi': True,
            'storage': False,
            'parking': False,
            'doorCode': False,
            'sauna': False,
            'electricity': False,
        },
        'additionalInfo': {
            "wifiName": "MyWifi",
            "wifiPassword": "secret1234",
            'storage': 'B451',
            'parking': 'A920',
            'doorCode': '2536',
            'saunaHours': '18:00 - 20:00',
            'electricityProvider': ''
        },
        'houseRules': {
            'silence': 'after 21:00',
            'smoking': False,
            'pets': False,
            'parties': False
        },
        'janitorInfo': {
            'janitorName': 'bastel',
            'janitorPhone': '+995568545678'
        },
        'status': 'rented',
        'favorite': True,
        'uri': 'https://images.pexels.com/photos/186077/pexels-photo-186077.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
    }
]


class Request:
    def __init__(self, id, tenantFullName, tenantRating, applicationStatus, mobileNumber, emailAddress,
                 propertyId, rentalPeriodStart, rentalPeriodEnd, rentalDuration, expiresIn, applicationStartDate,
                 applicationEndDate, stage, numberOfAssessments, paymentsScore, HousekeepingScore, communicationScore,
                 otherScore, imageUri, propertyName):
        self.id = id
        self.tenantFullName = tenantFullName
        self.tenantRating = tenantRating
        self.applicationStatus = applicationStatus
        self.mobileNumber = mobileNumber
        self.emailAddress = emailAddress
        self.propertyId = propertyId
        self.rentalPeriodStart = rentalPeriodStart
        self.rentalPeriodEnd = rentalPeriodEnd
        self.rentalDuration = rentalDuration
        self.expiresIn = expiresIn
        self.applicationStartDate = applicationStartDate
        self.applicationEndDate = applicationEndDate
        self.stage = stage
        self.numberOfAssessments = numberOfAssessments
        self.paymentsScore = paymentsScore
        self.HousekeepingScore = HousekeepingScore
        self.communicationScore = communicationScore
        self.otherScore = otherScore
        self.imageUri = imageUri
        self.propertyName = propertyName


requests = [
    Request(1, "John Smith", 85, "pending", "555-555-5555", "johnsmith@email.com", 1, "01 Jan 2021",
            "31 Jan 2021", "1 month", "7 days", "15 Dec 2020", "20 Dec 2020", 2, 3, 89, 95, 72, 87, "https://static.vecteezy.com/system/resources/previews/009/398/577/original/man-avatar-clipart-illustration-free-png.png", "Property 1").__dict__,
    Request(2, "Jane Doe", 72, "approved", "555-555-5556", "janedoe@email.com", 2, "01 Feb 2021",
            "28 Feb 2021", "4 weeks", "5 days", "25 Jan 2021", "30 Jan 2021", 3, 2, 75, 92, 68, 70, "https://cdn.pixabay.com/photo/2017/01/31/21/23/avatar-2027365_1280.png", "Property 2").__dict__,
    Request(3, "Robert Johnson", 92, "rejected", "555-555-5557", "robertjohnson@email.com", 3,
            "01 Mar 2021", "31 Mar 2021", "1 month", "3 days", "05 Feb 2021", "08 Feb 2021", 4, 4, 95, 89, 82, 65, "https://cdn.imgbin.com/10/14/1/imgbin-female-avatar-best-yYYaN63pH07CPxi6N6b1MeiDR.jpg", "Property 3").__dict__,
    Request(4, "Emily Williams", 78, "pending", "555-555-5558", "emilywilliams@email.com", 1, "01 Apr 2021",
            "30 Apr 2021", "1 month", "10 days", "20 Mar 2021", "30 Mar 2021", 2, 1, 82, 94, 70, 80, "https://www.pngrepo.com/png/165876/512/avatar.png", "Property 1").__dict__
]


# requests = [
#     {
#         "id": 1,
#         "tennantFullName": "Matti Meikäläinen",
#         "propertyId": 2,
#         "rating": "75",
#         "rentalStartDate": "2022-12-01",
#         "rentalEndDate": "2022-12-31",
#         "rentalDuration": "30 days",
#         "applicationStartDate": "2022-11-01",
#         "applicationEndDate": "2022-11-30",
#         "expiresIn": "1 month"
#     },
#     {
#         "id": 2,
#         "tennantFullName": "Maija Mäkeläinen",
#         "propertyId": 1,
#         "rating": "85",
#         "rentalStartDate": "2022-12-15",
#         "rentalEndDate": "2023-01-14",
#         "rentalDuration": "30 days",
#         "applicationStartDate": "2022-11-15",
#         "applicationEndDate": "2022-12-14",
#         "expiresIn": "1 month"
#     },
#     {
#         "id": 3,
#         "tennantFullName": "Kalle Kekkonen",
#         "propertyId": 1,
#         "rating": "65",
#         "rentalStartDate": "2022-12-10",
#         "rentalEndDate": "2022-12-30",
#         "rentalDuration": "20 days",
#         "applicationStartDate": "2022-11-10",
#         "applicationEndDate": "2022-11-30",
#         "expiresIn": "1 month"
#     },
#     {
#         "id": 4,
#         "tennantFullName": "Liisa Laitinen",
#         "propertyId": 1,
#         "rating": "95",
#         "rentalStartDate": "2022-12-01",
#         "rentalEndDate": "2023-01-31",
#         "rentalDuration": "61 days",
#         "applicationStartDate": "2022-11-01",
#         "applicationEndDate": "2022-12-01",
#         "expiresIn": "1 month"
#     },
#     {
#         "id": 5,
#         "tennantFullName": "Johanna Järvinen",
#         "propertyId": 1,
#         "rating": "80",
#         "rentalStartDate": "2022-12-20",
#         "rentalEndDate": "2023-01-19",
#         "rentalDuration": "30 days",
#         "applicationStartDate": "2022-11-20",
#         "applicationEndDate": "2022-12-19",
#         "expiresIn": "1 month"
#     },
#     {
#         "id": 6,
#         "tennantFullName": "Timo Tammi",
#         "propertyId": 1,
#         "rating": "70",
#         "rentalStartDate": "2022-12-05",
#         "rentalEndDate": "2023-01-04",
#         "rentalDuration": "30 days",
#         "applicationStartDate": "2022-11-05",
#         "applicationEndDate": "2022-12-04",
#         "expiresIn": "1 month"
#     }
# ]


@ app.route('/requests', methods=['GET'])
def get_all_requests():
    return jsonify(requests), 200


@ app.route('/property/<int:property_id>/requests/', methods=['GET'])
def get_requests_by_propertyid(property_id):
    propertyRequests = [
        request for request in requests if request['propertyId'] == property_id]
    if len(propertyRequests) == 0:
        return jsonify({'message': 'Requests not found'}), 404
    return jsonify(propertyRequests), 200


@ app.route('/requests/<int:request_id>', methods=['GET'])
def get_requests_by_id(request_id):
    request = [
        request for request in requests if request['id'] == request_id]
    if len(request) == 0:
        return jsonify({'message': 'Property not found'}), 404
    return jsonify(request[0])


@ app.route('/properties', methods=['GET'])
def get_properties():
    return jsonify(properties), 200


@ app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = [
        property for property in properties if property['id'] == property_id]
    if len(property) == 0:
        return jsonify({'message': 'Property not found'}), 404
    return jsonify(property[0])


@ app.route('/properties', methods=['POST'])
def create_property():
    data = request.get_json()
    new_property = {
        'id': properties[-1]['id'] + 1,
        'name': data['name'],
        'status': data['status'],
        'favorite': data['favorite'],
        'uri': data['uri'],
        'address': {
            'country': data['address']['country'],
            'province': data['address']['province'],
            'city': data['address']['city'],
            'zip_code': data['address']['zip_code'],
            'address': data['address']['address'],
            'address2': data['address']['address2'],
        },
        'sizeFee': {
            'price': data['sizeFee']['price'],
            'currency': data['sizeFee']['currency'],
            'size': data['sizeFee']['size'],
            'water': data['sizeFee']['water'],
        },
        'amenities': {
            'wifi': data['amenities']['wifi'],
            'storage': data['amenities']['storage'],
            'parking': data['amenities']['parking'],
            'doorCode': data['amenities']['doorCode'],
            'sauna': data['amenities']['sauna'],
            'electricity': data['amenities']['electricity'],
        },
        'additionalInfo': {
            "wifiName": data["additionalInfo"]["wifiName"],
            "wifiPassword": data["additionalInfo"]["wifiPassword"],
            'storage': data["additionalInfo"]["storage"],
            'parking': data["additionalInfo"]["parking"],
            'doorCode': data["additionalInfo"]["doorCode"],
            'saunaHours': data["additionalInfo"]["saunaHours"],
            'electricityProvider': data["additionalInfo"]["electricityProvider"],
        },
        'houseRules': {
            'silence': data["houseRules"]["silence"],
            'smoking': data["houseRules"]["smoking"],
            'pets': data["houseRules"]["pets"],
            'parties': data["houseRules"]["parties"],
        },
        'janitorInfo': {
            'janitorName': data["janitorInfo"]["janitorName"],
            'janitorPhone': data["janitorInfo"]["janitorPhone"],
        },
    }
    properties.append(new_property)
    return jsonify(new_property), 201


@ app.route('/properties/<int:id>', methods=['PATCH'])
def update_property(id):
    data = request.get_json()
    for property in properties:
        if property['id'] == id:
            if 'address' in data:
                property['address'] = data['address']
            if 'bedrooms' in data:
                property['bedrooms'] = data['bedrooms']
            if 'bathrooms' in data:
                property['bathrooms'] = data['bathrooms']
            if 'sqft' in data:
                property['sqft'] = data['sqft']
            return jsonify(property), 202

    return jsonify({'message': 'property not found'}), 404


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
