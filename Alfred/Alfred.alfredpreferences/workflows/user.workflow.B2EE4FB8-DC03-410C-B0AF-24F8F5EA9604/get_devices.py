"""
Author: Omar Iriskic
@contact:
    https://omaririskic.com/
    https://github.com/OMKE
Date: 15 - 04 - 2020 23:49
"""


from workflow import Workflow, ICON_WEB, web
import sys
from subprocess import Popen, PIPE

from pprint import pprint
from xml.dom import minidom


def main(wf):
    """
    @desc:
        xmltodict
        - parses xml to python dictionary
    """

    import xmltodict

    # @var sp - Runs the system_profiler SPBluetoothDataType in shell and returns it as xml file
    sp = Popen(["system_profiler", "SPBluetoothDataType", "-xml"],
               stdout=PIPE).communicate()[0]

    # @var doc - parses xml document as python dictionary
    doc = xmltodict.parse(sp)

    """
    filter_type
    @desc:
        Goes throu a list of bluetooth device types and returns if there is one in the available oens
    @params:
        names - a list of all values in the xml, 
    @return: string - founded type
    """

    def filter_type(names):
        available_types = ["Headphones", "Loudspeaker",
                           "Smartphone", "Mouse", "Keyboard", "GameController", "Trackpad"]

        for i in names:
            for j in available_types:
                if i == j:
                    return i

    # @var device_ordered_dict - because xml is written in nested dicts, we point to one we need for devices
    devices_ordered_dict = doc['plist']['array']['dict']['array'][1]['dict']['array'][0]['dict']

    # @var devices - initialization
    devices = []

    for i in devices_ordered_dict:
        added_type = False

        for j in i['dict']['key']:
            device = {}
            if j == "device_minorClassOfDevice_string":
                device['type'] = filter_type(i['dict']['string'])
                added_type = True

            if added_type:
                device['name'] = i['key']
                index_of_connected = i['dict']['key'].index(
                    'device_isconnected')
                device['is_connected'] = "Connected" if i['dict']['string'][index_of_connected] == "attrib_Yes" else "Not connected"
                devices.append(device)
                break

    """
    @desc:
        Goes through a list of devices and populates alfred script filter list
    """

    for i in devices:
        wf.add_item(title=i['name'],
                    subtitle=i["type"]+" - "+i['is_connected'], arg=i['name'], valid=True, icon="icons/" + i['type'].lower()+".ico")
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))
