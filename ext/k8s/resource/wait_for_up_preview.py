#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json
from overtherepy import OverthereHostSession

def get_kubectl_command(container):
    kubectl = 'kubectl --namespace={0}'.format(container.name)
    if container.container.kubeConfigContext is not None:
        kubectl = kubectl + ' --context={0}'.format(deployed.container.container.kubeConfigContext)
    return kubectl



command_line = "{0} get {1} {2} -o=json".format(get_kubectl_command(deployed.container), resource, resourceName)
print command_line

