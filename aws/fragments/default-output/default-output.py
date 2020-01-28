import json
import sys
from overtherepy import OverthereHostSession
from com.google.common.io import Resources
from java.nio.charset import Charset
from string import Template
from java.lang import Thread, Integer

def load_classpath_resource(resource):
    """
    Uploads the classpath resource to the session's working directory.
    :param resource: to find on the classpath to copy
    :return: string
    """
    url = Thread.currentThread().contextClassLoader.getResource(resource)
    if url is None:
        raise Exception("Resource [%s] not found on classpath." % resource)

    return Resources.toString(url, Charset.defaultCharset())

def stitch(ctx, source):
    print "----------------------------------------------------"
    print "output ctx    {0} {1}".format(ctx, type(ctx))
    print "output source {0} {1}".format(source, type(source))
    print "----------------------------------------------------"

    template_url = "aws/elasticbeanstalk/default_output.json.template"
    print "template url {0}".format(template_url)
    print "----------------------------------------------------"

    template_content = load_classpath_resource(template_url)
    #print template_content
    template = Template(template_content)
    values = {'application': 'PetClinic',
          'environment':'DEV', 
          'version':'1.0', 
          'region':'paris', 
          'file':'PetClinic.War', 
          'solutionStackName':'Tomcat 8'}

    content = template.safe_substitute(values)
    print "-----------------"
    print content
    print "-----------------"
    outputs = json.loads(content)['Outputs']
    print outputs
    print "-----------------"

    source.putPOJO('Outputs',outputs)

    return source
