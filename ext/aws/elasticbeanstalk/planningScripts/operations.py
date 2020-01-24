import uccm.deltas.compute

reload(uccm.deltas.compute)
from uccm.deltas.compute import DeltasBuilder, StepGenerator


class ServiceStepGenerator(StepGenerator):

    def create(self, delta, deployed, smoketest):
        context.addStepWithCheckpoint(
            steps.jython(**{'script': 'uccm/smoketest/execute-http-request.py',
                               'order': smoketest.order,
                               'description':"Run '%s' on %s" % (smoketest.name, smoketest.container.name),
                               'jython-context':{'deployed':deployed,
                                                 'smoketest':smoketest,
                                                 'template_url':'uccm/smoketest/execute-http-smoke-test.template.sh',
                                                 'target_host':deployed.container.account.awsHost       }
                            }),delta)

    def noop(self, delta, deployed, smoketest):
        self.create(delta,deployed,smoketest)



import traceback

try:
    builder = DeltasBuilder()
    list_of_deltas = builder.build2(delta.operation, deployed, previousDeployed, "smoketests")
    print "smoketests %s" % list_of_deltas
    ServiceStepGenerator(delta, list_of_deltas).generate()
except:
    raise Exception(str(traceback.format_exc()))
