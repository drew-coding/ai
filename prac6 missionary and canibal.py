from collections import deque

def is_valid_state(m_left, c_left, m_right, c_right):
    if m_left < 0 or m_left > 3 or c_left < 0 or c_left > 3:
        return False
    if m_right < 0 or m_right > 3 or c_right < 0 or c_right > 3:
        return False
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True

def BFS():
    initial_state = (3, 3, 0)
    goal_state = (0, 0, 1)
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        (m_left, c_left, boat_pos), path = queue.popleft()
        if (m_left, c_left, boat_pos) == goal_state:
            return path

        for m_move in range(4):
            for c_move in range(4):
                if 1 <= m_move + c_move <= 2:
                    if boat_pos == 0:
                        new_m_left = m_left - m_move
                        new_c_left = c_left - c_move
                        new_m_right = 3 - new_m_left
                        new_c_right = 3 - new_c_left
                        new_boat_pos = 1
                    else:
                        new_m_left = m_left + m_move
                        new_c_left = c_left + c_move
                        new_m_right = 3 - new_m_left
                        new_c_right = 3 - new_c_left
                        new_boat_pos = 0

                    if is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                        new_state = (new_m_left, new_c_left, new_boat_pos)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, path + [(m_move, c_move, new_boat_pos)]))

    return None

def print_solution(path):
    if path is None:
        print("No solution found!")
        return

    for i, step in enumerate(path):
        m_move, c_move, boat_pos = step
        side = "left" if boat_pos == 0 else "right"
        print(f"Step {i+1}: Move {m_move} missionaries and {c_move} cannibals to the {side} side.")

if __name__ == "__main__":
    print_solution(BFS())
