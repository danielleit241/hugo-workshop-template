---
title: "Redshift Spectrum"
weight: 1
---

Bài hướng dẫn này trình bày cách thiết lập và sử dụng Amazon Redshift Spectrum để truy vấn dữ liệu từ AWS Glue Data Catalog trong dự án Manhattan DataWays. Chúng ta sẽ sử dụng Redshift Serverless để kết nối và truy vấn dữ liệu taxi đã được xử lý thông qua Glue ETL pipeline.

Dự án này bao gồm kiến trúc data lake với:
- Dữ liệu raw từ S3
- Glue ETL job để xử lý dữ liệu
- Glue Data Catalog để catalog metadata
- Redshift Spectrum để truy vấn trực tiếp từ S3 mà không cần load dữ liệu vào Redshift

# Kiến trúc dữ liệu hiện tại

Trước khi thiết lập Redshift Spectrum, chúng ta có một Glue ETL pipeline hoàn chỉnh đang hoạt động trong tài khoản AWS. Pipeline này xử lý dữ liệu yellow taxi trip với kiến trúc phân tách rõ ràng giữa raw data, processed data và quarantine data.

## S3 Buckets

Chúng ta có 4 S3 buckets:

- **yellow-taxi-trip-demo-fcaj**: Chứa dữ liệu raw với thông tin taxi trip được tổ chức theo năm/tháng
- **processed-yellow-taxi-trip-data**: Chứa dữ liệu đã xử lý sau khi transform
- **quarantine-yellow-taxi-trip-data**: Quarantine cho dữ liệu có vấn đề về chất lượng

## Glue Crawlers

2 crawlers đang hoạt động:

- **glue_crawlers_data**: Crawl toàn bộ folder 2025, target database craw_data_catalog - Status: READY/SUCCEEDED
- **glue_crawlers_data_v2_point_1_month**: Crawl riêng dữ liệu tháng 1/2025, target database glue_database_raw_data_v2 - Status: READY/SUCCEEDED

## Glue Data Catalog

2 databases với tổng cộng 2 tables:

- **craw_data_catalog**: Chứa 1 table với dữ liệu partitioned, 48.7M records, format Parquet
- **glue_database_raw_data_v2**: Chứa 1 table cho dữ liệu tháng 1/2025

## Glue ETL Jobs

- **taxi-etl-job**: Script-based ETL job sử dụng Glue version 5.1, worker type G.1X với 10 workers

Tất cả resources đều nằm trong region us-east-2. Pipeline này xử lý dữ liệu yellow taxi trip với kiến trúc phân tách rõ ràng giữa raw data, processed data và quarantine data.