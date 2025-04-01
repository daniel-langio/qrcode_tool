import os
import json
import qrcode
from qrcode.constants import ERROR_CORRECT_L

def load_json_file(_path: str) -> dict:
    if is_path_exist(_path):
        with open(_path, 'r') as f:
            return json.load(f)

    raise Exception(f"json file not found at: {_path}")

def create_dir(_path: str):
    if not is_path_exist(_path):
        os.mkdir(_path)

def is_path_exist(_path: str):
    return os.path.exists(_path)

def escape_str(_str: str) -> str:
    return _str.replace(":", "_").replace(",", "_").replace(";", "_").replace("=", "_").replace("'", "").replace(" ", "_").strip("{}")

def generate_by_text(text: str, fill_color: str ="black", back_color: str ="white", output_dir: str = "./qrcodes") -> str:
    """
    """

    # create output dir
    create_dir(output_dir)

    # output path
    file_name = escape_str(text) + ".png"
    output_path = os.path.join(output_dir, file_name)

    qr = qrcode.QRCode(
        version=3,
        error_correction=ERROR_CORRECT_L,
        box_size=3,
        border=50
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_path)

    return output_path

def generate_by_json(json_path: str, fill_color: str ="black", back_color: str ="white", output_dir: str = "./qrcodes") -> str:
    """
    """
    data = load_json_file(json_path)

    if type(data) is list:
        for dt in data:
            generate_by_text(str(dt), fill_color, back_color, output_dir)
    elif type(data) is dict:
        generate_by_text(str(data), fill_color, back_color, output_dir)
    else:
        raise Exception(f"json format not valid: \n {data}")


if __name__ == "__main__":
    print(generate_by_json("./test.json"))