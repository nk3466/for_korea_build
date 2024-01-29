import xml.etree.ElementTree as ET
import requests

def create_xml(action, dev_num="1", dev_mode="null", unit_num="1", unit_status="on", unit_dimming='2', unit_color="10"):
    imap_elem = ET.Element('imap', ver="1.0", address="192.168.100.93", sender="server")
    service_elem = ET.SubElement(imap_elem, "service", type="request", name="remote_access_smartlight")
    target_elem = ET.SubElement(service_elem, "target", name="server2.0_new_auth", id="1", msg_no="11")
    action_elem = ET.SubElement(service_elem, "action")
    action_elem.text = action

    params = {
        "dev_num": dev_num,
        "dev_mode": dev_mode,
        "unit_num": unit_num,
        "unit_status": unit_status,
        "unit_dimming": unit_dimming,
        "unit_color": unit_color
    }

    params_elem = ET.SubElement(service_elem, "params", **params)
    device_info_elem = ET.SubElement(service_elem, "device_info", alias="test_phone", twinid="F6B253A39360F76356007356E79A3F82948582ADE31E3E77598FA127BFC69F36")

    return ET.tostring(imap_elem, encoding="utf-8", method="xml")


    
def control_light(unit_status):
    headers = {'Content-Type': 'application/xml'}
    target_url = "http://192.168.110.100/v2/admin/sys/transfer/10.20.3.17?port=11000&secure=true"
    control_xml = create_xml(action="control", unit_status=unit_status)
    control_response = requests.post(target_url, data=control_xml, headers=headers)
    return control_response
    
def control_light_dimming(unit_status, dimming_num):
    headers = {'Content-Type': 'application/xml'}
    print('dimming_num', dimming_num)
    target_url = "http://192.168.110.100/v2/admin/sys/transfer/10.20.3.17?port=11000&secure=true"
    control_xml = create_xml(action="control", unit_status=str(unit_status), unit_dimming=str(dimming_num[0]), unit_color = str(dimming_num[1]))
    control_response = requests.post(target_url, data=control_xml, headers=headers)
    return control_response
