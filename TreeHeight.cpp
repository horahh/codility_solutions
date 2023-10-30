int get_height(tree * T, int height)
{
    if ( T== NULL )
    {
        return height;
    }
    height+=1;
    height=max(get_height(T->l,height),get_height(T->r,height));
    return height;
}

int solution(tree * T) {
    // Implement your solution here  
    return get_height(T, -1);
}
