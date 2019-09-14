;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

    for x in range(0,1000):
        while SortingRobot.can_move_right(self) == True:
            SortingRobot.swap_item(self)
            SortingRobot.move_right(self)
            if SortingRobot.compare_item(self) == -1:
                SortingRobot.move_left(self)
                SortingRobot.swap_item(self)
                SortingRobot.move_right(self)
                SortingRobot.move_right(self)
                print(SortingRobot.light_is_on(self))
            else:
                SortingRobot.swap_item(self)
                SortingRobot.set_light_on(self)
                SortingRobot.move_left(self)
                SortingRobot.swap_item(self)
                SortingRobot.move_right(self)
                print(SortingRobot.light_is_on(self))

        while SortingRobot.can_move_left(self) == True:
            SortingRobot.move_left(self)
