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
from java.lang import Exception


def GetNeoLoadData(title, releaseid, reportXpathQuery, NeoLoadKpiName):
    output = "{ \"type\":\"" + NeoLoadKpiName + "\","
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
                attachments = task.attachments
                for attachment in attachments:
                    if "report.xml" in attachment.exportFilename or "report.xml" in attachment.fileUri:
                        file_byte = _releaseApi.getAttachment(attachment.id)
                        hits = NeoLoadFileUtil.getCustomStat(reportXpathQuery, file_byte)
                        result += "{\"kpi\":" + hits + "},"

        if result[-1:] == ",":
            result = result[:-1]

        result += "]"

        output += result + "}"
        return output
    except Exception as e:
        print  e.getMessage()
        return None


releaseid = release.id

if NeoLoadTaskTitle is not None and reportXpathQuery is not None and NeoLoadKpiName is not None:
    response = GetNeoLoadData(NeoLoadTaskTitle, releaseid, reportXpathQuery, NeoLoadKpiName)
    if response is not None:
        data = json.loads(response)