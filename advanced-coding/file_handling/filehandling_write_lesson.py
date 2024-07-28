with open("love.txt", "w") as f:
    f.write("I love Python.\n")
    f.write("I love Scala.\n")

    f.writelines([
        "I love Fortran.\n"
        "I love pascal.\n"
    ])