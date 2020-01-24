#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json
import sys
from overtherepy import OverthereHostSession

result=""
resourceName=stack_name
stack_status=""
#aws cloudformation describe-stacks --stack-name petclinic-PetStalk-aws --query 'Stacks[0].StackStatus'
command_line = "{0} cloudformation describe-stacks --stack-name {1} --region {2}".format('aws', stack_name,deployed.container.region)
print command_line

session = OverthereHostSession(target_host)

try:
    response = session.execute(command_line, check_success=False)
    rc = response.rc
    if rc != 0:
        print "Non zero Exit Code {0}".format(rc)
        raise Exception("Non zero Exit Code {0}".format(rc))
    else:
        data = json.loads(" ".join(response.stdout))
        outputs =  data['Stacks'][0]['Outputs']
        for output in outputs:
            if output['OutputKey']=='URL':
                value = output['OutputValue']
                deployed.exposedUrl = value
                print "URL: {0}".format(value)
                print "URL: {0}".format(deployed.exposedUrl)
                print "set this url to the deployment context {0}".format(deployed.id)
                context.setAttribute(deployed.id, value)
                #repositoryService.update(deployed.id,deployed)

finally:
    session.close_conn()
