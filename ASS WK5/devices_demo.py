# devices_demo.py

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._is_on = False  # Encapsulated attribute

    def power_on(self):
        if not self._is_on:
            self._is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self._is_on:
            self._is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def get_status(self):
        raise NotImplementedError("Subclasses must implement this method.")

# -------------------------------------------------------

class Smartphone(Device):
    def __init__(self, brand, model, storage, mobile_data):
        super().__init__(brand, model)
        self.storage = storage
        self.battery_level = 100
        self.installed_apps = []
        self.storage_used = 0
        self.photos = []
        self.mobile_data = mobile_data

    def install_app(self, app_name, size):
        if self.storage_used + size > self.storage:
            print("Not enough storage to install this app.")
        else:
            self.installed_apps.append(app_name)
            self.storage_used += size
            print(f"{self.model}: Installed '{app_name}'.")

    def use_data(self, amount):
        if amount > self.mobile_data:
            print(f"{self.model}: Not enough mobile data.")
        else:
            self.mobile_data -= amount
            print(f"{self.model}: Used {amount} GB data. Remaining: {self.mobile_data} GB.")

    def get_status(self):
        power_state = "ON" if self._is_on else "OFF"
        print(f"""
📱 Smartphone: {self.brand} {self.model}
🔋 Battery: {self.battery_level}%
💾 Storage: {self.storage_used}/{self.storage} GB
🌐 Data Left: {self.mobile_data} GB
🔌 Power: {power_state}
""")


# -------------------------------------------------------

class SmartWatch(Device):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.steps = 0
        self.heart_rate = 70

    def track_steps(self, count):
        self.steps += count
        print(f"{self.model}: Tracked {count} steps.")

    def get_status(self):
        power_state = "ON" if self._is_on else "OFF"
        print(f"""
⌚ SmartWatch: {self.brand} {self.model}
🚶 Steps: {self.steps}
❤️ Heart Rate: {self.heart_rate} bpm
🔌 Power: {power_state}
""")


# -------------------------------------------------------

def main():
    # Create a list of devices with different types
    devices = [
        Smartphone("Apple", "iPhone 15", 256, 20),
        SmartWatch("Garmin", "Vivoactive 5"),
        Smartphone("Samsung", "Galaxy S25", 128, 15),
        SmartWatch("Fitbit", "Sense 2")
    ]

    # Polymorphism in action
    print("🔁 Powering on all devices...\n")
    for device in devices:
        device.power_on()

    print("🔍 Getting status of all devices...\n")
    for device in devices:
        device.get_status()

    print("⚙️ Performing actions...\n")
    # Device-specific actions
    devices[0].install_app("Instagram", 2)
    devices[1].track_steps(3000)
    devices[2].use_data(5)
    devices[3].track_steps(1500)

    print("\n🧾 Updated status after actions:\n")
    for device in devices:
        device.get_status()


if __name__ == "__main__":
    main()
