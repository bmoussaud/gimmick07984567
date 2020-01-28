echo "${data}" > resource.json

<#if operation == "CREATE">
<#assign command>create-stack</#assign>
<#else>
<#assign command>update-stack</#assign>
</#if>

echo "aws cloudformation ${command} --stack-name ${stack_name} --template-body file://resource.json --region ${deployed.container.region}"
aws cloudformation ${command} --stack-name ${stack_name} --template-body file://resource.json --region ${deployed.container.region}
