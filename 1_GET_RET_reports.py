import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from datetime import date

# Disable SSL certificate verification warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def download_data(url, save_path):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    
    with open(save_path, 'wb') as file:
        file.write(response.content)
    
    print(f"Downloaded data from {url} and saved it to {save_path}")

# Get the current date
current_date = date.today().strftime("%Y-%m-%d")

# Set the save directory path
save_directory = os.path.expanduser(f"~/Documents/Data_Collection/input/ret/")

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Download RET files
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_220_129_66', os.path.join(save_directory, '10_220_129_66.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_220_129_121', os.path.join(save_directory, '10_220_129_121.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_224_6_86', os.path.join(save_directory,'10_224_6_86.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_224_6_150', os.path.join(save_directory, '10_224_6_150.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_224_69_150', os.path.join(save_directory, '10_224_69_150.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_224_7_214', os.path.join(save_directory, '10_224_7_214.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_224_7_22', os.path.join(save_directory, '10_224_7_22.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_228_76_214', os.path.join(save_directory,'10_228_76_214.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_228_81_22', os.path.join(save_directory,'10_228_81_22.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_228_84_22', os.path.join(save_directory,'10_228_84_22.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_228_79_86', os.path.join(save_directory,'10_228_79_86.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_220_5_214', os.path.join(save_directory,'10_220_5_214.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_224_2_214', os.path.join(save_directory,'10_224_2_214.csv'))
download_data('https://docs.nonpci-ranconfig-p.aws.dishcloud.io/r_central/getretmcms?cmsname=10_220_69_150', os.path.join(save_directory,'10_220_69_150.csv'))