# BultShield controlled demonstration

This repository contains synthetic scanner fixtures owned by the BultShield author.
The `vulnerable` branch is intentionally unsafe and must never be deployed.
The `fixed` branch removes the controlled issues. No real credentials are included.

- Gitleaks: a deliberately invented, nonfunctional GitHub-shaped token.
- Semgrep: unsafe eval in a parsing function; fixed uses JSON and validates the result.
- Trivy: an intentionally old dependency plus a root/latest Dockerfile; fixed removes the unused dependency and adds non-root/healthcheck configuration.
- Nuclei: register the separately authorized BultShield staging URL. Header evidence belongs to that deployed URL, not to this repository commit.

Do not install vulnerable dependencies or execute repository code as part of a scan.
Compare commit SHA and branch in BultShield. AI fixes require review and an isolated rescan.
