import sys
import subprocess
import json


def get_json_task_list():
    json_data = open('./taskconfig.json')
    data = json.load(json_data)
    json_data.close()
    return data


if __name__ == "__main__":
    processes = []
    task_list = get_json_task_list()

    try:
        for task in task_list:
            if task['type'] == 'copy':
                process = subprocess.Popen(
                    [sys.executable,
                     '%s' % './scheduler/copy_worker.py',
                     '-s %s' % task['source'],
                     '-d %s' % task['destination'],
                     '-t %d' % task['timeout']])
                processes.append(process)
            elif task['type'] == 'delete':
                process = subprocess.Popen(
                    [sys.executable,
                     '%s' % './scheduler/delete_worker.py',
                     '-s %s' % task['source'],
                     '-t %d' % task['timeout']])
                processes.append(process)

        for proc in processes:
            proc.wait()
    except KeyboardInterrupt:
        print("Quitting the program")