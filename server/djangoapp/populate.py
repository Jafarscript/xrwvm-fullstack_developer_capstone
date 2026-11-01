from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
        {"name": "BMW", "description": "The Ultimate Driving Machine. German engineering"},
        {"name": "Ford", "description": "Built Ford Tough. American heritage"},
        {"name": "Honda", "description": "Reliable and efficient. Japanese engineering"},
        {"name": "Hyundai", "description": "Innovative and modern. Korean technology"},
        {"name": "Tesla", "description": "Pioneering electric vehicles. American innovation"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        # Nissan (car_make_instances[0])
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Altima", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[0]},
        
        # Mercedes (car_make_instances[1])
        {"name": "A-Class", "type": "HATCH", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "GLE", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        
        # Audi (car_make_instances[2])
        {"name": "A4", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5", "type": "COUPE", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Q7", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        
        # Kia (car_make_instances[3])
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "VAN", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Sportage", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        
        # Toyota (car_make_instances[4])
        {"name": "Corolla", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Hilux", "type": "PICKUP", "year": 2023, "car_make": car_make_instances[4]},
        
        # BMW (car_make_instances[5])
        {"name": "3 Series", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[5]},
        {"name": "X5", "type": "SUV", "year": 2023, "car_make": car_make_instances[5]},
        {"name": "M4", "type": "COUPE", "year": 2023, "car_make": car_make_instances[5]},
        
        # Ford (car_make_instances[6])
        {"name": "Mustang", "type": "COUPE", "year": 2023, "car_make": car_make_instances[6]},
        {"name": "Explorer", "type": "SUV", "year": 2023, "car_make": car_make_instances[6]},
        {"name": "F-150", "type": "PICKUP", "year": 2023, "car_make": car_make_instances[6]},
        
        # Honda (car_make_instances[7])
        {"name": "Civic", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[7]},
        {"name": "CR-V", "type": "SUV", "year": 2023, "car_make": car_make_instances[7]},
        {"name": "Accord", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[7]},
        
        # Hyundai (car_make_instances[8])
        {"name": "Elantra", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[8]},
        {"name": "Tucson", "type": "SUV", "year": 2023, "car_make": car_make_instances[8]},
        {"name": "Santa Fe", "type": "SUV", "year": 2023, "car_make": car_make_instances[8]},
        
        # Tesla (car_make_instances[9])
        {"name": "Model 3", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[9]},
        {"name": "Model Y", "type": "SUV", "year": 2023, "car_make": car_make_instances[9]},
        {"name": "Model S", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[9]},
    ]

    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'])
