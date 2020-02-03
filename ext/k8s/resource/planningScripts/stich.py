
from stitch import stitchGlobalTemplate
import json

transformerContext = {
        "templateNamespace": "xld-k8s",
        "templateName": "xld-k8s-resource-template",
        "format":"json"}

data = stitchGlobalTemplate(deployed, context, transformerContext)
resourceName=json.loads(data)['metadata']['name']
resource=json.loads(data)['kind']

context.setAttribute("document",data)
context.setAttribute("resourceName",resourceName)
context.setAttribute("resource",resource)

