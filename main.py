def main():
    print("hello world")
    
  # reverse the list in place using .reverse()
    sorted_classes.reverse()
    print(sorted_classes)

    colors_a = ["blue", "turquoise", "baby blue", "red"]
    colors_b = ["burgundy", "orange", "blue", "brown"]

    # colors_a = colors_a + colors_b
    colors_a.extend(colors_b)
    print(colors_a)

    print("orange" in colors_a)
    print("pink" in colors_a)

    print(colors_a.index("orange"))
    print(colors_a.index("pink"))

    # get the frequency or count of an item in a list using listName.count(item)
    count = colors_a.count("blue")
    print(f"There are {count} blue!")

    # task - updating a list item from turquoise to green
    colors_a[colors_a.index("turqoise")] = "green"
    print(colors_a)

if __name__ == "__main__":
    main()
