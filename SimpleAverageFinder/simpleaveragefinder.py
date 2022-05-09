total = 0
count = 0
finished = False

while finished == False:
    entry = input("Number here: ")
    if entry.lower() == "done":
        finished = True
        print("Results: Total:", total,
          "Count:", count,
          "Average:", (total/count))
    elif entry.lower() != "done":
        try:
            float_entry = float(entry)
        except:
            print("Invalid input")
        else:
            total += float_entry
            count += 1
    
