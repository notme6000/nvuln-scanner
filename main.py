import xml.etree.ElementTree as EF

root = None

try:
    tree = EF.parse("hello.xml") 
    root = tree.getroot()
    print("-"*20)
    print("XML FILE SUCCESSFULLY READ")
    print(f"root tag : {root.tag}")
    print("-"*20)
except FileNotFoundError:
    print("ERROR: file not found")
except EF.ParseError as e:
    print("ERROR: file not parsed correctly")
except Exception as e:
    print("ERROR: unexpected error")

port_id = 0
port_services = 0
port_state = 0

if root is not None:
    for host in root.findall('host'):
        ports = host.find('ports')
        for port in ports.findall('port'):
            port_id = port.get('portid')
            protocol = port.get('protocol')

            state = port.find('state')
            status = state.get('state')

            services = port.find('service')
            service_name = services.get('name')
            version = services.get('product')

            print(f"port no : {port_id}")
            print(f"protocol : {protocol}")
            print(f"port status: {status}" )
            print(f"port service: {service_name}")
            print(f"service version: {version}")
            print("-"*20)
