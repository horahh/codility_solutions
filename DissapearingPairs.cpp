
#include <algorithm>
#include <numeric>


string solution1(string &S) {
    // Implement your solution here

    string Final = S;
    size_t output_index = 0;
    for ( size_t input_index=0; input_index < S.size(); input_index++)
    {
        //cout << "input: " << S[input_index] << " output "  << Final[output_index] << "\n";
        // insert char
        if (output_index ==0  || S[input_index] != Final[output_index-1])
        {
            Final[output_index] = S[input_index];
            output_index ++;
            continue;
        }
        // delete char
        if (output_index >0 || S[input_index] == Final[output_index-1])
        {
            output_index--;
        }
    }
    Final.resize(output_index);
    return Final;
}




string solution2(string &S) {
    // Implement your solution here
    string result="";
    auto push_delete = [&](char c){ 
        if (result.size() == 0 || c != result.back()) 
        {
            result.push_back(c) ;
        } else {
            result.pop_back();
        }
    };

    std::for_each(S.begin(),S.end(),push_delete);
    return result;
}
