<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#deploy-prod">Deploy to production</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- Deploy to production -->
## Deploy to production

### aws infrastructure
This project use:

* codepipeline
* eks
* ecr

#### Codepipeline - Codebuild

Click [here](https://docs.aws.amazon.com/codebuild/) to go to see the aws doc

* Create the codebuild project later go to IAM and attach the AmazonEC2ContainerRegistryPowerUser policy for the codebuild created

### EKS

* Create cluster eks with an IAM user(don't use the root account)
* Create nodes(on informatica tab):
    - create a Role(NodeInstanceRole) with the policy: AmazonEKSWorkerNodePolicy, AmazonEC2ContainerRegistryReadOnly and AmazonEKS_CNI_Polic
* We're goint to our terminal and we connect to the eks(create a new IAM user):
Install aws cli and kubectl cli on our machine
bash```
# set our credentials
aws configure
# check the credentials
aws sts get-caller-identity
# Create configuration to be able to connect to eks. kube is the name of the cluster eks
aws eks update-kubeconfig --name kube
# Test conecction
kubectl get svc
```

### Config ArgoCD
Click [here](https://argoproj.github.io/argo-cd/) to go to see the argo doc

bash```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
brew install argocd
# get default password
get pods -n argocd -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2
# create proxy
kubectl port-forward svc/argocd-server -n argocd 8080:443
# loging
argocd login localhost:8080
# update password
argocd account update-password

# forgot password?? set password to >> password
kubectl -n argocd patch secret argocd-secret   -p '{"stringData": {    "admin.password": "$2a$10$rRyBsGSHK6.uc8fntPwVIuLVHgsAhAX7TcdrqW/RADU0uh7CaChLa",    "admin.passwordMtime": "'$(date +%FT%T%Z)'"  }}'
```

### Crossplane
kubectl create namespace crossplane-system
helm repo add crossplane-alpha https://charts.crossplane.io/alpha
helm install crossplane --namespace crossplane-system crossplane-alpha/crossplane --version 0.8.0 --set clusterStacks.aws.deploy=true --set clusterStacks.aws.version=v0.6.0 --disable-openapi-validation
kubectl get pods -n crossplane-system
BASE64ENCODED_AWS_ACCOUNT_CREDS=$(echo -e "[default]\naws_access_key_id = $(aws configure get aws_access_key_id --profile default)\naws_secret_access_key = $(aws configure get aws_secret_access_key --profile default)" | base64  | tr -d "\n")

cat > aws-credentials.yaml <<EOF
---
apiVersion: v1
kind: Secret
metadata:
  name: aws-account-creds
  namespace: crossplane-system
type: Opaque
data:
  credentials: ${BASE64ENCODED_AWS_ACCOUNT_CREDS}
---
apiVersion: aws.crossplane.io/v1alpha3
kind: Provider
metadata:
  name: aws-provider-east
spec:
  credentialsSecretRef:
    name: aws-account-creds
    namespace: crossplane-system
    key: credentials
  region: us-east-1
EOF

kubectl apply -f "aws-credentials.yaml"

## Roadmap

* Use the CODEBUILD_SOURCE_VERSION into the builspec.yaml file
* To implement the ecr credential helper -> https://github.com/awslabs/amazon-ecr-credential-helper