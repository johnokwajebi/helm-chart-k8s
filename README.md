# Helm-Charts-K8s


# How to run the project before deploying the Helm Chart 

1. Create a virtual environment with `python3 -m venv env`
2. Change directory into bigfastapi `cd bigfastapi`
3. Activate the virtual environment using `.\env\bin\Activate.ps1` (windows) or `source /path/to/venv/bin/activate` (linux/mac)
4. Pull the latest commits from origin.
5. run `pip install -r requirements.txt`
6. Create a .env file by copying the .env.sample file
7. Run `python main.py`. Check the code to understand how to use the library


# Documentation

When you run the sample code, visit http://127.0.0.1:7001/docs to view the documentation for all endpoints

# Helm Chart

- Helm chart contains 2 deployments (bfa1 and bfa2) which uses one image named bfa.

- Configmaps which contains the configurations for both deployments

- Ingress which sends request to only bfa1. This can be updated to send request to the bfa2 by disabling ingress in bfa1 and enabling ingress in bfa in the `.bigfastapi/bfa/values.yaml` file. Run `helm upgrade bfa bfa -f ./bfa/values.yaml` in the bigfastapi folder to update the changes.

- Cronjob, which is executed once a day (the image is the same as in the deployments, but with the cronjob parameter)

# Running the Helm Chart

- There's a bash script `deploy.sh` to automate the build of the docker image and deploys the helm chart.
- The chart values and template can be found in `./bigfastapi/bfa`


# Documentation
To visit the api via the ingress host

- Add this line  `127.0.0.1  bigfastapi.info` to `/etc/hosts`

When you run the sample code, visit http://bigfastapi.info/docs to view the documentation for all endpoints
