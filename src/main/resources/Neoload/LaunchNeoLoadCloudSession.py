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
from com.neotys.xebialabs.xl import NeoLoadCloudPlatform

if NeoLoadCloudWorkGroup is None:
    print "No NeoLoadCloudWorkGroup defined"
    sys.exit(1)


#--------add trhe release id and title
# ->${release.id}
#Gayatree ->${release.title}
session=NeoLoadCloudPlatform(NeoLoadCloudWorkGroup, NeoLoadCloudDuration, NeoLoadCloudType)
if ap_northeast_1 is not None :
    session.addCloudLocation("ap_northeast_1", ap_northeast_1)
if ap_northeast_4 is not None :
    session.addCloudLocation("ap_northeast_4", ap_northeast_4)
if ap_south_2 is not None :
    session.addCloudLocation("ap_south_2", ap_south_2)
if ap_southeast_1 is not None :
    session.addCloudLocation("ap_southeast_1", ap_southeast_1)
if ap_southeast_3 is not None :
    session.addCloudLocation("ap_southeast_3", ap_southeast_3)
if eu_center_2 is not None :
    session.addCloudLocation("eu_center_2", eu_center_2)
if eu_west_1 is not None :
    session.addCloudLocation("eu_west_1", eu_west_1)
if eu_west_12 is not None :
    session.addCloudLocation("eu_west_12", eu_west_12)
if na_northeast_5 is not None :
    session.addCloudLocation("na_northeast_5", na_northeast_5)
if sa_east_1 is not None :
    session.addCloudLocation("sa_east_1", sa_east_1)
if us_east_1 is not None :
    session.addCloudLocation("us_east_1", us_east_1)
if us_east_8 is not None :
    session.addCloudLocation("us_east_8", us_east_8)
if us_west_1 is not None :
    session.addCloudLocation("us_west_1", us_west_1)
if us_west_2 is not None :
    session.addCloudLocation("us_west_2", us_west_2)
if us_northcentral_1 is not None :
    session.addCloudLocation("us_northcentral_1", us_northcentral_1)
if us_southcentral_1 is not None :
    session.addCloudLocation("us_southcentral_1", us_southcentral_1)
if us_east_5 is not None :
    session.addCloudLocation("us_east_5", us_east_5)
if ap_east_2 is not None :
    session.addCloudLocation("ap_east_2", ap_east_2)
if eu_west_2 is not None :
    session.addCloudLocation("eu_west_2", eu_west_2)
if eu_center_1 is not None :
    session.addCloudLocation("eu_center_1", eu_center_1)
if ap_east_1 is not None :
    session.addCloudLocation("ap_east_1", ap_east_1)
if ap_northeast_2 is not None :
    session.addCloudLocation("ap_northeast_2", ap_northeast_2)
if ap_northeast_3 is not None :
    session.addCloudLocation("ap_northeast_3", ap_northeast_3)
if ap_northeast_5 is not None :
    session.addCloudLocation("ap_northeast_5", ap_northeast_5)
if ap_northeast_6 is not None :
    session.addCloudLocation("ap_northeast_6", ap_northeast_6)
if ap_south_3 is not None :
    session.addCloudLocation("ap_south_3", ap_south_3)
if ap_south_4 is not None :
    session.addCloudLocation("ap_south_4", ap_south_4)
if ap_southeast_2 is not None :
    session.addCloudLocation("ap_southeast_2", ap_southeast_2)
if ap_southeast_6 is not None :
    session.addCloudLocation("ap_southeast_6", ap_southeast_6)
if ap_southeast_7 is not None :
    session.addCloudLocation("ap_southeast_7", ap_southeast_7)
if eu_west_5 is not None :
    session.addCloudLocation("eu_west_5", eu_west_5)
if eu_west_6 is not None :
    session.addCloudLocation("eu_west_6", eu_west_6)
if eu_west_13 is not None :
    session.addCloudLocation("eu_west_13", eu_west_13)
if eu_west_14 is not None :
    session.addCloudLocation("eu_west_14", eu_west_14)
if na_northeast_6 is not None :
    session.addCloudLocation("na_northeast_6", na_northeast_6)
if na_northeast_7 is not None :
    session.addCloudLocation("na_northeast_7", na_northeast_7)
