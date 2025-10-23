from .connections import Connection
import io
class ConnectionAdapter:
    conn: Connection

    def __init__(self, conn: Connection):
        self.conn = conn

    def get_output_printer(self) -> bytes:
        if(hasattr(self.conn.printer, "output")): # output only when is dummy printer.
            return self.conn.printer.output
        return b"no_dummy_printer"

    def send_text(self, text: str) -> None:
        self.conn.printer.text(text)

    def send_text_output(self, text: str) -> bytes:
        self.send_text(text=text)
        return self.get_output_printer()
    
    def send_image(self, image: bytes) -> None:
        self.conn.printer.image(io.BytesIO(image))

    def send_image_output(self, image: bytes) -> bytes:
        self.send_image(image=image)
        return self.get_output_printer()