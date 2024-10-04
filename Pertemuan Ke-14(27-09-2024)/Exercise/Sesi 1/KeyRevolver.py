price_per_bullet = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = list(map(int, input().split()))
intelligence_value = int(input())

total_cost = 0
bullets_fired = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]

    bullets_fired += 1
    total_cost += price_per_bullet

    if bullet <= lock:
        print("Bang!")
        locks.pop(0)
    else:
        print("Ping!")

    if bullets_fired % barrel_size == 0 and bullets:
        print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - total_cost}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
