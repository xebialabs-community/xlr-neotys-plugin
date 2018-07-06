# xlr-neotys-plugin

[![Build Status](https://travis-ci.org/xebialabs-community/xlr-neotys-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xlr-neotys-plugin)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/480e882e8e744d7484fe8c0060bbd070)](https://www.codacy.com/app/tjrandall/xlr-neotys-plugin_2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=xebialabs-community/xlr-neotys-plugin&amp;utm_campaign=Badge_Grade)
[![Code Climate](https://codeclimate.com/github/xebialabs-community/xlr-neotys-plugin/badges/gpa.svg)](https://codeclimate.com/github/xebialabs-community/xlr-neotys-plugin)
[![License: MIT][xlr-neotys-plugin-license-image] ][xlr-neotys-plugin-license-url]
[![Github All Releases][xlr-neotys-plugin-downloads-image]]()

[xlr-neotys-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-neotys-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-neotys-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-neotys-plugin/total.svg

## Preface

## Overview

Tasks: The plugin has 3 different tasks :
Launch test
            Launch test task allow the user to trigger a NeoLoad load test on a remote machine ( windows, macos, linux).

            This task supports all the different way to store a Neoload project :

### Locally
On a Neotys Team Server
On a Source control ( Git or svn)
            This task is also compatible with the usage of our new platform : NeoLoad Web.

             If the user has a NeoLoad web subscription, the plugin will stream the data to the user's NeoLoad web account ( saas or on prem).

            The task is failing when the SLA of the test are not met.

            The launch test task is storing on the ask 3 reports : report.xml ( required for the custom tile), junit.xml, report.pdf

        
### Update variable
            The update variable allows the user to rewrite the runtime context of a test.

            The main idea behind this task is to update the project used by "launch test task" by updating the reference of the System under test.

            If the XL release user is deploying the application on a new environment, he will be able to pass the definition of the environment to NeoLoad through the update variable task.
Cloud session
            Neotys offer and manage a cloud platform. Our users has the ability to spin up Load generators based on 57 different geos ( Load generator is the component generating the load to the application). Our users can run test from the expected location of the endusers.

            The cloud session task will allow xl release users to create a cloud session that would used by the "launch test " task.


    Update variable and cloud session are tasks that are optional but will change the behavior of the launch test task.


## Custom tile :
The plugin comes with 2 custom tiles :     
NeoLoad trending graph : The user can add to the release dashboard a tile that will trend all the test launched ( having a specific name) on following kpis :
Average response time
Errors
Hit/s
NeoLoad Custom trending graph : The user can trend any metrics exposed in our report.xml. the user will specify the xpath query required to collect the kpi from our report.

## Installation

## References

