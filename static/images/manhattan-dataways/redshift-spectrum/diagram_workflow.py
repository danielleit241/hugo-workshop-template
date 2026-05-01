from diagrams import Diagram, Cluster
from diagrams.aws.database import Redshift
from diagrams.aws.analytics import Glue
from diagrams.aws.storage import S3
from diagrams.generic.compute import Rack

with Diagram("Redshift Spectrum Workflow", direction="LR", filename="redshift_spectrum_workflow", show=False):
    user = Rack("User/Client")

    with Cluster("Redshift Cluster"):
        redshift = Redshift("Redshift")

    glue = Glue("Glue Data Catalog")

    s3 = S3("S3 Data Lake")

    spectrum_nodes = Rack("Spectrum Nodes")

    # Flow of the process
    user >> redshift >> glue >> s3 >> spectrum_nodes >> redshift >> user

    # Labels for steps
    redshift - glue
    glue - s3
    s3 - spectrum_nodes
    spectrum_nodes - redshift