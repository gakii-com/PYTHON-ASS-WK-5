# 🧠 Object-Oriented Programming (OOP) Demos in Python

This project includes two Python programs that demonstrate the core concepts of **Object-Oriented Programming**:

- ✅ Inheritance
- ✅ Polymorphism
- ✅ Encapsulation

---

## 📦 Files Included

| File Name          | Description                            |
|--------------------|----------------------------------------|
| `devices_demo.py`  | Simulates devices like smartphones and smartwatches with unique behaviors |
| `vehicle_demo.py`  | Demonstrates polymorphism with various vehicles using a common `move()` method |

---

## 🚀 1. Devices Demo – `devices_demo.py`

### 🔍 Description
This program defines a base `Device` class and two subclasses:
- `Smartphone`
- `SmartWatch`

Each device has its own implementation of `get_status()`, and the program shows how the same method name behaves differently depending on the object.

### 🧠 Concepts Used:
- Inheritance (`Smartphone` and `SmartWatch` inherit from `Device`)
- Polymorphism (`get_status()` is redefined in each subclass)
- Encapsulation (`_is_on` is a protected attribute)

🧪 Sample Output:
🔁 Powering on all devices...

iPhone 15 is now ON.
Vivoactive 5 is now ON.

📱 Smartphone: Apple iPhone 15
🔋 Battery: 100%
🌐 Data Left: 20 GB

⌚ SmartWatch: Garmin Vivoactive 5
🚶 Steps: 0
❤️ Heart Rate: 70 bpm

🚗 2. Vehicles Demo – vehicle_demo.py
🔍 Description

This program defines a base Vehicle class and several subclasses:

Car

Plane

Boat

Bike

Train

Each subclass implements its own version of the move() method. All objects are handled in the same loop — showing how polymorphism works.

🧠 Concepts Used:

Inheritance (Car, Plane, etc. inherit from Vehicle)

Polymorphism (move() behaves differently per vehicle)

🧪 Sample Output:
🚦 Vehicles are now moving:

Toyota: Driving on the road! 🚗
Boeing 747: Flying in the sky! ✈️
SailMaster 3000: Sailing on the water! 🛥️
Mountain Bike: Pedaling down the street! 🚲
Express Line: Running on tracks! 🚆

