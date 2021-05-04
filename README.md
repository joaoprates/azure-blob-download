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
