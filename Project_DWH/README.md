# Project: Data Warehouse for Sparkify

## Introduction

Sparkify, a music streaming app, has grown their user database and song database and want to move their processes and data onto the cloud. The data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in the Sparkify app.

Our task as a data engineer here is to build an ETL pipeline that extracts the data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for Sparkify's analytics team to continue finding insights into what songs their users are listening to. The database and ETL pipeline can be tested by running queries given by the analytics team from Sparkify and compare the results with their expected results.

## Project Files and Execution

- dwh.cfg - A configuration file containing AWS credential to create a Redshift cluster and access it to load data from S3.

- Create_Cluster.ipynb - A Jupyter notebook (run from local environment) for programmatic creation of the Redshift cluster (Infrastructure as Code) as well enable its deletion. The notebook handles creation of the cluster using credentials from the dwh.cfg file (read through the configparser wrapper), creates EC2, S3, IAM and Redshift resources (when run for the first time) and attaches an IAM role to the cluster for access to it and the S3 data. Optionally, the cluster can also be created from the AWS console GUI though issues are encountered in access to the cluster.

- sql_queries.py - A Python script (run from terminal) to read AWS configurations create fact and dimension tables (or drop them if they already exist) for the database and insertion of data into the tables, including all user and song details. The schema design comprises:

### Fact Table

- songplays - records in event data associated with song plays i.e. records with page NextSong
- songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables

- users - users in the app
- user_id, first_name, last_name, gender, level
- songs - songs in music database
- song_id, title, artist_id, year, duration
- artists - artists in music database
- artist_id, name, location, lattitude, longitude
- time - timestamps of records in songplays broken down into specific units
- start_time, hour, day, week, month, year, weekday

The CREATE statements include partition keys as per query requirements and the INSERT statements are written with DISTINCT to handle duplicate records. The file also contains copy commands for staging the data onto Redshift from S3. The star schema design supports denormalised tables to enable query execution without complex JOINs.

- create_tables.py - A Python script (run from terminal) to create (or drop if already exist) the tables, importing the create and drop commands from the sql_queries.py file.

- etl.py - A Python script (run from terminal) to run the ETL pipeline, importing the insert and copy commands from the sql_queries.py file, to load data from S3 to staging tables in Redshift, and then to analytics tables.  