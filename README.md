# 🚢 Portlogix
<img src="https://github.com/julianafoni/Portlogix/blob/main/portlogix%20cover.png?raw=true" />

---

# 📌 Context

**Portlogix** is a Python-based terminal simulation program developed to model and manage port logistics operations through structured CRUD (Create, Read, Update, Delete) functionalities. The system enables users to track and manipulate vessel data including ship names, ETA schedules, cargo types, gate assignments, and operational status. Features like multi-filter search, dynamic ship ID generation, and activity logging provide users with realistic tools for data handling in port environments.

Its simplicity, clarity, and modular design make it ideal for students, educators, and early-stage developers interested in building applied Python applications within the field of maritime logistics or operational simulation. This project also serves as a practical capstone-style prototype for academic learning, offering hands-on experience in system logic, user interaction flow, and structured data management in the logistics domain.

---

# 🛠 Business Tasks

The Port Logistics Task Tracker provides a simulation framework to replicate daily port management workflows, focusing on:
- Track and manage incoming ships and their associated cargo information
- Create, read, update, and delete shipping task data
- Enable data filtering by ship name, cargo type, status, and ETA
- Log and track system activities (update/delete)  

---

# 🎯 Objectives

- Provide a lightweight port task tracker prototype
- Simulate real-life maritime operations digitally
- Allow students and developers to practice backend logic using Python and tabular data

---

# 👥 Stakeholders or Target Users

- **Port authorities**: For managing docking schedules and cargo types
- **Maritime students or researchers**: To simulate port traffic control
- **Developers**: For building CRUD systems with meaningful use cases
- **Instructors/educators**: For classroom demonstrations on Python projects

---

# ⚠ Limitations

-	**Temporary Data**: Data is stored in-memory and will be lost upon program termination.
-	**No Login System**: There is no user role control, meaning all users have full access to the system.
-	**Manual Input**: All data must be input manually; there is no connection to external APIs or databases.
-	**No Error Handling on Formats**: Invalid datetime or input formats may not be fully validated.
-	**Limited Realism**: While realistic in flow, it lacks integration with real port hardware or tracking systems.

---

# 📊 Data Used

Each ship entry includes:
- **Ship ID** -  Auto-generated unique identifier (e.g., OS-45 for “Ocean Sovereign”)
- **Ship Name**
- **ETA** (Estimated Time of Arrival) - Date and Time
- Cargo Volume **(TEUs)** - Container capacity in Twenty-foot Equivalent Units
- **Cargo Type** - e.g., Containerized, Hazardous, Refrigerated
- **Dock Gate** - e.g., A1, B2
- **Status** - e.g., Waiting, Delayed, Loading, Docked

---

# 💻 User Instructions

To run this program:

**1. Requirements:**
- Make sure Python is installed on your system.
- Open terminal or Visual Studio Code.
- Install required module: pip install tabulate
- Run the program
- Follow the menu instructions inside the program.

**2. Follow the on-screen menu:**
- Display All Data
- Read Menu (with filters)
- Create Menu
- Update Menu (including reassigning gate)
- Delete Menu (with activity logs)
- Exit Program

**3. Tips:**
- Use valid formats for date/time (e.g., 2025-06-14 07:30)
- Avoid blank inputs for critical fields
- Monitor activity logs for deletion history

_Disclaimer: This program is for educational use only and does not use persistent storage._ 

---

# Documentation
## 🧭 Main Menu
![Main Menu](https://github.com/julianafoni/Portlogix/blob/main/main%20menu.png?raw=true)

## 📋 Ship Data Display
![Main Menu](

## 🔍 Read Menu – Filter 
![Main Menu](
---

# Assets
- 
