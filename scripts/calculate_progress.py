import argparse
import json
import sys

def main():
    parser = argparse.ArgumentParser(description='Calculate progress percentage.')
    parser.add_argument('--completed', type=int, required=True, help='Number of completed items')
    parser.add_argument('--total', type=int, required=True, help='Total number of items')
    
    args = parser.parse_args()
    
    completed = args.completed
    total = args.total
    
    if total == 0:
        percentage = 0.0
    else:
        percentage = (completed / total) * 100.0
        
    result = {
        "completed": completed,
        "total": total,
        "percentage": percentage
    }
    
    print(json.dumps(result))

if __name__ == '__main__':
    main()
