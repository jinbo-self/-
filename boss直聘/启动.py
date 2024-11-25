import subprocess
import time
import psutil

# 定义要监控的 Python 程序路径
program1 = "main.py"  # 替换为您的第一个 Python 程序路径
program2 = "测试.py"  # 替换为您的第二个 Python 程序路径

# 启动程序的函数
def start_program(program):
    print(f"启动程序: {program}")
    subprocess.Popen(["python", program])  # 使用 Popen 启动程序

# 检查程序是否在运行
def is_running(program_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # 检查进程名是否包含程序名
            if program_name in proc.info['name']:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# 主监控循环
while True:
    # 检查第一个程序

    start_program(program1)
    time.sleep(7)    # 每 15 秒检查一次