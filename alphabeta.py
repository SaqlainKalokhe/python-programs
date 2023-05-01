import math

def alphabeta(nodeIndex, depth, alpha, beta, isMaximizing, scores):
    if depth == 0 or len(scores) == 1:
        return scores[0]

    if isMaximizing:
        bestValue = -math.inf
        for i in range(len(scores) // 2):

            value = alphabeta(nodeIndex * 2 + i, depth - 1,
                              alpha, beta, False, scores)

            bestValue = max(bestValue, value)

            alpha = max(alpha, bestValue)

            if alpha >= beta:
                break

        print("Value of alpha at node", nodeIndex, ":", alpha)

        return bestValue

    else:

        bestValue = math.inf
        for i in range(len(scores) // 2, len(scores)):

            value = alphabeta(nodeIndex * 2 + i, depth -
                              1, alpha, beta, True, scores)

            bestValue = min(bestValue, value)

            beta = min(beta, bestValue)

            if alpha >= beta:
                break

        print("Value of beta at node", nodeIndex, ":", beta)

        return bestValue


scores = [3, 5, 2, 9, 12, 5, 23, 23]
print("The optimal value is:", alphabeta(
    0, 3, -math.inf, math.inf, True, scores))
