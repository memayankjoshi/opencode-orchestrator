import sys
import json
import yaml
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def update_task(task_id, key, value):
    yaml_path = os.path.join(BASE_DIR, 'tasks.yaml')
    with open(yaml_path, 'r', encoding='utf-8') as f:
        tasks = yaml.safe_load(f) or []
    
    for t in tasks:
        if t['id'] == task_id:
            t[key] = value
            break
            
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(tasks, f, sort_keys=False)

def complete_task(task_id):
    update_task(task_id, 'status', 'complete')
    
    json_path = os.path.join(BASE_DIR, 'progress.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        prog = json.load(f)
        
    prog['completed'] += 1
    prog['remaining'] = max(0, prog['remaining'] - 1)
    prog['current_task'] = ''
    prog['status'] = 'idle'
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(prog, f, indent=2)

def set_session(task_id, agent, retry=0, error=''):
    json_path = os.path.join(BASE_DIR, 'session.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'active_agent': agent,
            'retry_count': retry,
            'current_task': task_id,
            'last_error': error
        }, f, indent=2)
        
    # Also update progress.json current_task
    prog_path = os.path.join(BASE_DIR, 'progress.json')
    with open(prog_path, 'r', encoding='utf-8') as f:
        prog = json.load(f)
    prog['current_task'] = task_id
    prog['status'] = 'running'
    with open(prog_path, 'w', encoding='utf-8') as f:
        json.dump(prog, f, indent=2)

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'complete':
        complete_task(sys.argv[2])
    elif cmd == 'session':
        # python opencode_state.py session TASK_ID AGENT_NAME RETRY_COUNT "ERROR_MSG"
        set_session(sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5] if len(sys.argv) > 5 else '')
    elif cmd == 'escalate':
        # python opencode_state.py escalate TASK_ID NEW_AGENT
        update_task(sys.argv[2], 'recommended_agent', sys.argv[3])
    print(f"State updated for {cmd}.")
