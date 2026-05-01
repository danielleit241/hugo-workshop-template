from diagrams import Diagram
from diagrams.generic.compute import Rack

with Diagram("Redshift Serverless Setup Flow", direction="LR", filename="redshift_setup_flow", show=False, graph_attr={'fontsize': '12', 'splines': 'ortho', 'nodesep': '0.5', 'ranksep': '1.0'}, node_attr={'fontsize': '10'}):
    access = Rack("1. Access Redshift Console")

    customize = Rack("2. Click 'Customize settings'")

    namespace = Rack("3. Configure Namespace\n(name, database, credentials)")

    workgroup = Rack("4. Configure Workgroup\n(name, capacity to 4 RPU)")

    iam = Rack("5. Create IAM Role\n(for S3 & Glue access)")

    network = Rack("6. Configure Network\n(VPC, security)")

    create = Rack("7. Save Configuration")

    wait = Rack("8. Wait for Workgroup\nStatus: Available")

    complete = Rack("Setup Complete")

    access >> customize >> namespace >> workgroup >> iam >> network >> create >> wait >> complete