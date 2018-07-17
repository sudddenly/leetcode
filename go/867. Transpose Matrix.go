// runtime 32ms
func transpose(A [][]int) [][]int {
    n := len(A)
    m := len(A[0])
    T := make([][]int, m)

    for i := 0; i < m; i++ {
        T[i] = make([]int, n)
    }

    for i, Ai := range A {
        for j, v := range Ai {
            T[j][i] = v
        }
    }

    return T
}