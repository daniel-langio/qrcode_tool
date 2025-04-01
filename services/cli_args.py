import argparse

parser = argparse.ArgumentParser(description="qrcode generator script")

# arguments
parser.add_argument('--dir', type=str, default='./qrcodes')
parser.add_argument('--json', type=str)
parser.add_argument('--text', type=str)

args = parser.parse_args()
