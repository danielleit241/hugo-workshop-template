---
title: "Introduction"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

### Workshop này sẽ sử dụng các AWS resources và công cụ sau:

- **Amazon S3**: Amazon Simple Storage Service (S3) cung cấp khả năng lưu trữ đối tượng có thể mở rộng cho dữ liệu, file xuất ra, và các tài nguyên sử dụng trong toàn bộ workshop. Đây là nền tảng để lưu trữ dữ liệu đầu vào và các file trung gian một cách bền vững và có tính sẵn sàng cao.

- **EventBridge và Step Functions**: Amazon EventBridge giúp định tuyến sự kiện giữa các dịch vụ AWS, trong khi AWS Step Functions cho phép bạn điều phối các workflow nhiều bước một cách trực quan và đáng tin cậy. Kết hợp lại, chúng giúp tự động hóa toàn bộ luồng xử lý theo sự kiện trong giải pháp.

- **AWS Lambda**: AWS Lambda chạy mã mà không cần provision hay quản lý máy chủ. Trong workshop này, Lambda có thể được dùng để xử lý sự kiện, chuyển đổi dữ liệu, và kết nối các dịch vụ bằng các hàm serverless nhẹ.

- **AWS Glue DataBrew**: AWS Glue DataBrew là công cụ chuẩn bị dữ liệu trực quan giúp làm sạch và chuẩn hóa dữ liệu mà không cần viết code. Công cụ này rất hữu ích để phân tích sơ bộ và xử lý dữ liệu thô trước khi đưa vào các dịch vụ phân tích phía sau.

- **Amazon Redshift**: Amazon Redshift là dịch vụ data warehouse được quản lý toàn phần, được thiết kế cho phân tích dữ liệu quy mô lớn. Nó cho phép truy vấn nhanh trên dữ liệu có cấu trúc và hỗ trợ các workload business intelligence.

- **Amazon Athena**: Amazon Athena là dịch vụ truy vấn tương tác cho phép phân tích dữ liệu lưu trong Amazon S3 bằng SQL tiêu chuẩn. Đây là lựa chọn rất phù hợp để khám phá dữ liệu nhanh mà không cần thiết lập hạ tầng.

- **Amazon QuickSight**: Amazon QuickSight là dịch vụ business intelligence trên cloud dùng để tạo dashboard và biểu đồ trực quan. Nó giúp trình bày kết quả phân tích ở định dạng dễ hiểu cho người dùng kinh doanh và các bên liên quan.

- **IAM, CloudTrail, CloudWatch, và SNS**: AWS Identity and Access Management (IAM) kiểm soát quyền truy cập vào tài nguyên AWS, AWS CloudTrail ghi lại hoạt động tài khoản phục vụ kiểm toán, Amazon CloudWatch giám sát log và metrics, còn Amazon SNS gửi thông báo để bạn luôn được cập nhật về các sự kiện quan trọng.