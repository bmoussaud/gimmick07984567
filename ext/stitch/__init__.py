
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



def stitchGlobalTemplate(deployed, context, transformerContext):
    print "stitchGlobalTemplate {0}".format(transformerContext)
    stitchedContent = context.getArtifactTransformer("stitchEngine").transform(deployed.file.getInputStream(), transformerContext)
    return stringify(stitchedContent)



