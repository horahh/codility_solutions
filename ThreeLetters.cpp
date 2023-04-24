string solution(int A, int B) {
    // Implement your solution here

    int big = A;    
    char big_char = 'a';
    int little = B;
    char little_char='b';  
    int counter=-1;  
    if ( A < B)
    {
        big = B;
        big_char='b';
        little = A;
        little_char ='a';
    }
    string solution_result = string(big+little,big_char);

    int module = 3;
    int threshold = 2;
    if ( A == B)
    {
        module=2;
        threshold=1;
    }   
    
    auto replace_function=[&](char val){
        counter++;
        auto result=false;
        if( counter % module >= threshold ) 
        {
            little--;
            result= true;
        }
        if( counter%module < threshold)
        {
            big--;
            result = false;
        }
        if ( (big <= little) & (counter %module==module-1))
        {
            module=2;
            counter=0;
            threshold = 1;
        }        
        return result;
    };
    replace_if(solution_result.begin(),solution_result.end(),replace_function,little_char);
    //cout << solution_result <<endl;
    return solution_result;
}
