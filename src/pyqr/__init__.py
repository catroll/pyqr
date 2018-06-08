# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'

from .qrcode import constants as qrcode_constants, QRCode
from .pyzbar import pyzbar
from PIL import Image


def decode(file_path):
    """QR code decode

    Args:
        file_path:

    Returns:
        None, if failed
        string, if success
    """
    data = pyzbar.decode(Image.open(file_path))
    if data:
        return data[0].data.decode('utf-8')


def encode(content, save_path):
    """QR code encode

    Args:
        content: string
        save_path: string, file path

    Returns:
        Image Object
    """
    qr = QRCode(version=1, error_correction=qrcode_constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    if save_path:
        img.save(save_path)
    return img
