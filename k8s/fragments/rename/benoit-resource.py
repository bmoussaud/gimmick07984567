def stitch(ctx, source):
    print "----------------------------------------------------"
    print "benoit-resource ctx    {0} {1}".format(ctx, type(ctx))
    print "benoit-resource source {0} {1}".format(source, type(source))
    print "----------------------------------------------------"
    metadata_node = source.path("metadata")
    prefix = "benoit"
    new_name = "{0}-{1}".format(prefix,metadata_node.get("name").textValue())
    new_name = new_name.replace("-",".")
    metadata_node.put('name', new_name)
    return source
