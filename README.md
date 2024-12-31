# hearth

Build a local chat room with Llama based bot feature accessible via Wifi.

Tech Stack
- Starlette for minimal web server
- Postgres (could be NoSQL, could be moved free managed source like railway)
- std html, css, js for frontend. With htmx and lightweight frameworks like alpine
- Containerized with Docker
- Deployed with k8s along with ArgoCD. (microk8s or something similar)

Specialities about the project.

I'm building it mainly to test my newly acquired skills and deep dive into it.

- End to End project with main focus on backend concepts.
- Fully async server including the DB client.
- try out uv for package management.
- websocket support.
- Redis for caching.
- Background workers.
- Starlette, Redis, ChromaDB, Postgres, Nginx container setup.
- Logging to sentry.
- Possibly Oauth with gmail. Not mandatory.
- Proper test suite.
- Proper markdown docs.
- cicd for linting checks.
- Deployment to GKE with GCP free credits
- maybe terraform for provisioning some AWS resources like ECR, Bucket, SSM

Road to k8s deployment
[x] - Docker
[ ] - Docker optimization
[ ] - local k8s setup
[ ] - terraform for AWS resources
[ ] - helm chart
[ ] - manual deployment
[ ] - Argo, csi secrets store, istio setup
[ ] - cicd for docker build and push, argo sync
[ ] - GKE setup
