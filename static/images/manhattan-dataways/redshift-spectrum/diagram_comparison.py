from diagrams import Diagram, Cluster
from diagrams.aws.database import Redshift
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Glue
from diagrams.generic.storage import Storage

with Diagram("Traditional Redshift vs Redshift Spectrum", direction="LR", filename="redshift_comparison", show=False):
    with Cluster("Traditional Redshift"):
        traditional_redshift = Redshift("Redshift Cluster")
        local_storage = Storage("Local Storage")

    with Cluster("Redshift Spectrum"):
        spectrum_redshift = Redshift("Redshift")
        s3_storage = S3("S3 Data Lake")
        glue_catalog = Glue("Glue Catalog")
        spectrum_nodes = Storage("Spectrum Nodes")

    # Connections (though not necessary for comparison)
    traditional_redshift >> local_storage
    spectrum_redshift >> glue_catalog >> s3_storage >> spectrum_nodes