package com.neotys.xebialabs.xl;

/**
 * Created by hrexed on 23/03/18.
 */
class NeoLoadVarsResponse extends CloudResponse {

    NeoLoadVarsResponse(String content, int responseCode) {
        super(content, responseCode);
    }

    void appendContent(String content) {
        if (!this.getYmlContent().contains(content))
            this.ymlContent += "," + content;
    }
}
