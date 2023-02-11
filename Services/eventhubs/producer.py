import json
import asyncio
from datetime import datetime

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

# data model
from rentals import Rental
from eventhub_utilities import *

from eventhub_constants import EVENT_HUB_NAME,\
                              EVENT_HUB_CONNECTION,\
                              RECORD_TO_SEND




def create_streaming_data():
    arrayList = []
    ctr = 0
    now = datetime.datetime.now() 
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
    while ctr < int(RECORD_TO_SEND):
        arrayList.append(Rental(generate_random_rental(),
                                generate_random_status(),
                                generate_random_cities(),
                                generate_random_cities(),
                                generate_random_pickup_date(),
                                generate_random_dropoff_date(),
                                'NZ',
                                date_time))
        ctr = ctr + 1


    return arrayList


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION, eventhub_name=EVENT_HUB_NAME
    )

    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        rentalList = create_streaming_data()
        counter = 0
        for rental in rentalList:
            data = json.dumps(rental.__dict__)
            event_data_batch.add(EventData(data))
            counter = counter + 1
            print(f'.....sending record # {counter}')
        print(f'.....sending record completed')

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)



if __name__ == "__main__":
    asyncio.run(run())

