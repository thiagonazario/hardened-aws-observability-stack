# AWS Hardened Observability Stack 🛡️📊

**Methodology:** Hardened by Design & DevSecOps Standards
**Engine:** Pulumi + Python (Infrastructure as Code)

This repository implements a production-ready AWS infrastructure focused on the **Service Trinity** (Logs, Metrics, Tracing) with a zero-trust networking approach.

## 🏗️ The Architecture
Deployed in 24 seconds, the stack enforces:
- **Private-First VPC:** No public IP mapping, high-security tagging.
- **FinOps Optimized Tracing:** AWS X-Ray sampling rules set to 5% to balance visibility and cost.
- **Centralized Monitoring:** Custom CloudWatch Dashboards for Core Service Health.

## 🛡️ Hardened Features
- [x] **Isolation:** Resources deployed in private subnets without IGW exposure.
- [x] **Traceability:** Sampling rules labeled with `Standard: DevSecOps`.
- [x] **Automation:** Pure Python logic for complex infrastructure orchestration.

## 📸 Proof of Concept
| X-Ray Sampling Rule | Hardened VPC Map |
|---|---|
| ![X-Ray Proof](./img/xray-sampling.png) | ![VPC Proof](./img/vpc-map.png) |

---
*Created by the Ghost Architect.*
