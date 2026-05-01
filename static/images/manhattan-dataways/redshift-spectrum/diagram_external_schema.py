from diagrams import Diagram
from diagrams.generic.compute import Rack
from diagrams.aws.security import IAM
from diagrams.aws.analytics import Glue
from diagrams.aws.database import Redshift
from diagrams.aws.storage import S3

with Diagram("External Schema Creation Flow", direction="LR", filename="external_schema_flow", show=False, graph_attr={'fontsize': '12', 'splines': 'ortho', 'nodesep': '0.5', 'ranksep': '1.0'}, node_attr={'fontsize': '10'}):
    iam_role = IAM("Create IAM Role\n(glue-role-manhattan-processed-crawler)")

    crawler = Glue("Create Glue Crawler\n(glue-crawler-processed-yellow-taxi)")

    run_crawler = Rack("Run Crawler")

    s3_data = S3("S3 Processed Data")

    schema = Redshift("Create External Schema\n(spectrum_processed)")

    query = Rack("Query Tables")

    iam_role >> crawler >> run_crawler >> s3_data >> schema >> query