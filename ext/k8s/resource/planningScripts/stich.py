
from stitch import stitchGlobalTemplate
import json

mandatory_transformer_context ={
        "templateNamespace": "xld-k8s",
        "templateName": "xld-k8s-mandatory-template",
        "format":"json"}


if deployedApplication.environment.enableStitch:

    transformerContext ={
            "templateNamespace": "xld-k8s",
            "templateName": "xld-k8s-resource-template",
            "format":"json"}

    data = stitchGlobalTemplate(deployed, context, transformerContext)
else:
    data = stitchGlobalTemplate(deployed, context, mandatory_transformer_context)



resourceName=json.loads(data)['metadata']['name']
resource=json.loads(data)['kind']

context.setAttribute("document",data)
context.setAttribute("resourceName",resourceName)
context.setAttribute("resource",resource)
