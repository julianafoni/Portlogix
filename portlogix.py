from tabulate import tabulate
import random
from datetime import datetime

# === Initial sample ship data (with Ship ID) ===
ships_data = [
    {
        "Ship ID": "OS-45",
        "Ship Name": "Ocean Sovereign",
        "ETA": "2025-06-14 07:30",
        "TEUs": 1800,
        "Cargo Type": "Containerized Cargo",
        "Gate": "A1",
        "Status": "Waiting"
    },
    {
        "Ship ID": "SV-11",
        "Ship Name": "Sea Voyager",
        "ETA": "2025-06-14 09:45",
        "TEUs": 1250,
        "Cargo Type": "Refrigerated Cargo",
        "Gate": "A3",
        "Status": "Delayed (weather)"
    },
    {
        "Ship ID": "BH-200",
        "Ship Name": "Blue Horizon",
        "ETA": "2025-06-14 12:15",
        "TEUs": 950,
        "Cargo Type": "Containerized Cargo",
        "Gate": "B2",
        "Status": "Loading/Unloading"
    },
    {
        "Ship ID": "CS-90",
        "Ship Name": "Coral Spirit",
        "ETA": "2025-06-14 23:00",
        "TEUs": 320,
        "Cargo Type": "Hazardous Materials",
        "Gate": "B1",
        "Status": "Priority"
    },
    {
        "Ship ID": "NQ-1",
        "Ship Name": "Nusantara Queen",
        "ETA": "2025-06-15 04:20",
        "TEUs": 1600,
        "Cargo Type": "Containerized Cargo",
        "Gate": "A2",
        "Status": "Waiting"
    },
    {
        "Ship ID": "GS-06",
        "Ship Name": "Golden Straits",
        "ETA": "2025-06-15 08:10",
        "TEUs": 2100,
        "Cargo Type": "General Cargo",
        "Gate": "C1",
        "Status": "Docked"
    },
    {
        "Ship ID": "AM-77",
        "Ship Name": "Aurora Mariner",
        "ETA": "2025-06-15 10:45",
        "TEUs": 1100,
        "Cargo Type": "Containerized Cargo",
        "Gate": "B3",
        "Status": "Waiting"
    }
]

# === DISPLAY ALL SHIPS ===
def display_all_data():
    if not ships_data:
        print("No ship data available.")
    else:
        print("\n=== Ship Schedule List ===")
        print(tabulate(ships_data, headers="keys", tablefmt="fancy_grid"))

# === MAIN MENU ===
def display_main_menu():
    print("\n=== Port Logistics Task Tracker ===")
    menu = [
        ["1", "Display All Data"],
        ["2", "Read Menu"],
        ["3", "Create Menu"],
        ["4", "Update Menu"],
        ["5", "Delete Menu"],
        ["6", "Exit Program"],
    ]
    print(tabulate(menu, headers=["Option", "Description"], tablefmt="fancy_grid"))

def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice (1–6): ").strip()
        if choice == "1":
            display_all_data()
        elif choice == "2":
            read_menu()
        elif choice == "3":
            create_menu()
        elif choice == "4":
            update_menu()
        elif choice == "5":
            delete_menu()
        elif choice == "6":
            print("Exiting program. Thank You!")
            break
        else:
            print("Invalid choice. Please enter 1–6.")

# === READ MENU ===
def read_menu():
    print("\n=== Read Menu ===")
    if not ships_data:
        print("⚠️  No data available. Please add data first.")
        return

    while True:
        read_options = [
            ["1", "Search by Ship Name"],
            ["2", "Filter by Status"],
            ["3", "Filter by Gate"],
            ["4", "Filter by ETA Date (YYYY-MM-DD)"],
            ["5", "Combine Multiple Filters"],
            ["6", "Back to Main Menu"]
        ]
        print("\nWhat would you like to do?")
        print(tabulate(read_options, headers=["Option", "Description"], tablefmt="fancy_grid"))

        choice = input("Choose an option (1–6): ").strip()
        results = []

        if choice == "1":
            name = input("Enter ship name: ").strip().lower()
            results = [s for s in ships_data if name in s["Ship Name"].lower()]
        elif choice == "2":
            status = input("Enter status: ").strip().lower()
            results = [s for s in ships_data if status in s["Status"].lower()]
        elif choice == "3":
            gate = input("Enter gate: ").strip().upper()
            results = [s for s in ships_data if s["Gate"].upper() == gate]
        elif choice == "4":
            date = input("Enter ETA date (YYYY-MM-DD): ").strip()
            results = [s for s in ships_data if s["ETA"].startswith(date)]
        elif choice == "5":
            print("\n=== Combine Multiple Filters ===")
            print("Leave fields empty to skip them.")
            filter_inputs = [
                ["Status", ""],
                ["Gate", ""],
                ["ETA Date (YYYY-MM-DD)", ""],
                ["Cargo Type", ""]
            ]
            
            for i, (field_name, _) in enumerate(filter_inputs):
                filter_inputs[i][1] = input(f"Enter {field_name}: ").strip()

            status = filter_inputs[0][1].lower()
            gate = filter_inputs[1][1].upper()
            date = filter_inputs[2][1]
            cargo = filter_inputs[3][1].lower()

            results = ships_data
            if status:
                results = [s for s in results if status in s["Status"].lower()]
            if gate:
                results = [s for s in results if gate == s["Gate"].upper()]
            if date:
                results = [s for s in results if s["ETA"].startswith(date)]
            if cargo:
                results = [s for s in results if cargo in s["Cargo Type"].lower()]
        elif choice == "6":
            print("Returning to main menu...")
            break
        else:
            print("Invalid option.")
            continue

        if results:
            print("\n✅ Matching Ships:")
            print(tabulate(results, headers="keys", tablefmt="fancy_grid"))
        else:
            print("❌ No matching ships found.")


