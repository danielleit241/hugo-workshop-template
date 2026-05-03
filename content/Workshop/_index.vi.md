---
title: "Quy trình dữ liệu với AWS Glue"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

## Tổng quan

Trong workshop này, chúng ta sẽ xây dựng một pipeline phân tích dữ liệu tự động trên AWS để xử lý dữ liệu chuyến xe TLC Yellow Taxi. Giải pháp tuân theo kiến trúc serverless, event-driven, bắt đầu từ dữ liệu thô trong Amazon S3 và sử dụng Amazon EventBridge, AWS Step Functions, AWS Lambda, cùng AWS Glue DataBrew để điều phối việc nạp dữ liệu, phân tích sơ bộ, làm sạch, xác thực và chuyển đổi dữ liệu.

Sau khi dữ liệu được xử lý, nó sẽ được lưu vào lớp S3 processed và nạp vào Amazon Redshift cho các tác vụ OLAP, đồng thời Amazon Athena sẽ hỗ trợ truy vấn SQL ad-hoc trực tiếp trên S3. Cuối cùng, Amazon QuickSight sẽ được dùng để xây dựng dashboard tương tác phục vụ phân tích kinh doanh, còn IAM, CloudTrail, CloudWatch và SNS sẽ đảm nhiệm bảo mật, kiểm toán, giám sát và cảnh báo trong toàn bộ quy trình.

![Architecture](/images/Proposal/diagram-architecture.jpg)

## Nội dung

1. [Giới thiệu](1-Introduction/)
2. [Chuẩn bị](2-Preparation/)
3. [Giám sát và Bảo mật](3-MonitoringSecurity/)
4. [Pipeline phân tích dữ liệu](4-AnalyticsPipeline/)
5. [Trí tuệ doanh nghiệp](5-BusinessIntelligence/)
