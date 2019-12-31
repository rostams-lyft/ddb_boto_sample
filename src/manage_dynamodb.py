from src.client_factory import  DynamoDBClient
from src.dynamodb import DynamoDB

def get_dynamodb():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)

    return dynamodb

def create_dynamodb_table():
    dynamodb = get_dynamodb()
    table_name = "Movies"

    # define attributes
    attribute_definitions = [
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ]

    # key schema definitions
    key_schema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # Partition Key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE' # Sort Key
        }
    ]

    initial_iops = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    }

    dynamodb_create_table_response = dynamodb.create_table(table_name, attribute_definitions, key_schema, initial_iops)
    print("Created DynamoDB Table " + table_name + ":" + str(dynamodb_create_table_response))

def describe_table():
    print(str(get_dynamodb().describe_table("Movies")))


def update_table_iops():
    get_dynamodb().update_read_write_capacity("Movies", 4, 4)

def delete_table():
    get_dynamodb().delete_table_with_name("Movies")

if __name__ == '__main__':
    #create_dynamodb_table()
    #update_table_iops()
    #describe_table()
    delete_table()
