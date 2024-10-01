#!/bin/bash

CPU_THRESHOLD=80
MEM_THRESHOLD=80
DISK_THRESHOLD=90
LOGFILE="/var/log/system_monitor.log"

# Check CPU usage
cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
echo "CPU usage: $cpu_usage%" | tee -a $LOGFILE
if (( $(echo "$cpu_usage > $CPU_THRESHOLD" | bc -l) )); then
    echo "High CPU usage detected: $cpu_usage%" | tee -a $LOGFILE
fi

# Check memory usage
mem_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
echo "Memory usage: $mem_usage%" | tee -a $LOGFILE
if (( $(echo "$mem_usage > $MEM_THRESHOLD" | bc -l) )); then
    echo "High memory usage detected: $mem_usage%" | tee -a $LOGFILE
fi

# Check disk usage
disk_usage=$(df / | grep / | awk '{ print $5}' | sed 's/%//g')
echo "Disk usage: $disk_usage%" | tee -a $LOGFILE
if [ "$disk_usage" -gt "$DISK_THRESHOLD" ]; then
    echo "High disk usage detected: $disk_usage%" | tee -a $LOGFILE
fi

# Alert or log when thresholds breached
# (You can modify this to send an email alert)
echo "System monitoring completed." | tee -a $LOGFILE