# === GENERATE SHIP ID AUTOMATICALLY ===
def generate_ship_id(name):
    words = name.upper().split()
    initials = ''.join(word[0] for word in words)
    number = random.randint(10, 999)
    return f"{initials}-{number}"

# === CREATE MENU ===
def create_menu():
    print("\n=== Create New Ship Record ===")
    while True:
        # Input fields for new ship
        new_ship_inputs = [
            ["Ship Name", ""],
            ["ETA (YYYY-MM-DD HH:MM)", ""],
            ["Volume (TEUs)", ""],
            ["Cargo Type", ""],
            ["Gate (e.g. A1, B2)", ""],
            ["Status (e.g. Waiting, Docked, Delayed)", ""]
        ]

        for i, (field_name, _) in enumerate(new_ship_inputs):
            new_ship_inputs[i][1] = input(f"Enter {field_name}: ").strip()

        ship_name = new_ship_inputs[0][1]
        ship_id = generate_ship_id(ship_name)

        if any(ship["Ship ID"] == ship_id for ship in ships_data):
            print(f"⚠️  Auto-generated Ship ID '{ship_id}' already exists. Retrying...")
            continue

        eta = new_ship_inputs[1][1]
        try:
            teus = int(new_ship_inputs[2][1])
        except ValueError:
            print("TEUs must be a number.")
            return
        cargo_type = new_ship_inputs[3][1]
        gate = new_ship_inputs[4][1].upper()
        status = new_ship_inputs[5][1]

        new_ship = {
            "Ship ID": ship_id,
            "Ship Name": ship_name,
            "ETA": eta,
            "TEUs": teus,
            "Cargo Type": cargo_type,
            "Gate": gate,
            "Status": status
        }

        print("\n📋 Please review the data:")
        print(tabulate([new_ship], headers="keys", tablefmt="fancy_grid"))
        
        confirmation_options = [
            ["1", "Yes"],
            ["2", "No"]
        ]
        print("\nSave this data?")
        print(tabulate(confirmation_options, headers=["Option", "Description"], tablefmt="fancy_grid"))
        confirm_choice = input("Choose an option (1 or 2): ").strip()

        if confirm_choice == "1":
            ships_data.append(new_ship)
            print("✅ Data successfully saved!")
        else:
            print("❌ Data not saved.")

        add_another_options = [
            ["1", "Yes"],
            ["2", "No"]
        ]
        print("\nAdd another ship?")
        print(tabulate(add_another_options, headers=["Option", "Description"], tablefmt="fancy_grid"))
        again_choice = input("Choose an option (1 or 2): ").strip()

        if again_choice != "1":
            break

