#
# Copyright 2018 NEOTYS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import json
from com.neotys.xebialabs.xl import NeoLoadFileUtil
from java.lang import Exception


def GetNeoLoadData(title, releaseid, trendingtype):
    output = "{ \"type\":\"" + trendingtype + "\","
    result = "\"data_graph\":[ "

    try:
        tasks = []
        try:
            # For new version API
            try:
                release = _releaseApi.getRelease(releaseid)
            except Exception as e:
                print e.getMessage()
                release = _releaseApi.getArchivedRelease(releaseid)

            for phase in release.phases:
                for t in phase.tasks:
                    if t.title == title:
                        tasks.append(t)
        except Exception as e:
            # For old version API
            print e.getMessage()
            tasks = _taskApi.searchTasksByTitle(title, None, releaseid)

        for task in tasks:
            if task.type.name == "CustomScriptTask":
                # if task.type=="Neoload.LaunchTest" :
                attachments = task.attachments
                print attachments
                for attachment in attachments:
                    if "report.xml" in attachment.exportFilename or "report.xml" in attachment.fileUri:
                        file_byte = _releaseApi.getAttachment(attachment.id)
                        if trendingtype == "Hit/s":
                            hits = NeoLoadFileUtil.getStat("hits", file_byte)
                            result += "{\"kpi\":" + hits + "},"
                        if trendingtype == "Response Time":
                            error = NeoLoadFileUtil.getStat("response", file_byte)
                            result += "{\"kpi\":" + error + "},"
                        if trendingtype == "Errors":
                            response = NeoLoadFileUtil.getStat("error", file_byte)
                            result += "{\"kpi\":" + response + "},"

        if result[-1:] == ",":
            result = result[:-1]

        result += "]"

        output += result + "}"
        print "Date for graph ................."
        print output
        return output
    except Exception as e:
        print e.getMessage()
        return None


releaseid = release.id

if NeoLoadTaskTitle is not None and TrendingData is not None:
    response = GetNeoLoadData(NeoLoadTaskTitle, releaseid, TrendingData)
    if response is not None:
        data = json.loads(response)