# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.


import time
wait_time = 1
max_retries = 5
attempt = 0

while attempt < max_retries:
  print(f"Attempt {attempt + 1}: Waiting for {wait_time} seconds before retrying...")
  time.sleep(wait_time)
  success = False  
  if success:
    print("Operation succeeded!")
    break
  else:
    print("Operation failed. Retrying...")
    wait_time *= 2
    attempt += 1
else:
  print("Max retries reached. Operation failed after 5 attempts.")
