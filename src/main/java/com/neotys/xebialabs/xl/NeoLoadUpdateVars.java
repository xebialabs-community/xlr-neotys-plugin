/**
 * Copyright 2018 NEOTYS
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
package com.neotys.xebialabs.xl;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by hrexed on 23/03/18.
 */
public class NeoLoadUpdateVars {
    private String variableName;
    private String variableValue;
    private List<String> variables = new ArrayList<>();

    public NeoLoadUpdateVars(String variableName, String variableValue) {
        this.variableName = variableName;
        this.variableValue = variableValue;
    }

    public void SetExistingVars(String var) {
        if (var != null) {
            String[] parts = var.split(",");
            Collections.addAll(variables, parts);
        }
    }

    public NeoLoadVarsResponse UpdateVariable() {
        NeoLoadVarsResponse response;
        response = new NeoLoadVarsResponse(variableName + "=" + variableValue, 0);
        for (String variable : variables) {
            response.appendContent(variable);
        }

        return response;
    }
}
