// you can use includes, for example:
#include <algorithm>
#include <numeric>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

vector<int> solution(vector<int> &A, int K) {
    // Implement your solution here

    vector<int> A_rotated(A.size(),0);

    if ( K==0 || A.size()==0)
    {
        return A;
    }

    K = K%A.size();

    copy(A.begin(),A.end()-K,A_rotated.begin()+K);
    copy(A.end()-K,A.end(),A_rotated.begin());
    return A_rotated;
}
