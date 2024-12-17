from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import MacForm, UserForm, IpForm
import re

@app.route('/', methods=['GET', 'POST'])
def form():
    mac_form = MacForm()
    user_form = UserForm()
    ip_form = IpForm()
    return render_template('form.html', mac_form=mac_form, user_form=user_form, ip_form=ip_form)

@app.route('/generate_mac_script', methods=['POST'])
def generate_mac_script():
    mac_form = MacForm()
    if mac_form.validate_on_submit():
        data = mac_form.data.data
        print(f"Received MAC data: {data}")  # Debugging line
        mac_addresses = re.split(r'[,\s]+', data.strip())
        formatted_macs = [re.sub(r'[:-]', ':', mac).upper() for mac in mac_addresses if mac]
        print(f"Formatted MACs: {formatted_macs}")  # Debugging line
        script = generate_mac_script_content(formatted_macs)
        print(f"Generated script: {script}")  # Debugging line
        return render_template('result.html', script=script)
    else:
        print("MAC form validation failed")  # Debugging line
        print(mac_form.errors)  # Debugging line
    return redirect(url_for('form'))

@app.route('/generate_user_script', methods=['POST'])
def generate_user_script():
    user_form = UserForm()
    if user_form.validate_on_submit():
        users_data = user_form.users.data
        print(f"Received users data: {users_data}")  # Debugging line
        users = [line.split() for line in users_data.splitlines() if line]
        print(f"Parsed users: {users}")  # Debugging line
        script = generate_user_script_content(users)
        print(f"Generated script: {script}")  # Debugging line
        return render_template('result.html', script=script)
    else:
        print("User form validation failed")  # Debugging line
        print(user_form.errors)  # Debugging line
    return redirect(url_for('form'))

@app.route('/generate_ip_script', methods=['POST'])
def generate_ip_script():
    ip_form = IpForm()
    if ip_form.validate_on_submit():
        ips_data = ip_form.ips.data
        print(f"Received IP data: {ips_data}")  # Debugging line
        ip_addresses = re.split(r'[,\s]+', ips_data.strip())
        print(f"Parsed IPs: {ip_addresses}")  # Debugging line
        script = generate_ip_script_content(ip_addresses)
        print(f"Generated script: {script}")  # Debugging line
        return render_template('result.html', script=script)
    else:
        print("IP form validation failed")  # Debugging line
        print(ip_form.errors)  # Debugging line
    return redirect(url_for('form'))

def generate_mac_script_content(mac_addresses):
    script_lines = []
    for mac in mac_addresses:
        script_lines.append("config firewall address")
        script_lines.append(f"edit \"{mac}\"")
        script_lines.append("set type mac")
        script_lines.append(f"set macaddr \"{mac}\"")
        script_lines.append("next")
        script_lines.append("end")
    return "\n".join(script_lines)

def generate_user_script_content(users):
    script_lines = []
    for username, password in users:
        script_lines.append("config user local")
        script_lines.append(f"edit \"{username}\"")
        script_lines.append(f"set passwd \"{password}\"")
        script_lines.append("next")
        script_lines.append("end")
    return "\n".join(script_lines)

def generate_ip_script_content(ip_addresses):
    script_lines = []
    for ip in ip_addresses:
        script_lines.append("config firewall address")
        script_lines.append(f"edit \"{ip}\"")
        script_lines.append(f"set subnet {ip} 255.255.255.255")
        script_lines.append("next")
        script_lines.append("end")
    return "\n".join(script_lines)

