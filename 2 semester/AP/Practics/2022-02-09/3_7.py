heights = []

count = 0

while True:
    height = int(input("[>] Enter height: "))
    if height == -1:
        break
    heights.append(height)

for i in range(1, len(heights) - 1):
    if heights[i - 1] < heights[i] > heights[i + 1]:
        count += 1

print(f"[+] Count of hills: {count}")

