# GuviDataHarvestWareHouse

## Overview

This repository contains scripts to fetch data from 10 YouTube channels and store it in a MongoDB database. Additionally, it provides instructions for migrating data from MongoDB to SQL and displaying questions and answers using a Streamlit interface.

## Data Retrieval

To retrieve data from YouTube channels and store it in MongoDB, execute the following command:

Run the `ChannelData.py` script:

   ```shell
   python ChannelData.py

This command will create a MongoDB database named "youtube" and a collection named "channels" to store the fetched data.

## Data Migration

To migrate data from MongoDB to SQL, follow these instructions:

1. Create SQL tables by running:

   ```shell
   python SqlTableCreation.py

2. Migrate data from MongoDB to SQL using:

   ```shell
   python MongoToSql.py


