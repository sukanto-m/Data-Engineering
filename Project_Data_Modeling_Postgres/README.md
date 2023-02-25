# Project: Data Modeling with Postgres

Sparkify - a streaming music startup - wants to analyse data being collected by them on user activity through their app. Specifically, the analytics team is interested in what kind of songs a user is listening to. At the moment, they don't have an easy way to query the data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. 

Sparkify wants a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. My role is to create a database schema and ETL pipeline for this analysis.

## Project Files and Steps

The project primarily contains the following files, apart from the user data log files in JSON format:

- sql_queries.py: A Python script to create the fact and dimension tables (or drop them if they already exist to start the data modeling process afresh) and query songs by performing JOINs across the tables.
- create_tables.py: A Python script to create (or drop) the Sparkify database and tables in Postgres using the psycopg2 wrapper. Uses sql_queries as input.
- etl.ipynb: A Jupyter notebook to read and process a single file from song_data and log_data (from the available dataset) and load them onto tables.
- etl.py: Python script to read and process files from song_data and log_data, based on code from et.ipynb
- test.ipynb: Jupyter notebook to test correct data types, constraints and upserts in the Extract Transform Load (ETL) process.

All the Python scripts can be run from the command line and Jupyter notebooks from local host. The create_tables.py file needs to be run before all other files, at least once, so that the database is created for the other files to connect to.

### Database schema and ETL pipeline design

All the fact and dimension tables have a primary key and at least one constraint for JOINs to function across tables. The tables have at least one level of normalisation with regard to the attributes. Certain tables also have ON CONFLICT clauses to resolve any clashes in the ETL process. The data types have been set in accordance with the data obtained from thr JSON files, with some emphasis on the 'timestamp' column in the 'time' table - the date, time, wwekday, year etc are extracted from the column to provide granularity of analysis on user listening patterns. The 'songplay' table serves as a sort of master table referencing data from all the other tables - hence creating a star schema for the database.

