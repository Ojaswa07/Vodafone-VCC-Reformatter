import re
import time
from colorama import init, Fore
from tqdm import tqdm

# Initialize colorama
init()

# ASCII art for the header
header_art = f"""{Fore.RED}
██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗
██║  ██║██╔══██╗██║    ██║██║ ██╔╝
███████║███████║██║ █╗ ██║█████╔╝ 
██╔══██║██╔══██║██║███╗██║██╔═██╗ 
██║  ██║██║  ██║╚███╔███╔╝██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
{Fore.RESET}"""

# Read input from input.txt
with open('input.txt', 'r') as file:
    input_text = file.read()

# Extract individual VCC details
vcc_start_line = "Online Payment Card Details"
vcc_end_line = "Card accepted on any local or international websites"
vcc_matches = re.findall(rf"{vcc_start_line}(.*?)(?={vcc_start_line}|{vcc_end_line}|\Z)", input_text, re.DOTALL)

# Initialize a list to store the reformatted VCCs
reformatted_vccs = []

# Display header ASCII art
print(header_art)

# Define colorful loading bar
loading_bar = tqdm(total=len(vcc_matches), bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', dynamic_ncols=True)

# Iterate over each VCC detail
for vcc_detail in vcc_matches:
    # Extract card number, expiry date, and CVV from the VCC detail
    card_number = re.findall(r"Card number:\s*(\d+)", vcc_detail)
    expiry_date = re.findall(r"Expiry date:\s*(\d{2})/(\d{2})", vcc_detail)
    cvv = re.findall(r"CVV:\s*(\d+)", vcc_detail)

    # Check if any detail is missing
    if not card_number or not expiry_date or not cvv:
        continue

    # Reformat the extracted information
    reformatted_vcc = f'{card_number[0]}:{expiry_date[0][0]}{expiry_date[0][1]}:{cvv[0]}'

    # Add the reformatted VCC to the list
    reformatted_vccs.append(reformatted_vcc)

    # Update the loading bar
    loading_bar.update()

    # Sleep for a short duration for smoother animation
    time.sleep(0.1)

# Finish the loading bar
loading_bar.close()

# Write reformatted VCCs to output.txt
with open('output.txt', 'w') as file:
    file.write('\n'.join(reformatted_vccs))

# Display the total amount of reformatted VCCs
print(f"{Fore.RED}Reformatted VCCs: {len(reformatted_vccs)}{Fore.RESET}")
