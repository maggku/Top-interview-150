"""
Easy
Topics
premium lock iconCompanies
Hint

You are given an integer array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""

#(y1-y0)(xi-x0)=(y1-y0)(x1-x0)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #(x0-x1)/(y0-y1)=(x-x2)/(y-y2)
        #(x0-x1)(y-y2)=(x-x2)(y0-y1)
        #dx(y-y2)=(x-x2)dy

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x0-x1
        dy = y0 - y1

        for x, y in coordinates:
            if dx * (y - y0) != dy * (x - x0):
                return False
        return True