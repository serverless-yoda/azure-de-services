import configparser
from eventhub_utilities import *

parser = configparser.ConfigParser()
parser.read(getConfigPath())

# initialize config parser and get all required information
parser = configparser.ConfigParser()
parser.read(getConfigPath())


# PRODUCER SECTION
# taken from EventHub Shared Access Policies Connection String
EVENT_HUB_NAME = parser.get('EVENT_HUB', 'EVENT_HUB_NAME')
NAMESPACE_NAME = parser.get('EVENT_HUB', 'NAMESPACE_NAME')
SHARED_ACCESS = parser.get('EVENT_HUB', 'SHARED_ACCESS')
EVENT_HUB_CONNECTION = (
                                    f'Endpoint=sb://{NAMESPACE_NAME}/;'
                                    f'SharedAccessKeyName=RootManageSharedAccessKey;'
                                    f'SharedAccessKey={SHARED_ACCESS};'
                                 )

RECORD_TO_SEND = parser.get('DEFAULT', 'RECORD_TO_SEND')


# CONSUMER SECTION
SAVE_TO_ADLS2 = parser.get('DEFAULT', 'SAVE_TO_ADLS2')

EVENT_HUB_NAME = parser.get('EVENT_HUB', 'EVENT_HUB_NAME')
NAMESPACE_NAME = parser.get('EVENT_HUB', 'NAMESPACE_NAME')
SHARED_ACCESS  = parser.get('EVENT_HUB', 'SHARED_ACCESS')

EVENT_HUB_CONNECTION = (
                                    f'Endpoint=sb://{NAMESPACE_NAME}/;'
                                    f'SharedAccessKeyName=RootManageSharedAccessKey;'
                                    f'SharedAccessKey={SHARED_ACCESS};'
                                 )


BLOB_CHECK_POINT_CONTAINER_NAME = parser.get('STORAGE','BLOB_CHECK_POINT_CONTAINER_NAME')
BLOB_EP_URL = parser.get('STORAGE', 'BLOB_EP_URL')
QUEUE_EP_NAME = parser.get('STORAGE', 'QUEUE_EP_NAME')
FILE_EP_NAME = parser.get('STORAGE', 'QUEUE_EP_NAME')
TABLE_EP_NAME = parser.get('STORAGE', 'TABLE_EP_NAME')
SHARED_ACCESS_SIGNATURE = parser.get('STORAGE', 'SHARED_ACCESS_SIGNATURE')

# taken from ADLS2 Shared Access Policies Connection String
BLOB_STORAGE_CONNECTION_KEY = (f'BlobEndpoint=https://{BLOB_EP_URL}/;'
                               f'QueueEndpoint=https://{QUEUE_EP_NAME}/;'
                               f'FileEndpoint=https://{FILE_EP_NAME}/;'
                               f'TableEndpoint=https://{TABLE_EP_NAME}/;'
                               f'{SHARED_ACCESS_SIGNATURE}'
                               )


BLOB_RAW_CONTAINER_NAME = parser.get('STORAGE','BLOB_RAW_CONTAINER_NAME')
