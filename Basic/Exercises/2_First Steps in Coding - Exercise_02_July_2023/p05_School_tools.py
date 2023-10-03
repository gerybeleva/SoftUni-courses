pencil_packets = int(input())
pencil_price = 5.8
marker_packets = int(input())
marker_price = 7.2
blackboard_packets = int(input())
blackboard_price = 1.2
discount = int(input())

sum = round(((pencil_packets * pencil_price) + (marker_packets * marker_price) + (blackboard_packets * blackboard_price)) * (1-(discount / 100)),2)

print(sum)