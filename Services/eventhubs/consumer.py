import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import (
    BlobCheckpointStore,
)
from savetodatalake import *
from constants.service_constants import EVENT_HUB_CONNECTION,\
                                        BLOB_STORAGE_CONNECTION_KEY,\
                                        BLOB_CHECK_POINT_CONTAINER_NAME,\
                                        SAVE_TO_ADLS2,\
                                        EVENT_HUB_NAME


async def on_event(partition_context, event):
    str_json = event.body_as_str(encoding="UTF-8")
    # Print the event data.
    print(
        'Received the event: "{}" from the partition with ID: "{}"'.format(
            str_json, partition_context.partition_id
        )
    )

    # save to azure datalake storage
    if SAVE_TO_ADLS2:
        stream_block_blob(str_json)

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)


async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string(
        BLOB_STORAGE_CONNECTION_KEY, BLOB_CHECK_POINT_CONTAINER_NAME
    )

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(
        EVENT_HUB_CONNECTION,
        consumer_group="$Default",
        eventhub_name=EVENT_HUB_NAME,
        checkpoint_store=checkpoint_store,
    )
    async with client:
        # Call the receive method. Read from the beginning of the
        # partition (starting_position: "-1")
        await client.receive(on_event=on_event, starting_position="-1")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())


