import time
from track_poster import post_a_track

def main():
  while True:
    post_a_track()
    time.sleep(60*60*24)

if __name__ == "__main__":
  main()

