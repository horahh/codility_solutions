// you can use includes, for example:
#include <algorithm>
#include <numeric>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int fib(int i)
{
    if ( i <= 1) return i;
    return fib(i-1)+ i;
}

int solution(int M, vector<int> &A) {
    // Implement your solution here
    vector<int> slice_content(M+1,0);    
    int result =0;
    int element_count = 0;
    

    auto add_element=[&](int e)
    {
        if ( e > M) cout << "error";
        if (slice_content[e])
        {
            result+=fib(element_count);
            element_count=0;         
            std::fill(slice_content.begin(),slice_content.end(),0);
                     
        }
        slice_content[e]=1;
        element_count++;
    };
    std::for_each(A.begin(),A.end(),add_element);
    add_element(A.back());

    return result;
}


