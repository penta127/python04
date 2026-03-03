#!/usr/bin/env python3

def ft_ancient_text() -> None:
    file = None
    filename = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {filename}")

    try:
        file = open(filename, "r")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")

        data = file.read()
        print(data)
        print()
        print("Data recovery complete. Storage unit disconnected.")

    except Exception:
        print("ERROR:Storage vault not found. Run data generator first.")

    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    ft_ancient_text()
