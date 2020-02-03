#set -x
echo '${data}' > ./document.json
cat -n ./document.json
kubectl --context="${deployed.container.container.kubeConfigContext}" apply -f ./document.json -n ${deployed.container.name}
