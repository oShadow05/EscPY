import unittest
from build_connections.connections import ConnectionUSB, ConnectionRegistry, ConnectionETH, ConnectionDummy
from build_connections.device import Device, DeviceParamsBag
from build_connections import constants

# Global
usb_params = DeviceParamsBag()
usb_params.add_par_int(constants.PRODUCT_ID, 0x192)
usb_params.add_par_int(constants.VENDOR_ID, 0x256)

eth_params = DeviceParamsBag()
eth_params.add_par_str(constants.IP, "127.0.0.1")



class TestConnectionRegistry(unittest.TestCase):
    def test_registered_USB(self):
        device = Device("USB1", usb_params)
        conn = ConnectionRegistry.create("ConnUSB", device)
        self.assertIsInstance(conn, ConnectionUSB)
        self.assertEqual(conn.device.name, "USB1")

    def test_registered_ETH(self):
        device = Device("ETH1", eth_params)
        conn = ConnectionRegistry.create("ConnETH", device)
        self.assertIsInstance(conn, ConnectionETH)
        self.assertEqual(conn.device.name, "ETH1")

    def test_registered_DUMMY(self):
        device = Device("Dummy", eth_params)
        conn = ConnectionRegistry.create("ConnDummy", device)
        self.assertIsInstance(conn, ConnectionDummy)
        self.assertEqual(conn.device.name, "Dummy")

class TestConnections(unittest.TestCase):
    def test_usb(self):
        device = Device("USB1", usb_params)   
        usb = ConnectionUSB(device)
        self.assertIsInstance(usb, ConnectionUSB)
    
    def test_ethernet(self):
        device_eth = Device("ETH1", eth_params)
        eth = ConnectionETH(device_eth)
        self.assertIsInstance(eth, ConnectionETH)

    def test_dummy(self):
        device_dummy = Device("Dummy", None)
        dummy = ConnectionDummy(device_dummy)
        self.assertIsInstance(dummy, ConnectionDummy)
