import xml.etree.ElementTree as ET
import requests

def create_xml(name, action, dev_num="1", dev_mode="null", unit_num="all", unit_status="on", unit_dimming='5', unit_color="5"):
    imap_elem = ET.Element('imap', ver="1.0", address="192.168.100.93", sender="server")
    service_elem = ET.SubElement(imap_elem, "service", type="request", name=name)# "remote_access_smartlight")
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

def create_xml_(name, action, dev_cnt = "all", dev_num = "1", unit_cnt = "null", ctrl_action = "on/null/null/null/60"):

    imap_elem = ET.Element('imap', ver="1.0", address = "", sender = "server")
    service_elem = ET.SubElement(imap_elem, "service", type = "request", name=name)
    target_elem = ET.SubElement(service_elem, "target", name = "server2.0_new_auth", id = "1", msg_no = "11")
    action_elem = ET.SubElement(service_elem, "action")
    action_elem.text = action
    cnt_elem = ET.SubElement(service_elem, "dev_cnt")
    cnt_elem.text = dev_cnt

    params = {
        "dev_num" : dev_num,
        "unit_cnt" : unit_cnt,
        "ctrl_action" : ctrl_action 
    }

    params_elem = ET.SubElement(service_elem, "dev_params", **params)
    device_info_elem = ET.SubElement(service_elem, "device_info", alias = "test_phone", twinid="F6B253A39360F76356007356E79A3F82948582ADE31E3E77598FA127BFC69F36")

    return ET.tostring(imap_elem, encoding="utf-8", method="xml")

def create_xml_other(name, action, dev_cnt = "all", dev_num = "1", unit_cnt = "gas1", ctrl_action = "close"):

    imap_elem = ET.Element('imap', ver="1.0", address = "", sender = "server")
    service_elem = ET.SubElement(imap_elem, "service", type = "request", name=name)
    target_elem = ET.SubElement(service_elem, "target", name = "server2.0_new_auth", id = "1", msg_no = "11")
    action_elem = ET.SubElement(service_elem, "action")
    action_elem.text = action
    cnt_elem = ET.SubElement(service_elem, "dev_cnt")
    cnt_elem.text = dev_cnt

    params = {
        "dev_num" : dev_num,
        "unit_cnt" : unit_cnt,
        "ctrl_action" : ctrl_action 
    }

    params_elem = ET.SubElement(service_elem, "dev_params", **params)
    device_info_elem = ET.SubElement(service_elem, "device_info", alias = "test_phone", twinid="F6B253A39360F76356007356E79A3F82948582ADE31E3E77598FA127BFC69F36")

    return ET.tostring(imap_elem, encoding="utf-8", method="xml")