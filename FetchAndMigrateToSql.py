import pymongo
from ChannelData import fetch_channel_info
from SqlTableCreation import create_tables
from MongoToSql import migrate_to_sql

def fetch_migrate(api_key, channel_ids):
    print("\nFetching channel data process started\n")
    print('Received channel_ids: ', channel_ids)
    fetch_channel_info(api_key, channel_ids)
    print("\nFetching channel data process completed\n")
    create_tables()
    print("\nMigration process from mongo to sql started\n")
    migrate_to_sql(channel_ids)
    print("\nMigration process from mongo to sql completed\n")
    return "Finished fetching channel data, stored into mongo db and migrated to SQL"
