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

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringReader;

/**
 * Created by hrexed on 04/04/18.
 */
public class NeoLoadFileUtil {

    private static final String HITS = "hits";
    private static final String ERRORS = "error";
    private static final String RESPONSE = "response";

    public static String getCustomStat(String xpath, byte[] bytes) {
        try {
            InputStream input = new ByteArrayInputStream(bytes);
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse(input);

            return getCustomData(doc, xpath);
        } catch (Exception e) {
            return e.getMessage();
        }
    }

    public static String getStat(String type, byte[] bytes) throws IOException, SAXException, ParserConfigurationException, XPathExpressionException {
        InputStream input = new ByteArrayInputStream(bytes);
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();

        //don't valid xml file
		builder.setEntityResolver((publicId, systemId) -> {
			if (systemId.contains("report.dtd")) {
				return new InputSource(new StringReader(""));
			} else {
				return null;
			}
		});
        Document doc = builder.parse(input);
        switch (type) {
            case HITS:
                return getData(doc, "avg_hits/s");
            case ERRORS:
                return getData(doc, "total_errors");
            case RESPONSE:
                return getData(doc, "avg_reqresponsetime");
        }
        return "0";
    }

    private static String getData(Document doc, String key) throws XPathExpressionException {
        XPath xPath = XPathFactory.newInstance().newXPath();
        String result = null;
        NodeList nodes = (NodeList) xPath.evaluate("/report/summary/statistics/statistic[@name='" + key + "']", doc.getDocumentElement(), XPathConstants.NODESET);
        for (int i = 0; i < nodes.getLength(); ++i) {
            Element e = (Element) nodes.item(i);
            result = e.getAttribute("value");
        }
		System.out.println("Result parse: " + result);
		if (result != null) {
			return result.replaceAll(",", ".");
		}
		return null;
    }

    private static String getCustomData(Document doc, String Xpath) throws XPathExpressionException {
        XPath xPath = XPathFactory.newInstance().newXPath();
        XPathExpression xPathExpression = xPath.compile(Xpath);
        return (String) xPathExpression.evaluate(doc, XPathConstants.STRING);
    }
}
