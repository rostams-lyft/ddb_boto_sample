

class DynamoDB:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.dynamodb """

    def create_table(self, table, attribute_definitions, key_schema, iops):
        print("Creating DynamoDB Table")
        return self._client.create_table(
            TableName=table,
            AttributeDefinitions=attribute_definitions,
            KeySchema=key_schema,
            ProvisionedThroughput=iops
        )

    def describe_table(self, table):
        print("Describing DDB with name " + table)
        return self._client.describe_table(TableName=table)

    def update_read_write_capacity(self, table, new_read_capacity, new_write_capacity):
        print("Updating provisioned throughput of DDB table with name " + table)
        return self._client.update_table(
            TableName=table,
            ProvisionedThroughput={
                'ReadCapacityUnits': new_read_capacity,
                'WriteCapacityUnits': new_write_capacity
            }
        )

    def delete_table_with_name(self, table):
        print("Deleting DDB table: " + table)
        return self._client.delete_table(TableName=table)