if us_east_4 is not None :
    session.addCloudLocation("us_east_4", us_east_4)
if us_northcentral_2 is not None :
    session.addCloudLocation("us_northcentral_2", us_northcentral_2)
if us_northcentral_3 is not None :
    session.addCloudLocation("us_northcentral_3", us_northcentral_3)
if us_southcentral_2 is not None :
    session.addCloudLocation("us_southcentral_2", us_southcentral_2)
if us_west_7 is not None :
    session.addCloudLocation("us_west_7", us_west_7)
if us_west_8 is not None :
    session.addCloudLocation("us_west_8", us_west_8)
if us_west_9 is not None :
    session.addCloudLocation("us_west_9", us_west_9)
if ap_east_3 is not None :
    session.addCloudLocation("ap_east_3", ap_east_3)
if ap_northeast_7 is not None :
    session.addCloudLocation("ap_northeast_7", ap_northeast_7)
if ap_southeast_8 is not None :
    session.addCloudLocation("ap_southeast_8", ap_southeast_8)
if eu_west_7 is not None :
    session.addCloudLocation("eu_west_7", eu_west_7)
if us_east_3 is not None :
    session.addCloudLocation("us_east_3", us_east_3)
if us_east_9 is not None :
    session.addCloudLocation("us_east_9", us_east_9)
if us_northcentral_4 is not None :
    session.addCloudLocation("us_northcentral_4", us_northcentral_4)
if us_west_6 is not None :
    session.addCloudLocation("us_west_6", us_west_6)
if eu_west_8 is not None :
    session.addCloudLocation("eu_west_8", eu_west_8)
if eu_west_11 is not None :
    session.addCloudLocation("eu_west_11", eu_west_11)
if na_northeast_1 is not None :
    session.addCloudLocation("na_northeast_1", na_northeast_1)
if eu_west_3 is not None :
    session.addCloudLocation("eu_west_3", eu_west_3)
if eu_west_9 is not None :
    session.addCloudLocation("eu_west_9", eu_west_9)
if eu_west_10 is not None :
    session.addCloudLocation("eu_west_10", eu_west_10)
if eu_center_3 is not None :
    session.addCloudLocation("eu_center_3", eu_center_3)
if eu_north_1 is not None :
    session.addCloudLocation("eu_north_1", eu_north_1)
if eu_south_1 is not None :
    session.addCloudLocation("eu_south_1", eu_south_1)
if na_northeast_2 is not None :
    session.addCloudLocation("na_northeast_2", na_northeast_2)
if na_northeast_3 is not None :
    session.addCloudLocation("na_northeast_3", na_northeast_3)
if na_northeast_4 is not None :
    session.addCloudLocation("na_northeast_4", na_northeast_4)
if us_west_3 is not None :
    session.addCloudLocation("us_west_3", us_west_3)
if us_west_5 is not None :
    session.addCloudLocation("us_west_5", us_west_5)
if us_southcentral_3 is not None :
    session.addCloudLocation("us_southcentral_3", us_southcentral_3)
if us_southcentral_4 is not None :
    session.addCloudLocation("us_southcentral_4", us_southcentral_4)
if us_east_2 is not None :
    session.addCloudLocation("us_east_2", us_east_2)
if ap_southeast_5 is not None :
    session.addCloudLocation("ap_southeast_5", ap_southeast_5)
if ap_south_1 is not None :
    session.addCloudLocation("ap_south_1", ap_south_1)
if us_east_7 is not None :
    session.addCloudLocation("us_east_7", us_east_7)
if eu_west_4 is not None :
    session.addCloudLocation("eu_west_4", eu_west_4)

response=session.generateYmlCloudFile()
# set variables
responseCode = response.getResponseCode()
output = response.getStdout()
error = response.getStderr()
NeoLoadCloudYML = Variable('NeoLoadCloudYML', response.getYmlContent())

releaseid=getCurrentRelease().id
variables=releaseApi.getVariables(releaseid)
CreateVar=True

for var in variables :
    if var.key == 'NeoLoadCloudYML':
        var.value=response.getYmlContent()
        releaseApi.updateVariable( var)
        CreateVar=False

if CreateVar == True :
    releaseApi.createVariable(releaseid, NeoLoadCloudYML)


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