# update menu
def update_menu():
    print("\n=== Update Ship Record ===")

    if not ships_data:
        print("⚠️ No ship data available to update.")
        return

    while True:
        update_options = [
            ["1", "Search and update by Ship ID"],
            ["2", "Return to Main Menu"]
        ]
        print("\nUpdate Menu Options:")
        print(tabulate(update_options, headers=["Option", "Description"], tablefmt="fancy_grid"))

        option = input("Choose an option (1 or 2): ").strip()

        if option == "2":
            print("Returning to main menu...")
            break

        if option != "1":
            print("Invalid input. Try again.")
            continue

        # Step 1: User inputs primary key (Ship ID)
        ship_id = input("Enter Ship ID to update (e.g. OS-45): ").strip().upper()
        matches = [ship for ship in ships_data if ship["Ship ID"] == ship_id]

        if not matches:
            print("❌ The data you are looking for does not exist.")
            continue

        # Step 2: Show current ship data
        ship = matches[0]
        print("\n✅ Ship Found:")
        print(tabulate([ship], headers="keys", tablefmt="fancy_grid"))

        # Step 3: Confirm update
        confirmation_options = [
            ["1", "Yes"],
            ["2", "No"]
        ]
        print("\nDo you want to update this ship?")
        print(tabulate(confirmation_options, headers=["Option", "Description"], tablefmt="fancy_grid"))
        confirm_choice = input("Choose an option (1 or 2): ").strip()

        if confirm_choice != "1":
            print("Returning to previous menu...")
            continue

        # Step 4: Ask for column to update
        field_options = [
            ["ETA", "ETA"],
            ["TEUs", "TEUs"],
            ["Cargo Type", "Cargo Type"],
            ["Gate", "Gate"],
            ["Status", "Status"]
        ]
        print("\nFields you can update:")
        print(tabulate(field_options, headers=["Field", "Description"], tablefmt="fancy_grid"))
        
        field_input = input("Enter the field name to update: ").strip().title()
        
        # Map input to actual key names in the dictionary
        field_mapping = {
            "Eta": "ETA",
            "Teus": "TEUs",
            "Cargo Type": "Cargo Type",
            "Gate": "Gate",
            "Status": "Status"
        }
        field_key = field_mapping.get(field_input)

        if not field_key:
            print("❌ Invalid field name.")
            continue

        # Step 5: Input new value
        new_value = input(f"Enter new value for {field_key}: ").strip()

        # Step 6: Final confirmation
        final_confirmation_options = [
            ["1", "Yes"],
            ["2", "No"]
        ]
        print(f"\nAre you sure you want to update '{field_key}' to '{new_value}'?")
        print(tabulate(final_confirmation_options, headers=["Option", "Description"], tablefmt="fancy_grid"))
        final_confirm_choice = input("Choose an option (1 or 2): ").strip()
        
        if final_confirm_choice != "1":
            print("Update cancelled.")
            continue

        # Step 7: Apply the update
        if field_key == "TEUs":
            try:
                new_value = int(new_value)
            except ValueError:
                print("⚠️ TEUs must be a numeric value. Update aborted.")
                continue

        ship[field_key] = new_value
        print("✅ Data successfully updated!")
        print(tabulate([ship], headers="keys", tablefmt="fancy_grid"))

        # Step 8: Ask if user wants to update another
        repeat_options = [
            ["1", "Yes"],
            ["2", "No"]
        ]
        print("\nDo you want to update another ship?")
        print(tabulate(repeat_options, headers=["Option", "Description"], tablefmt="fancy_grid"))
        repeat_choice = input("Choose an option (1 or 2): ").strip()
        
        if repeat_choice != "1":
            break

# deleting menu
# This should be declared globally at the top of your program
activity_logs = []

def delete_menu():
    print("\n=== Delete Ship Record ===")

    if not ships_data:
        print("⚠️ No ship data available to delete.")
        return

    while True:
        delete_options = [
            ["1", "Delete by Ship ID"],
            ["2", "Return to Main Menu"]
        ]
        print("\nDelete Menu Options:")
        print(tabulate(delete_options, headers=["Option", "Description"], tablefmt="fancy_grid"))

        option = input("Choose an option (1 or 2): ").strip()

        if option == "2":
            print("Returning to main menu...")
            break

        if option != "1":
            print("Invalid input. Try again.")
            continue

        ship_id = input("Enter Ship ID to delete (e.g. OS-45): ").strip().upper()
        matches = [ship for ship in ships_data if ship["Ship ID"] == ship_id]

        if not matches:
            print("❌ The data you are looking for does not exist.")
            continue

        ship = matches[0]
        print("\n✅ Ship Found:")
        print(tabulate([ship], headers="keys", tablefmt="fancy_grid"))

        confirmation_options = [
            ["1", "Yes"],
            ["2", "No"]
        ]
        print("\nAre you sure you want to delete this ship?")
        print(tabulate(confirmation_options, headers=["Option", "Description"], tablefmt="fancy_grid"))
        confirm_choice = input("Choose an option (1 or 2): ").strip()

        if confirm_choice != "1":
            print("Deletion cancelled.")
            continue

        final_confirmation_prompt = [["Type 'delete' to confirm permanent deletion", ""]]
        print(tabulate(final_confirmation_prompt, headers=["Action", "Input"], tablefmt="fancy_grid"))
        final_confirm = input("Enter confirmation: ").strip().lower()

        if final_confirm != "delete":
            print("⚠️ Deletion not confirmed. Returning to menu.")
            continue

        # 📝 Log activity before deletion
        deletion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{deletion_time}] DELETED: {ship['Ship ID']} - {ship['Ship Name']}"
        activity_logs.append(log_entry)

        # Perform deletion
        ships_data.remove(ship)
        print("✅ Data successfully deleted!")
        print(f"📝 Log: {log_entry}")

        again_options = [
            ["1", "Yes"],
            ["2", "No"]
        ]
        print("\nDelete another ship?")
        print(tabulate(again_options, headers=["Option", "Description"], tablefmt="fancy_grid"))
        again_choice = input("Choose an option (1 or 2): ").strip()
        if again_choice != "1":
            break

if __name__ == "__main__":
    main()