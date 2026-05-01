---
title: "Redshift Spectrum"
weight: 1
---

This guide demonstrates how to set up and use Amazon Redshift Spectrum to query data from AWS Glue Data Catalog in the Manhattan DataWays project. We will use Redshift Serverless to connect and query processed taxi data through the Glue ETL pipeline.

The project includes a data lake architecture with:
- Raw data from S3
- Glue ETL jobs for data processing
- Glue Data Catalog for metadata cataloging
- Redshift Spectrum for direct queries from S3 without loading data into Redshift

# Current Data Architecture

Before setting up Redshift Spectrum, we have a complete Glue ETL pipeline running in the AWS account. This pipeline processes yellow taxi trip data with a clear separation between raw data, processed data, and quarantine data.

## S3 Buckets

We have 4 S3 buckets:

- **yellow-taxi-trip-demo-fcaj**: Contains raw data with taxi trip information organized by year/month
- **processed-yellow-taxi-trip-data**: Contains processed data after transformation
- **quarantine-yellow-taxi-trip-data**: Quarantine for data with quality issues

## Glue Crawlers

2 active crawlers:

- **glue_crawlers_data**: Crawls entire 2025 folder, target database craw_data_catalog - Status: READY/SUCCEEDED
- **glue_crawlers_data_v2_point_1_month**: Crawls January 2025 data specifically, target database glue_database_raw_data_v2 - Status: READY/SUCCEEDED

## Glue Data Catalog

2 databases with a total of 2 tables:

- **craw_data_catalog**: Contains 1 partitioned table with 48.7M records, Parquet format
- **glue_database_raw_data_v2**: Contains 1 table for January 2025 data

## Glue ETL Jobs

- **taxi-etl-job**: Script-based ETL job using Glue version 5.1, G.1X worker type with 10 workers

All resources are in the us-east-2 region. This pipeline processes yellow taxi trip data with a clear architecture separating raw, processed, and quarantine data.