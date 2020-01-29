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


def empty_json_file():
    localOpts = LocalConnectionOptions(os=OperatingSystemFamily.UNIX)
    host = OverthereHost(localOpts)
    session =  OverthereHostSession(host)  
    input_file = session.upload_text_content_to_work_dir(json.dumps(dict()),"empty_json_file.json",executable=False)
    print ("input_file is {0}".format(input_file))
    return input_file
   

def stitchGlobalTemplate(input_file, context):

    transformerContext = {
            "templateNamespace": "xld-aws-beanstalk-global",
            "templateName": "xld-aws-beanstalk-template-global",
            "format":"json"}

    
    stitchedContent = context.getArtifactTransformer("stitchEngine").transform(input_file.getInputStream(), transformerContext)

    return stringify(stitchedContent)



data = stitchGlobalTemplate(empty_json_file(), context)

print ("--- OUTPUT ---")
print (data)
print ("--- /OUTPUT ---")

context.addStep(steps.os_script(
    description="Deploy {0} to {1} Elastic BeanStalk".format(deployed.name, deployed.container.name),
    target_host=deployed.container.account.awsHost,
    script="aws/elasticbeanstalk/deploy",
    freemarker_context={"deployedApplication": deployedApplication, 
        "stack_name": "{0}-{1}-{2}-{3}".format(deployedApplication.environment.name,deployedApplication.version.application.name,deployed.name, deployed.container.name),
        "operation" : delta.operation,
        "data": data},
    order=61))
