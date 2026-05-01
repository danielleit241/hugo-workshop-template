from diagrams import Diagram, Cluster
from diagrams.aws.database import Redshift
from diagrams.aws.security import IAM
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Glue
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack

with Diagram("Redshift Serverless Architecture", direction="LR", filename="redshift_serverless_architecture", show=False, graph_attr={'fontsize': '12', 'splines': 'ortho', 'nodesep': '0.5', 'ranksep': '1.0'}, node_attr={'fontsize': '10'}):
    database = Storage("Database Objects")
    users = IAM("Users & Permissions")
    roles = IAM("IAM Roles")
    metadata = Storage("Metadata & Encryption")

    compute = Redshift("Compute Engine\n(4 RPU)")
    endpoint = Rack("Connection Endpoint")
    monitoring = Rack("Query Monitoring")

    iam_role = IAM("IAM Role")
    s3 = S3("S3 Buckets")
    glue = Glue("Glue Catalog")

    # Connections to ensure horizontal flow
    database >> compute
    users >> compute
    roles >> compute
    metadata >> compute
    compute >> iam_role >> s3 >> glue
    endpoint >> compute
    monitoring >> compute