def stitch(ctx, source):
    print "----------------------------------------------------"
    print "default ctx {0} {1}".format(ctx, type(ctx))
    print "default source {0} {1}".format(source, type(source))
    print "----------------------------------------------------"

    nodes = source.get("services")

    if nodes:
        for n in nodes:
            image = n.get("image")
            if image:
                s = image.textValue()
                n.put("image", "benoit.docker.io/%s" % s)

    return source
