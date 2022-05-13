# Helm-Charts-K8s


# How to run the project before deploying the Helm Chart 

1. Create a virtual environment with `python3 -m venv env`
2. Change directory into bigfastapi `python3 -m venv env`
3. Activate the virtual environment using `.\env\bin\Activate.ps1` (windows) or `source /path/to/venv/bin/activate` (linux/mac)
4. Pull the latest commits from origin.
5. run `pip install -r requirements.txt`
6. Create a .env file by copying the .env.sample file
7. Run `python main.py`. Check the code to understand how to use the library


# Documentation

When you run the sample code, visit http://127.0.0.1:7001/docs to view the documentation for all endpoints

# Helm Chart

- 2 deployments (api, background), each deployment uses one image but with different launch parameters (api, background)
- configmap for config file
- Ingress which sends requests to pods with API only
- Cronjob, which is executed once a day (the image is the same as in the deployments, but with the cronjob parameter)


- Helm chart contains 2 deployments (bfa1 and bfa2) which uses one image named bfa.

- Configmaps which contains the configurations for both deployments

- Ingress which sends request to only bfa1. This can be updated to send request to the bfa2 by disabling ingress in bfa1 and enabling ingress in bfa by running helm upgrade bfa bfa -f ./bfa/values.yaml

- Cronjob, which is executed once a day (the image is the same as in the deployments, but with the cronjob parameter)

# Running the Helm Chart

There's a bash script `deploy.sh` to automate the build of the docker image and deploys the helm chart.


# Documentation
To visit the api via the ingress host

add this line  `127.0.0.1  bigfastapi.info` to `/etc/hosts`

When you run the sample code, visit http://bigfastapi.info/docs to view the documentation for all endpoints
