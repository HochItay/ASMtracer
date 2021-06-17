integer function iterative_pow (a, b)     
    implicit none      
    integer :: a, b
    integer :: result = 1
    integer :: i = 0

    do while (i < b)
        result = result * a
        i = i + 1
    end do

    iterative_pow = result   
end function iterative_pow

recursive integer function recursive_pow (a, b)    result(r)
    implicit none      
    integer :: a, b

    if (b == 0) then      
        r = 1  
    else
        r = recursive_pow(a, b-1) * a
    end if  
end function recursive_pow

program test
    implicit none

    integer,external :: iterative_pow
    integer,external :: recursive_pow
    
    integer :: a = 2
    integer :: b = 6

    integer :: iterative_pow_res
    integer :: recursive_pow_res
    iterative_pow_res = iterative_pow(a, b)
    recursive_pow_res = recursive_pow(a, b)

    print *, "the result of ", a, " to the power of ", b, " using iterative_pow is ", iterative_pow_res, "\n"
    print *, "the result of ", a, " to the power of ", b, " using recursive_pow is ", recursive_pow_res, "\n"
end program test