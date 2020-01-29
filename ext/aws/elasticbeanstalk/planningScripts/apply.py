from java.io import BufferedReader
from java.io import InputStreamReader
from java.lang import StringBuilder
from overtherepy import LocalConnectionOptions, OverthereHost, OverthereHostSession
from com.xebialabs.overthere import OperatingSystemFamily
import json

def stringify(stream):
    reader = BufferedReader(InputStreamReader(stream))
    out = StringBuilder()

    while True:
        line = reader.readLine()
        if line is None:
            break
        out.append(line)
        out.append("\n")

    reader.close()
    return out.toString()


def content_to_file(input_content):
    localOpts = LocalConnectionOptions(os=OperatingSystemFamily.UNIX)
    host = OverthereHost(localOpts)
    session =  OverthereHostSession(host)  
    input_file = session.get_conn().getTempFile("a_json_file", ".json")
    session.copy_text_to_file(input_content,input_file)
    print ("input_file is {0}".format(input_file))
    return input_file
   


def stitchGlobalTemplateString(input_content, context, transformer_context):
    print("--> stich {0}".format(transformer_context))
    stitchedContent = context.getArtifactTransformer("stitchEngine").transform(content_to_file(input_content).getInputStream(), transformer_context)
    return stringify(stitchedContent)



initial_data = json.dumps(dict())
transformerContext = {
        "templateNamespace": "xld-aws-beanstalk-global",
        "templateName": "xld-aws-beanstalk-template-global",
        "format":"json"}

data = stitchGlobalTemplateString(initial_data, context, transformerContext)


if "prod" in deployedApplication.environment.name:
    print "===================== PRODPRODPROD"
    transformerContextProd = {
        "templateNamespace": "xld-aws-beanstalk-global",
        "templateName": "xld-aws-beanstalk-template-prod",
        "format":"json"}
    data = stitchGlobalTemplateString(data, context, transformerContextProd)

print ("--- OUTPUT ---")
print (data)
print ("--- /OUTPUT ---")
print deployedApplication.environment.name
print "prod" in deployedApplication.environment.name


context.addStep(steps.os_script(
    description="Deploy {0} to {1} Elastic BeanStalk".format(deployed.name, deployed.container.name),
    target_host=deployed.container.account.awsHost,
    script="aws/elasticbeanstalk/deploy",
    freemarker_context={ 
        "stack_name": "{0}-{1}-{2}-{3}".format(deployedApplication.environment.name,deployedApplication.version.application.name,deployed.name, deployed.container.name),
        "operation" : delta.operation,
        "data": data},
    order=61))
