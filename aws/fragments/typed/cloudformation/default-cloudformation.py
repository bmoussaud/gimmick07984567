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
    print "default-cloudformation ctx    {0} {1}".format(ctx, type(ctx))
    print "default-cloudformation source {0} {1}".format(source, type(source))
    print "----------------------------------------------------"

    template_url = "aws/cloudformation/default_resource.json.template"
    print "template url {0}".format(template_url)
    print "----------------------------------------------------"

    template_content = load_classpath_resource(template_url)
    #print template_content
    template = Template(template_content)
    values = {}
    content = template.safe_substitute(values)
    print "-----------------"
    print content
    print "-----------------"
    print json.loads(content)
    print "-----------------"
    # it should be loaded in a template
    #template_url = "aws/cloudformation/default_resource.json.template"
    #template = Template(template_content)
    #content = template.safe_substitute(values)
    # as I don't know how to fill up the source with it, this is the code.
    source.put('AWSTemplateFormatVersion','2010-09-09')
    source.putPOJO('Resources',dict())
    source.putPOJO('Outputs', dict())

    return source
