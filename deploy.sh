app="bfa"


cd bigfastapi

docker build -t $app .


helm install  $app  $app -f ./bfa/values.yaml
