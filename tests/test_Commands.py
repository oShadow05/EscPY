import unittest
from build_connections.connections import ConnectionRegistry
from build_connections.connection_adapter import ConnectionAdapter
from build_connections.device import Device
from esc_pos.commands import PrintTextCommand, PrintImageCommand
import base64
class TestCommands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.device = Device("Dummy", None)
        cls.conn = ConnectionRegistry.create("ConnDummy", cls.device)
        cls.adapter = ConnectionAdapter(conn=cls.conn)

    def test_send_text_command(self):
        command = PrintTextCommand()
        text = "Hello World!"
        command.execute(self.adapter, text)
        self.assertEqual(command.output, b"\x1bt\x00Hello World!")

    def test_send_image_command(self):
        command = PrintImageCommand()
        base64img_str = (
            "UklGRqYBAABXRUJQVlA4IJoBAADQLgCdASraAaoBPp1OpE4lpCOiIAgAsBOJaW7hd2EbQAnsA99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych77ZOQ99snIe+2TkPfbJyHvtk5D32ych76wAAD+/9YYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
        )
        image_bytes = base64.b64decode(base64img_str)
        command.execute(self.adapter, image_bytes)
        self.assertTrue(command.output[:8].hex(), "1d7630003c00aa01")

        self.assertEqual(command.output[-1:], b"\x00") # image used is completely white