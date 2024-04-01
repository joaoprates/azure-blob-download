Azure Blob Storage Downloader
This project is a Python application that downloads blobs from an Azure Blob Storage container to your local machine. It also sets metadata for each blob and copies them to a second Azure Blob Storage account.

Setup
Before running the application, you need to create a .connection file in the root directory of the project. This file should contain the connection string for your Azure Blob Storage account. The connection string should look something like this:

You can find the connection string in the Azure portal:

Navigate to your storage account in the Azure portal.
Click on the "Access keys" option under the "Settings" section.
Here you can see your account name, key, and connection string.
How it works
The application works by first reading the connection string from the .connection file. It then creates a ContainerClient for the specified container in your Azure Blob Storage account.

The application lists all the blobs in the container and downloads each one to your local machine. It creates the necessary directories for each blob based on its name.

After downloading a blob, the application sets some metadata for it. The metadata is a dictionary of key-value pairs. You can modify the metadata in the main function.

Finally, the application copies each blob to a second Azure Blob Storage account. You need to provide the connection string for the second account in the main function.

Running the application
To run the application, you need to have Python installed on your machine. You also need to install the azure-storage-blob package, which you can do with the following command:

Once you have Python and azure-storage-blob installed, you can run the application with the following command:

Replace client_azure_blob.py with the name of the Python file that contains the main function.

Note
This application is a simple example of how to work with Azure Blob Storage in Python. It's not intended for use in production environments. Always make sure to secure your connection strings and other sensitive data.

**Azure Blob Client**

Client to download Files from Storage "Azure Blob"

**Instalation**

python.exe -m pip install azure-storage-blob

**Config File**

It is necessary to have a .connection file, with the value of the connection string for connection

**Container Name**

main("teste")

**Methods** 

- read_config_file - Reads the .connection configuration file to read a connection string
- create_folders - Creates the folder structure for downloading the file
- create_file_blob - Download the file
- main - Main method for running the script
- Executes the script, passing the name of the container
