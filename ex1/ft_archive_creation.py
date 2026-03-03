#!/usr/bin/env python3

def ft_archive_creation() -> None:
    filename = "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print(f"Initializing new storage unit: {filename}")
    file = None
    try:
        file = open(filename, "w")
        print("Storage unit created successfully...")
        print()
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if file is not None:
            file.close()

    file = None
    data = ""
    try:
        file = open(filename, "r")
        data = file.read()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if file is not None:
            file.close()
    print("Inscribing preservation data...")
    print(data)
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
