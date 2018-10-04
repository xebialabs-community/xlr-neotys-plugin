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
import java.util.List;

/**
 * Created by hrexed on 15/02/18.
 */
public class NeoLoadCloudPlatform {
    private String cloudWorkGroup;
    private int duration;
    private List<CloudBooking> cloudLocations = new ArrayList<>();
    private StringBuilder errors = new StringBuilder();
    private StringBuilder output = new StringBuilder();
    private String cloudType;
    private static final String MEDIUM = "MEDIUM";
    private static final String LARGE = "LARGE";

    public NeoLoadCloudPlatform(String cloudWorkGroup, String duration, String cloudType) {

            if (isCorrectType(cloudType)) {
                this.cloudType = cloudType.toUpperCase();
            } else {
                this.cloudType = MEDIUM;
            }
            this.cloudWorkGroup = cloudWorkGroup;
	    try {
            this.duration = Integer.parseInt(duration);

        } catch (NumberFormatException e) {
            addError("ERROR", "Conversion issue", e);
        }
    }

    public void addCloudLocation(String locationId, String number) {
        cloudLocations.add(new CloudBooking(Integer.parseInt(number), locationId));
    }

    private boolean isCorrectType(String type) {
        return MEDIUM.equalsIgnoreCase(type) || LARGE.equalsIgnoreCase(type);
    }

    private void addError(String type, String message, Exception e) {
        if (e != null) {
            errors.append(type)
                    .append(" : ")
                    .append(message)
                    .append(" excception : ")
                    .append(e.getMessage())
                    .append("\n");
        } else {
            errors.append(type)
                    .append("Error :")
                    .append(message)
                    .append("\n");
        }
    }

    private void addOutput(String message) {
        output.append(message).append("\n");
    }

    public CloudResponse generateYmlCloudFile() {
		int responseCode = 0;
        CloudResponse cloudResponse;
        StringBuilder yml = new StringBuilder();
        try {
            addOutput("Generating the YML\n");
            yml.append("infrastructures:\n");
            yml.append("  - name: My Cloud infrastructure\n");
            yml.append("    type: NEOTYS_CLOUD_LOAD_GENERATOR\n");
            yml.append("    workgroup: ").append(this.cloudWorkGroup).append("\n");
            yml.append("    architecture: ").append(this.cloudType).append("\n");
            yml.append("    duration: ").append(this.duration).append("h\n");
            yml.append("    zones:\n");
	        for (CloudBooking cloudLocation : cloudLocations) {
		        if (cloudLocation.getCloudZoneID() == null) {
			        addError("Location", "Location NULL", null);
		        }
		        yml.append("    - id: ").append(cloudLocation.getCloudZoneID()).append("\n");
		        yml.append("      count: ").append(cloudLocation.getNumberOfLG()).append("\n");
	        }

            if (yml.length() > 0) {
                addOutput("YML generated :\n" + yml.toString());
				responseCode = 0;
            }
			if (errors.length() > 0) {
				responseCode = 1;
			}
        } catch (Exception e) {
            addError("ERROR", "Technical Error", e);
        }
        cloudResponse = new CloudResponse(yml.toString(), responseCode);
        cloudResponse.addToError(errors);
        cloudResponse.addToOut(output);

        return cloudResponse;
    }
}


