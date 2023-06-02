module mymod
        implicit none
        interface bar
        subroutine bar_f08ts (a) bind(C, name="sync")
        implicit none
        type(*), dimension(..) :: a
        end subroutine
        end interface
end module

module pub
        implicit none

        interface sub
        subroutine pub_f08ts(a)
        implicit none
        type (*), dimension(..) :: a
        end subroutine
        end interface
end module

        subroutine pub_f08ts(a)
        use mymod
        implicit none
        type (*), dimension(..) :: a
        call bar(a)
        end subroutine

subroutine bugsub(a)
        use pub
        implicit none
        real :: a
        call sub(a)
end subroutine

program bug
        implicit none
        real a
        a = 1
        call bugsub(a)
end program
