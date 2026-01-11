import requests
import tkinter
from tkintermapview import TkinterMapView, convert_address_to_coordinates
import customtkinter
import sys
import subprocess

# Get the public IP address
ip_response = requests.get('https://httpbin.org/ip')
ip_address = ip_response.json()['origin']

# Get location information using IPinfo API
response = requests.get(f"https://ipinfo.io/{ip_address}?token=c5e878ee370a18")
location_data = response.json() if response.status_code == 200 else None

# Main application window
root_tk = tkinter.Tk()
root_tk.geometry("375x667")
root_tk.title('Map View Example')

# Map widget
map_widget = TkinterMapView(root_tk, width=800, height=450, corner_radius=10)
map_widget.pack(pady=20)

# Extract latitude and longitude from location data
latitude, longitude = map(float, location_data['loc'].split(',')) if location_data else (0, 0)
map_widget.set_position(latitude, longitude)
map_widget.set_marker(latitude, longitude, text="Your Location")

# Search bar and button
def search_location():
    address = search_entry.get()
    coordinates = convert_address_to_coordinates(address)
    if coordinates:
        map_widget.set_position(*coordinates)
        map_widget.set_marker(*coordinates, text="Destination")
        draw_path(coordinates)

search_frame = customtkinter.CTkFrame(root_tk)
search_frame.pack(pady=20)

search_entry = customtkinter.CTkEntry(search_frame, placeholder_text="Enter a destination address")
search_entry.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

search_button = customtkinter.CTkButton(search_frame, text="Search", command=search_location)
search_button.pack(side=tkinter.LEFT, padx=10)

menu_button = customtkinter.CTkButton(search_frame, text="   Back  ", command=lambda: run_menu())
menu_button.pack(side=tkinter.RIGHT, padx=10)
# Function to draw a path
def draw_path(destination):
    map_widget.set_path([latitude, longitude], destination)

def run_menu():
    root_tk.destroy() 
    root_tk.after(1000,subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\gui_menu.py']))

root_tk.mainloop()
