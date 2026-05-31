from kubernetes import client, config

# Load in-cluster configuration
config.load_incluster_config()

# Create a Kubernetes API client
v1 = client.AppsV1Api()

# List deployments in the default namespace
deployments = v1.list_namespaced_deployment(namespace="default")

# Extract the latest release tag from the deployments
release_tag = None
for deployment in deployments.items:
    if deployment.metadata.name == "my-deployment":
        # Extract the image tag from the deployment spec
        image_tag = deployment.spec.template.spec.containers[0].image
        release_tag = image_tag.split(":")[-1]

# Print the release tag
print(release_tag)
```
execution trace:
stdout:
v1.18.10

stderr:


return code: 0