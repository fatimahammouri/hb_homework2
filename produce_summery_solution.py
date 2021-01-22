def melon_count(day_number, the_file):
    print(day_number)
    delievery_log = open(the_file)
    for line in delievery_log:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon} for total of ${amount}".format(
        count, melon, amount))
    delievery_log.close()

melon_count("Day 1", "um-deliveries-20140519.txt")
melon_count("Day 2", "um-deliveries-20140520.txt")
melon_count("Day 3", "um-deliveries-20140521.txt")