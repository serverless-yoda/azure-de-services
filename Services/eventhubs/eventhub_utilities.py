import string
import time
import random
import datetime
import os

rental_columns = ['rentalid', 'status', 'pickuploc', 'dropoffloc','pickupdate','dropoffdate']
cities = ['AKL', 'CHC', 'ZQN', 'WLG']
statuses = ['KK', 'CO', 'CI', 'IN', 'NN', 'XX']


def generate_random_rental(length=10):
    """Generate a random string"""
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def generate_random_cities():
    return str(random.choice(cities))


def generate_random_status():
    return str(random.choice(statuses))


def generate_random_pickup_date():
    """Generate a random pickup date"""
    return datetime.date.fromtimestamp(time.time()).strftime('%Y-%m-%d')


def generate_random_dropoff_date():
    """Generate a random dropoff date"""
    seed = random.randint(1, 60)
    pickup_date = datetime.datetime.strptime(generate_random_pickup_date(), "%Y-%m-%d")
    return str(pickup_date + datetime.timedelta(days=seed)).split(" ")[0]


def random_current_timestamp():
    return generate_random_timestamp_date()


def generate_random_timestamp_date():
    no_seed = random.uniform(-1, -60)
    return str(datetime.date.today() + datetime.timedelta(days=no_seed))


def getConfigPath():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    #print(cur_path)
    return os.path.join(cur_path, "eventhub_pipeline.conf")
