from azure.storage.blob import BlobClient
import os
from azure.storage.blob import ContainerClient

def main(container_name):
    """
    Main
        Args:
            :param container_name
                Container Name of connection
    """
    connection_string = read_config_file(".connection")

    container = ContainerClient.from_connection_string(
        conn_str=connection_string, container_name=container_name)

    blob_list = container.list_blobs()

    for blob in blob_list:
        create_folders(blob.name)
        create_file_blob(connection_string, blob, container_name)

def create_file_blob(connection_string, blob, container_name):
    """
    Create File of blob
        Args:
            :param connection_string
                Value of connection string
            :param blob
                Object Blob
            :param container_name
                Name of container

    """
    file = BlobClient.from_connection_string(
        conn_str=connection_string, container_name=container_name, blob_name=blob.name)
    with open("./" + blob.name, "wb") as my_blob:
        blob_data = file.download_blob()
        blob_data.readinto(my_blob)

def create_folders(name):
    """
    Create the folder's structures necessary
        Args:
            :param name
                Blob name with folders structures
    """

    split = name.split("/")

    if(len(split) > 1):
        folder_name = ""
        value_range = len(split) - 1
        for i in range(0, value_range):
            folder_name += split[i] + "/"

        if(os.path.exists("./" + folder_name) is False):
            os.makedirs("./" + folder_name)


def read_config_file(name_file):
    """
    Read the config file
        Args:
            :param name_file
                Name of config file
        Return:
            Value of connection string
    """

    connection_string = ""

    if(os.path.exists("./" + name_file) is True):
        with open(name_file, 'r') as reader:
            connection_string += reader.read()

    return connection_string


if __name__ == "__main__":
    main("teste")
