from utils.misc.send_birtday_message import main_process
import asyncio
import threading

main_thread = threading.Thread(target= asyncio.run, args=(main_process(), ))

