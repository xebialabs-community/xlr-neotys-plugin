#
# Copyright 2018 NEOTYS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from com.neotys.xebialabs.xl import NeoLoadFileUtil

def GetNeoLoadData(title,releaseid):
    result="{\"data_graph\":[ "
    try:

        TasksList=taskApi.searchTasksByTitle(title,None,releaseid)
        for task in TasksList:
            if task.type=="Neoload.LaunchTest" :
                attachmens=task.attachments
                for att in attachmens:
                    if att.name=="report.xml":
                        file_byte= releaseApi.getAttachment(att.id)
                        hits=NeoLoadFileUtil("hits",file_byte)
                        error=NeoLoadFileUtil("error",file_byte)
                        response=NeoLoadFileUtil("response",file_byte)
                        result+="{\"hits\":"+hits+",\"error\":"+error+",\"response\": "+response+"},"


        result=result[:-1]
        result+="]}"
        return result
    except:
        return None


title = request.query["NeoLoadTaskTitle"]
releaseid = request.query["releaseid"]
if title is not None and releaseid is not None:
    resJythonResponse()
    response.entity=GetNeoLoadData(NeoLoadTaskTitle)
else :
    response.entity=None
    response.exception="No Get Parameters found"

#NeoLoadTaskTitle = request.query["NeoLoadTaskTitle"]

##json=GetNeoLoadData(NeoLoadTaskTitle)
