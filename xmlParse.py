import xml.etree.ElementTree as ET

fileName = "xmlFile.xml"
group_over_5 = []
tree = ET.parse(fileName)
root = tree.getroot()
for item in root.findall("group_Id"):
    artifact = item.find("artifactId").text
    version = item.find("version").text
    num = item.find("Num").text
    if(float(num))>5:
        print("++++++++++Group Over 5 ++++++++++ ")
        group_over_5.append(num)
    print(artifact,num)

    
