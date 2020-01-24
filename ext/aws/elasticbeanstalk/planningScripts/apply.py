from java.io import BufferedReader
from java.io import InputStreamReader
from java.lang import StringBuilder

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


def stitchGlobalTemplate(deployed, context):

    transformerContext = {"templateNamespace": "xld-docker-compose-global",
                          "templateName": "xld-docker-compose-template-global"}

    stitchedContent = context.getArtifactTransformer("stitchEngine").transform(deployed.file.getInputStream(), transformerContext)

    return stringify(stitchedContent)







if deployed:

    #data = stitchGlobalTemplate(deployed, context)
    data = "XXXX"


    context.addStep(steps.os_script(
                            description="Deploy {0} to {1} Elastic BeanStalk".format(deployed.name, deployed.container.name),
                            target_host=deployed.container.account.awsHost,
                            script="aws/elasticbeanstalk/deploy",
                            freemarker_context={"deployedApplication": deployedApplication, 
                                "stack_name": "{0}-{1}-{2}-{3}".format(deployedApplication.environment.name,deployedApplication.version.application.name,deployed.name, deployed.container.name),
                                "operation" : delta.operation,
                                "data": data},
                            order=61))
