import uuid
from azure.storage.blob import BlobServiceClient,  ContainerClient

from eventhub_utilities import *
from eventhub_constants import BLOB_RAW_CONTAINER_NAME,\
                               BLOB_STORAGE_CONNECTION_KEY



def stream_block_blob(str_json, folder_destination):
    # Instantiate a new ContainerClient
    container_name = BLOB_RAW_CONTAINER_NAME  # str(uuid.uuid4())
    # Create a unique name for the container

    blob_service_client = BlobServiceClient.from_connection_string(BLOB_STORAGE_CONNECTION_KEY)
    container = ContainerClient.from_connection_string(BLOB_STORAGE_CONNECTION_KEY, container_name)

    if container.exists():
        pass
    else:
        # Container foo does not exist. You can now create it.
        container.create_container()

    data = str_json
    #current_time = datetime.datetime.now()
    dir_parent_name = folder_destination.split('/')[0]
    dir_child_name = folder_destination.split('/')[1]
    
    file_name = ("/".join([dir_parent_name,dir_child_name,
                           # str(current_time.year),
                           # str(current_time.month),
                           # str(current_time.day),
                           # str(current_time.hour),
                           str(uuid.uuid4()) + ".json"]))

    print(file_name) #streaming/29b98232-1543-4e25-939a-627b22b3d437.json
    # Instantiate a new ContainerClient
    container_client = blob_service_client.get_container_client(container_name)

    try:
        # Instantiate a new source blob client
        source_blob_client = container_client.get_blob_client(file_name)

        # Upload content to block blob
        source_blob_client.upload_blob(data, blob_type="BlockBlob")

    finally:
        # Delete container
        pass



