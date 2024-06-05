from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import requests

TOR_API_URL = "https://secureupdates.checkpoint.com/IP-list/TOR.txt"

app = Flask(__name__)
app.config['FLASK_DEBUG'] = True

# Endpoint to search for an exact IP address
@app.route('/search', methods=['GET'])
def search_ip():
    # Extract the IP address from the request
    ip = request.args.get('ip')
    if ':' in ip:
        ip = '[' + ip + ']'
    # Check if the IP is in the Tor exit node list and respond accordingly
    if ip in ten_set:
        return f'IP {ip} is a Tor exit node'
    else:
        return f'IP {ip} is not a Tor exit node'

# Endpoint to delete an exact IP address from the list
@app.route('/delete', methods=['GET', 'DELETE'])
def delete_ip():
    ip = request.args.get('ip')
    if ':' in ip:
        ip = '[' + ip + ']'
    if ip in ten_set:
        ten_set.remove(ip)
        del_set.add(ip)
        return f'IP {ip} deleted successfully<br>{del_set}'
    else:
        return f'IP {ip} not found in the list'

# Endpoint to retrieve the full list
@app.route('/list', methods=['GET'])
def retrieve_list():
    app.logger.info("list")
    ten_view = update_view(ten_set)
    return f'{len(ten_set)}<br>{ten_view}'

# Update the list view using the latest tor exit nodes
def update_view(ten):
    view = ''
    for ip in ten:
        view += ip
        view += '<br>'
    return view

def fetch_tor_exit_nodes():
    response = requests.get(TOR_API_URL)
    if response.status_code == 200:
        res = response.text.split('\r\n')
        res.pop()
        return res

    return None

def refresh_tor_exit_nodes():
    global tor_exit_nodes  # Assuming tor_exit_nodes is a global list
    global ten_set
    updated_nodes = fetch_tor_exit_nodes()  # Fetch the latest Tor exit nodes
    tor_exit_nodes = updated_nodes  # Update the global list
    ten_set = set()
    ten_set.update(tor_exit_nodes)
    app.logger.info("%d", len(ten_set))
    app.logger.info("scheduler triggered")
    for ip in del_set:
        if ip in ten_set:
            app.logger.info("delete %s", ip)
            ten_set.remove(ip)

if __name__ == '__main__':

    # Initialize the Tor exit node list and start the Flask app
    tor_exit_nodes = fetch_tor_exit_nodes()
    if tor_exit_nodes == None:
        print("Failed to retrieve Tor exit node list.")
        exit(1)

    scheduler = BackgroundScheduler()

    # Start the scheduler
    scheduler.start()

    # Schedule the refresh_tor_exit_nodes function to run every 2 minutes
    scheduler.add_job(refresh_tor_exit_nodes, 'interval', seconds=20)

    # Initiate set for tor exit nodes and set for deleted nodes
    ten_set, del_set = set(), set()
    ten_set.update(tor_exit_nodes)
    app.run(host="0.0.0.0", debug=True)
