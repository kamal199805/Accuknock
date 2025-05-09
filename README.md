import psutil
import logging
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80      # in percentage
MEMORY_THRESHOLD = 80   # in percentage
DISK_THRESHOLD = 80     # in percentage

# Set up logging
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_alert(metric, value):
    alert_msg = f"ALERT: {metric} is at {value}%"
    print(alert_msg)
    logging.warning(alert_msg)

def monitor_system():
    # CPU
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        log_alert("CPU Usage", cpu)

    # Memory
    memory = psutil.virtual_memory().percent
    if memory > MEMORY_THRESHOLD:
        log_alert("Memory Usage", memory)

    # Disk
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        log_alert("Disk Usage", disk)

    # Processes
    print("\nTop 5 processes by memory usage:")
    for proc in sorted(psutil.process_iter(['pid', 'name', 'memory_percent']),
                       key=lambda p: p.info['memory_percent'],
                       reverse=True)[:5]:
        print(f"PID {proc.info['pid']} - {proc.info['name']} - {proc.info['memory_percent']:.2f}% memory")

if __name__ == "__main__":
    print(f"\nSystem Health Check - {datetime.now()}")
    monitor_system()
