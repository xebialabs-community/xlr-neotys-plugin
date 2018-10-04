#
# Copyright 2018 NEOTYS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys
from com.neotys.xebialabs.xl import NeoLoadUpdateVars

if ConstantVariableName is None:
    print "No Variable Name defined"
    sys.exit(1)

if ConstantVariableValue is None:
    print "No Variable Name defined"
    sys.exit(1)

Vars= NeoLoadUpdateVars(ConstantVariableName,ConstantVariableValue)
releaseid=getCurrentRelease().id
variables=releaseApi.getVariables(releaseid)
CreateVar=True

for var in variables :
    if var.key == 'NeoLoadVariable':
        Vars.SetExistingVars(var.value)
        Neoloadupdated=var
        CreateVar=False

response=Vars.UpdateVariable()


if CreateVar == True :
    NeoLoadVar=Variable('NeoLoadVariable', response.ymlContent)
    releaseApi.createVariable(releaseid, NeoLoadVar)
else:
    Neoloadupdated.value=response.ymlContent
    releaseApi.updateVariable( Neoloadupdated)


# set variables
responseCode = response.getResponseCode()
output = response.getStdout()
error = response.getStderr()


if responseCode == 0:
    print output
else:
    print "Exit code "
    print responseCode
    print
    print "#### Output:"
    print output

    print "#### Error stream:"
    print error
    print
    print "----"

    sys.exit(responseCode)