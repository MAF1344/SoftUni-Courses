def gift_box_coverage():
    size_of_side = float(input())

    gift_box_area = 6 * size_of_side * size_of_side

    num_sheets = int(input())

    total_covered_area = 0

    for i in range(num_sheets):
        length = float(input())
        width = float(input())

        sheet_area = length * width

        if (i + 1) % 3 == 0:
            sheet_area *= 0.75

        if (i + 1) % 5 == 0:
            sheet_area = 0

        total_covered_area += sheet_area

    if total_covered_area >= gift_box_area:
        percentage_left = ((total_covered_area - gift_box_area) / total_covered_area) * 100
        print(f"You've covered the gift box!\n{percentage_left:.2f}% wrap paper left.")
    else:
        percentage_not_covered = ((gift_box_area - total_covered_area) / gift_box_area) * 100
        print(f"You are out of paper!\n{percentage_not_covered:.2f}% of the box is not covered.")

gift_box_coverage()