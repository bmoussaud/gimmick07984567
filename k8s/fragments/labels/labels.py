def stitch(ctx, source):
    print "----------------------------------------------------"
    print "labels ctx    {0} {1}".format(ctx, type(ctx))
    print "labels source {0} {1}".format(source, type(source))
    print "----------------------------------------------------"
    nodes = source.findValues("labels", None)
    for n in nodes:
        print("sitch {0}".format(n))
        n.put("deployed_by","xl-deploy-9.5.1")
    return source
