import pulumi
import pulumi_aws as aws
from modules.networking import HardenedNetwork

# Initialize Network
network = HardenedNetwork("ghost-obs")

# 1. LOGS: CloudWatch Log Group with Retention (FinOps)
log_group = aws.cloudwatch.LogGroup("hardened-app-logs",
    retention_in_days=30, # FinOps: 
    tags={"Project": "Hardened-Observability"})

# 2. METRICS: Dashboard basic
dashboard_body = {
    "widgets": [{
        "type": "metric",
        "x": 0, "y": 0, "width": 12, "height": 6,
        "properties": {
            "metrics": [["AWS/EC2", "CPUUtilization"]],
            "period": 300,
            "stat": "Average",
            "region": "us-east-1",
            "title": "Core Service Health"
        }
    }]
}

obs_dashboard = aws.cloudwatch.Dashboard("service-trinity-dash",
    dashboard_name="Service-Trinity-Main-Metrics",
    dashboard_body=pulumi.Output.json_dumps(dashboard_body))

# 3. TRACING: X-Ray
xray_sampling_rule = aws.xray.SamplingRule("hardened-sampling",
    rule_name="GhostArchitectRule",
    version=1,
    priority=1000,
    reservoir_size=1,
    fixed_rate=0.05, # Just 5% (FinOps!)
    url_path="*",
    host="*",
    http_method="*",
    service_type="*",
    service_name="*",
    resource_arn="*",
    attributes={"Standard": "DevSecOps"})

# EXPORTS
pulumi.export("vpc_id", network.vpc.id)
pulumi.export("log_group_name", log_group.name)
pulumi.export("dashboard_url", obs_dashboard.id)