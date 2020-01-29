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
    print "production-optionsbeanstalk-resources ctx    {0} {1}".format(ctx, type(ctx))
    print "production-optionsbeanstalk-resources source {0} {1}".format(source, type(source))
    print "----------------------------------------------------"

    template_url = "aws/elasticbeanstalk/production_option.json.template"
    print "template url {0}".format(template_url)
    print "----------------------------------------------------"

    template_content = load_classpath_resource(template_url)
    #print template_content
    template = Template(template_content)
    values = {'minsize': '2','maxsize':'6'}

    content = template.safe_substitute(values)
    option_settings = json.loads(content)['OptionSettings']
    opts = source.findValue("OptionSettings")
    #opts: type 'com.fasterxml.jackson.databind.node.ArrayNode'
    for entry in option_settings:
        print "-> add {0}".format(entry)
        opts.addPOJO(entry)
    
    return source
