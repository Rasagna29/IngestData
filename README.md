# ingest_data_with_python

### Note: 
This project is designed for educational purposes. Redistribution, modification, or copying of this project is strictly prohibited.

### Description:
This demonstrates how to set up a DuckDB database and interact with it using Python for data ingestion. It has simple python scripts to create tables as well as ingest data based on sql insert queries to write data to these tables.

### Clone the Repository
Clone the repository to your local machine:
git clone [https://github.com/Rasagna29/ingest_data_with_python.git](https://github.com/Rasagna29/ingest_data_with_python.git)

## Installation and Setup

Follow these steps to set up the environment and tools: 

### 1. Install Homebrew (if not already installed)
Homebrew is a package manager for macOS. To install it, open the terminal and run:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### 2. Install Python (if not already installed)
Install it using Homebrew:

brew install python

### 3. Install virtual Environment  (if not already installed)
Note: A virtual environment isolates project dependencies, preventing conflicts and ensuring consistent setups across different projects.
pip install virtualenv

### 4. Set Up the Project Directory
mkdir ingest_data_with_python/

cd ingest_data_with_python/

### 5. Create and Activate a Virtual Environment
To keep the dependencies isolated, create and activate a Python virtual environment:

##### To create Python virtual environment  (this is done for each project to ensure the dependencies of this project are isolated from other projects)
python3 -m venv venv

##### To activate Python virtual environment
#### For bash/zsh users:
source venv/bin/activate  
#### For fish shell users:
source venv/bin/activate.fish

### 6. Install Required Python Libraries
Once your virtual environment is activated, install the necessary libraries for DuckDB, Pandas, Apache Airflow and Watchdog

##### pip install duckdb 

Run below to see version of duckdb
python -c "import duckdb; print(duckdb.__version__)"

##### pip install pandas 
Run below to see version of pandas
python -c "import pandas; print(pandas.__version__)"

Exit Virtual Environment
deactivate 

Exit Bash
exit

### 7. Create a Python script for the DuckDB database setup:

Create scripts directory in ingest_data_with_python/
  mkdir scripts/
  cd scripts
  nano create_tables.py (the file is already available in scripts directory in main branch)

Press Ctrl + X, type Y, and hit Enter

Return to the project root:
cd ..

Create a data directory for the database file:
mkdir data/

### 8. Run the Python Script to Create the Database
  Activate the virtual environment:
  source venv/bin/activate  

  Run the scripts to create a DuckDB database named first_database.duckdb
  The below will create orders, order_states table, and also ingest data to these tables.
    1. python /Users/rasagna/ingest_data_with_python/scripts/create_tables.py --> new database (dynamic_state_ingestion_database.duckdb) will be created in /data directory 
    2. python /Users/rasagna/ingest_data_with_python/scripts/ingest_order_data.py --> inserts data to orders table
    3. python /Users/rasagna/ingest_data_with_python/scripts/ingest_order_states_data.py --> inserts data to order_states table
    
### 9. Connect to the Database Using a Client
To connect to the database using a client:
1. Download and install DBeaver.
2. Open DBeaver and create a new database connection.
3. Select DuckDB as the database type.
4. Browse to the database file located at: /Users/rasagna/ingest_data_with_python/data/first_database.duckdb
5. You can now view the newly created tables and its columns as defined in the create_tables.py script and also data in these tables

#### Note: 
When DBeaver (or any other client) is open and you try to run Python scripts that interact with a DuckDB database, you might encounter a conflict due to DuckDB's file-based locking mechanism. DuckDB ensures that only one process can write to the database at a time. If DBeaver (or another process) has the database open, other scripts cannot access or modify the database concurrently. 
To resolve this:
   1. Close or disconnect the database in DBeaver (or the other client) before running the script.
   2. Alternatively, you can run DBeaver in read-only mode to prevent write conflicts.

Congratulations!
You have successfully created your first DuckDB database, created tables and inserted data using a Python script.




 
