class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l_row = 0
        r_row = len(matrix) - 1

        while l_row <= r_row:
            m_row = int((l_row + r_row) / 2)
            cur_row = matrix[m_row]

            if target < cur_row[0]:
                r_row = m_row - 1
            elif target > cur_row[len(cur_row) - 1]:
                l_row = m_row + 1
            else:
                l = 0
                r = len(cur_row) - 1

                while l <= r:
                    mid = int((l + r) / 2)
                    cur = cur_row[mid]

                    if target < cur:
                        r = mid - 1
                    elif target > cur:
                        l = mid + 1
                    else:
                        return True
                
                return False

        return False

        