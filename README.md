# IngestDataWithPython

This project is designed for educational purposes. It demonstrates how to set up a DuckDB database and interact with it using Python for data ingestion. Redistribution, modification, or copying of this project is strictly prohibited.

### 1. Clone the Repository
Clone the repository to your local machine:
git clone [https://github.com/Rasagna29/IngestDataWithPython.git](https://github.com/Rasagna29/IngestDataWithPython.git)

## Installation and Setup

Follow these steps to set up the environment and tools:

### 1. Install Homebrew (if not already installed)
Homebrew is a package manager for macOS. To install it, open the terminal and run:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### 2. Install Python (if not already installed)
Install it using Homebrew:

brew install python

### 3. Install virtual Environment
pip install virtualenv

### 4. Set Up the Project Directory
mkdir ingest_data/

cd ingest_data/

### 5. Create and Activate a Virtual Environment
To keep the dependencies isolated, create and activate a Python virtual environment:

To create Python virtual environment 
python3 -m venv venv

To activate Python virtual environment
#### For bash/zsh users:
source venv/bin/activate  
#### For fish shell users:
source venv/bin/activate.fish

### 6. Install Required Python Libraries
Once your virtual environment is activated, install the necessary libraries for DuckDB, Pandas, and Apache Airflow:

pip install duckdb 

Run below to see version of duckdb
python -c "import duckdb; print(duckdb.__version__)"

pip install pandas 
Run below to see version of pandas
python -c "import pandas; print(pandas.__version__)"

pip install apache-airflow
Run below to see version of airflow
python -c "import airflow; print(airflow.__version__)"

Exit Virtual Environment
exit

### 7. Create a Python script for the DuckDB database setup:

Create scripts directory in ingest_data/
  mkdir scripts/
  cd scripts
  nano create_duckdb_db.py (content of file available in scripts directory in main branch)

Press Ctrl + X, type Y, and hit Enter

Return to the project root:
cd ..

Create a data directory for the database file:
mkdir data/

### 8. Run the Python Script to Create the Database
  Activate the virtual environment:
    source venv/bin/activate  

  Run the script to create a DuckDB database named first_database.duckdb
    python /Users/rasagna/ingest_data/scripts/create_duckdb_db.py

### 9. Connect to the Database Using a Client
To connect to the database using a client:
1. Download and install DBeaver.
2. Open DBeaver and create a new database connection.
3. Select DuckDB as the database type.
4. Browse to the database file located at: /Users/rasagna/ingest_data_with_python/data/first_database.duckdb
5. You can now view the newly created table and its columns as defined in the create_duckdb_db.py script.

Congratulations!
You have successfully created a DuckDB database using a Python script and connected to it with DBeaver.


