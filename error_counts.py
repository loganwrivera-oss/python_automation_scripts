server_logs = [
    "INFO: Server started",
    "ERROR: Database connection failed",
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "WARNING: High memory usage",
    "ERROR: Disk full",
    "INFO: Backup complete",
    "ERROR: Database connection failed",
    "ERROR: Disk full"
]

error_counts = {}

for i in server_logs:
    if "ERROR:" in i:
        logs = i.split(": ")
        message = logs[1]
        if message in error_counts:
            error_counts[message] += 1
        else:
            error_counts[message] = 1

print(error_counts)

for message, count in error_counts.items():
    if count > 2:
        print(f"Alert: {message} is critical")
