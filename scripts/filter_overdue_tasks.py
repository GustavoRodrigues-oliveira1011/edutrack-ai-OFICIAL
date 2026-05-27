import argparse
import json
import time

def main():
    parser = argparse.ArgumentParser(description='Filter subject IDs with overdue tasks.')
    parser.add_argument('--tasks', type=str, required=True, help='JSON string containing list of tasks')
    
    args = parser.parse_args()
    
    try:
        tasks = json.loads(args.tasks)
    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON format"}))
        return

    # In Xano, timestamp is typically in milliseconds since epoch
    current_time_ms = int(time.time() * 1000)
    
    overdue_subject_ids = set()
    
    for task in tasks:
        status = task.get("status", "pending")
        if status == "completed":
            continue
            
        due_date = task.get("due_date")
        if due_date is None:
            continue
            
        try:
            due_date = float(due_date)
        except ValueError:
            continue
            
        if due_date < current_time_ms:
            subject_id = task.get("subject_id")
            if subject_id is not None:
                overdue_subject_ids.add(subject_id)
                
    result = {
        "subject_ids": list(overdue_subject_ids)
    }
    
    print(json.dumps(result))

if __name__ == '__main__':
    main()
